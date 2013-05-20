# Create your views here.
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('knowledge_index'))