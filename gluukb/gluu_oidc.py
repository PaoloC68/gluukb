# -*- coding: utf-8 -*-
__author__ = 'paolo'
from urllib import urlencode
from urllib2 import Request

from oauth2 import Request as OAuthRequest

from django.utils import simplejson

from social_auth.utils import setting, dsa_urlopen
from social_auth.backends import OpenIdAuth, ConsumerBasedOAuth, BaseOAuth2, \
                                 OAuthBackend, OpenIDBackend
from social_auth.exceptions import AuthFailed
GLUU_OAUTH2_SERVER = 'seed.gluu.org'
GLUU_OATUH2_AUTHORIZATION_URL = 'https://accounts.google.com/o/oauth2/auth'
GLUU_OAUTH2_SCOPE = ['openid',
                       'email']
GLUUAPIS_PROFILE = 'https://seed.gluu.org/oxauth/seam/resource/restv1/oxauth/userinfo'
GLUUAPIS_EMAIL = 'email'


class GluuOAuth2Backend(OAuthBackend):
    """Google OAuth2 authentication backend"""
    name = 'gluu'

    def get_user_id(self, details, response):
        """Use google email as unique id"""
        return details['email']

    def get_user_details(self, response):
        """Return user details from Orkut account"""
        email = response.get('email', '')
        return {'username': email.split('@', 1)[0],
                'email': email,
                'fullname': '',
                'first_name': '',
                'last_name': ''}

    EXTRA_DATA = [
        ('refresh_token', 'refresh_token', True),
        ('expires_in', 'expires'),
        ('token_type', 'token_type', True)
    ]

    def get_user_id(self, details, response):
        """Use google email or id as unique id"""
        user_id = super(GluuOAuth2Backend, self).get_user_id(details,
                                                               response)
        if setting('GLUU_OAUTH2_USE_UNIQUE_USER_ID', False):
            return response['id']
        return user_id

    def get_user_details(self, response):
        email = response.get('email', '')
        return {'username': email.split('@', 1)[0],
                'email': email,
                'fullname': response.get('name', ''),
                'first_name': response.get('given_name', ''),
                'last_name': response.get('family_name', '')}

_OAUTH2_KEY_NAME = setting('GLUU_OAUTH2_CLIENT_ID') and \
                   'GLUU_OAUTH2_CLIENT_ID' or \
                   'GLUU_OAUTH2_CLIENT_SECRET'

class GluuOAuth2(BaseOAuth2):
    """Gluu OAuth2 support"""
    AUTH_BACKEND = GluuOAuth2Backend
    AUTHORIZATION_URL = 'https://seed.gluu.org/oxauth/seam/resource/restv1/oxauth/authorize'
    ACCESS_TOKEN_URL = 'https://seed.gluu.org/oxauth/seam/resource/restv1/oxauth/token'
    SETTINGS_KEY_NAME = _OAUTH2_KEY_NAME
    SETTINGS_SECRET_NAME = 'GLUU_OAUTH2_CLIENT_SECRET'
    SCOPE_VAR_NAME = 'GLUU_OAUTH_EXTRA_SCOPE'
    DEFAULT_SCOPE = GLUU_OAUTH2_SCOPE
    REDIRECT_STATE = False

    def user_data(self, access_token, *args, **kwargs):
        """Return user data from Google API"""
        return gluuapis_profile(GLUUAPIS_PROFILE, access_token)

def gluuapis_profile(url, access_token):
    """
    Loads user data from googleapis service, such as name, given_name,
    family_name, etc. as it's described in:
    https://developers.google.com/accounts/docs/OAuth2Login
    """
    data = {'access_token': access_token, 'alt': 'json'}
    request = Request(url + '?' + urlencode(data))
    try:
        return simplejson.loads(dsa_urlopen(request).read())
    except (ValueError, KeyError, IOError):
        return None

BACKENDS = {
    'gluu': GluuOAuth2,
}
