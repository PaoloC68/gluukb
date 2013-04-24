# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Accounts(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=150L, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    account_type = models.CharField(max_length=50L, blank=True)
    industry = models.CharField(max_length=50L, blank=True)
    annual_revenue = models.CharField(max_length=100L, blank=True)
    phone_fax = models.CharField(max_length=100L, blank=True)
    billing_address_street = models.CharField(max_length=150L, blank=True)
    billing_address_city = models.CharField(max_length=100L, blank=True)
    billing_address_state = models.CharField(max_length=100L, blank=True)
    billing_address_postalcode = models.CharField(max_length=20L, blank=True)
    billing_address_country = models.CharField(max_length=255L, blank=True)
    rating = models.CharField(max_length=100L, blank=True)
    phone_office = models.CharField(max_length=100L, blank=True)
    phone_alternate = models.CharField(max_length=100L, blank=True)
    website = models.CharField(max_length=255L, blank=True)
    ownership = models.CharField(max_length=100L, blank=True)
    employees = models.CharField(max_length=10L, blank=True)
    ticker_symbol = models.CharField(max_length=10L, blank=True)
    shipping_address_street = models.CharField(max_length=150L, blank=True)
    shipping_address_city = models.CharField(max_length=100L, blank=True)
    shipping_address_state = models.CharField(max_length=100L, blank=True)
    shipping_address_postalcode = models.CharField(max_length=20L, blank=True)
    shipping_address_country = models.CharField(max_length=255L, blank=True)
    parent_id = models.CharField(max_length=36L, blank=True)
    sic_code = models.CharField(max_length=10L, blank=True)
    campaign_id = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'accounts'

class AccountsAudit(models.Model):
    id = models.CharField(max_length=36L)
    parent_id = models.CharField(max_length=36L)
    date_created = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    field_name = models.CharField(max_length=100L, blank=True)
    data_type = models.CharField(max_length=100L, blank=True)
    before_value_string = models.CharField(max_length=255L, blank=True)
    after_value_string = models.CharField(max_length=255L, blank=True)
    before_value_text = models.TextField(blank=True)
    after_value_text = models.TextField(blank=True)
    class Meta:
        db_table = 'accounts_audit'

class AccountsBugs(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    account_id = models.CharField(max_length=36L, blank=True)
    bug_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'accounts_bugs'

class AccountsCases(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    account_id = models.CharField(max_length=36L, blank=True)
    case_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'accounts_cases'

class AccountsContacts(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    contact_id = models.CharField(max_length=36L, blank=True)
    account_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'accounts_contacts'

class AccountsCstm(models.Model):
    id_c = models.CharField(max_length=36L, primary_key=True)
    domain_c = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'accounts_cstm'

class AccountsOpportunities(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    opportunity_id = models.CharField(max_length=36L, blank=True)
    account_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'accounts_opportunities'

class AclActions(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    name = models.CharField(max_length=150L, blank=True)
    category = models.CharField(max_length=100L, blank=True)
    acltype = models.CharField(max_length=100L, blank=True)
    aclaccess = models.IntegerField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'acl_actions'

class AclRoles(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    name = models.CharField(max_length=150L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'acl_roles'

class AclRolesActions(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    role_id = models.CharField(max_length=36L, blank=True)
    action_id = models.CharField(max_length=36L, blank=True)
    access_override = models.IntegerField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'acl_roles_actions'

class AclRolesUsers(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    role_id = models.CharField(max_length=36L, blank=True)
    user_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'acl_roles_users'

class AddressBook(models.Model):
    assigned_user_id = models.CharField(max_length=36L)
    bean = models.CharField(max_length=50L, blank=True)
    bean_id = models.CharField(max_length=36L)
    class Meta:
        db_table = 'address_book'

class AsteriskLog(models.Model):
    id = models.IntegerField(primary_key=True)
    call_record_id = models.CharField(max_length=36L, blank=True)
    asterisk_id = models.CharField(max_length=45L, blank=True)
    callstate = models.CharField(max_length=10L, blank=True)
    callerid = models.CharField(max_length=45L, db_column='callerID', blank=True) # Field name made lowercase.
    callername = models.CharField(max_length=45L, db_column='callerName', blank=True) # Field name made lowercase.
    channel = models.CharField(max_length=30L, blank=True)
    timestampcall = models.DateTimeField(null=True, db_column='timestampCall', blank=True) # Field name made lowercase.
    timestamplink = models.DateTimeField(null=True, db_column='timestampLink', blank=True) # Field name made lowercase.
    timestamphangup = models.DateTimeField(null=True, db_column='timestampHangup', blank=True) # Field name made lowercase.
    direction = models.CharField(max_length=1L, blank=True)
    hangup_cause = models.IntegerField(null=True, blank=True)
    hangup_cause_txt = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'asterisk_log'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80L, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100L)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128L)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=30L, unique=True)
    first_name = models.CharField(max_length=30L)
    last_name = models.CharField(max_length=30L)
    email = models.CharField(max_length=75L)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class Bugs(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    bug_number = models.IntegerField()
    type = models.CharField(max_length=255L, blank=True)
    status = models.CharField(max_length=100L, blank=True)
    priority = models.CharField(max_length=100L, blank=True)
    resolution = models.CharField(max_length=255L, blank=True)
    work_log = models.TextField(blank=True)
    found_in_release = models.CharField(max_length=255L, blank=True)
    fixed_in_release = models.CharField(max_length=255L, blank=True)
    source = models.CharField(max_length=255L, blank=True)
    product_category = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'bugs'

class BugsAudit(models.Model):
    id = models.CharField(max_length=36L)
    parent_id = models.CharField(max_length=36L)
    date_created = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    field_name = models.CharField(max_length=100L, blank=True)
    data_type = models.CharField(max_length=100L, blank=True)
    before_value_string = models.CharField(max_length=255L, blank=True)
    after_value_string = models.CharField(max_length=255L, blank=True)
    before_value_text = models.TextField(blank=True)
    after_value_text = models.TextField(blank=True)
    class Meta:
        db_table = 'bugs_audit'

class Calls(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=50L, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    duration_hours = models.IntegerField(null=True, blank=True)
    duration_minutes = models.IntegerField(null=True, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    date_end = models.DateTimeField(null=True, blank=True)
    parent_type = models.CharField(max_length=255L, blank=True)
    status = models.CharField(max_length=100L, blank=True)
    direction = models.CharField(max_length=100L, blank=True)
    parent_id = models.CharField(max_length=36L, blank=True)
    reminder_time = models.IntegerField(null=True, blank=True)
    outlook_id = models.CharField(max_length=255L, blank=True)
    email_reminder_time = models.IntegerField(null=True, blank=True)
    email_reminder_sent = models.IntegerField(null=True, blank=True)
    repeat_type = models.CharField(max_length=36L, blank=True)
    repeat_interval = models.IntegerField(null=True, blank=True)
    repeat_dow = models.CharField(max_length=7L, blank=True)
    repeat_until = models.DateField(null=True, blank=True)
    repeat_count = models.IntegerField(null=True, blank=True)
    repeat_parent_id = models.CharField(max_length=36L, blank=True)
    recurring_source = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'calls'

class CallsContacts(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    call_id = models.CharField(max_length=36L, blank=True)
    contact_id = models.CharField(max_length=36L, blank=True)
    required = models.CharField(max_length=1L, blank=True)
    accept_status = models.CharField(max_length=25L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'calls_contacts'

class CallsCstm(models.Model):
    id_c = models.CharField(max_length=36L, primary_key=True)
    class Meta:
        db_table = 'calls_cstm'

class CallsLeads(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    call_id = models.CharField(max_length=36L, blank=True)
    lead_id = models.CharField(max_length=36L, blank=True)
    required = models.CharField(max_length=1L, blank=True)
    accept_status = models.CharField(max_length=25L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'calls_leads'

class CallsUsers(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    call_id = models.CharField(max_length=36L, blank=True)
    user_id = models.CharField(max_length=36L, blank=True)
    required = models.CharField(max_length=1L, blank=True)
    accept_status = models.CharField(max_length=25L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'calls_users'

class CampaignLog(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    campaign_id = models.CharField(max_length=36L, blank=True)
    target_tracker_key = models.CharField(max_length=36L, blank=True)
    target_id = models.CharField(max_length=36L, blank=True)
    target_type = models.CharField(max_length=100L, blank=True)
    activity_type = models.CharField(max_length=100L, blank=True)
    activity_date = models.DateTimeField(null=True, blank=True)
    related_id = models.CharField(max_length=36L, blank=True)
    related_type = models.CharField(max_length=100L, blank=True)
    archived = models.IntegerField(null=True, blank=True)
    hits = models.IntegerField(null=True, blank=True)
    list_id = models.CharField(max_length=36L, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    more_information = models.CharField(max_length=100L, blank=True)
    marketing_id = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'campaign_log'

class CampaignTrkrs(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    tracker_name = models.CharField(max_length=30L, blank=True)
    tracker_url = models.CharField(max_length=255L, blank=True)
    tracker_key = models.IntegerField()
    campaign_id = models.CharField(max_length=36L, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    is_optout = models.IntegerField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'campaign_trkrs'

class Campaigns(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=50L, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    tracker_key = models.IntegerField()
    tracker_count = models.IntegerField(null=True, blank=True)
    refer_url = models.CharField(max_length=255L, blank=True)
    tracker_text = models.CharField(max_length=255L, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100L, blank=True)
    impressions = models.IntegerField(null=True, blank=True)
    currency_id = models.CharField(max_length=36L, blank=True)
    budget = models.FloatField(null=True, blank=True)
    expected_cost = models.FloatField(null=True, blank=True)
    actual_cost = models.FloatField(null=True, blank=True)
    expected_revenue = models.FloatField(null=True, blank=True)
    campaign_type = models.CharField(max_length=100L, blank=True)
    objective = models.TextField(blank=True)
    content = models.TextField(blank=True)
    frequency = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'campaigns'

class CampaignsAudit(models.Model):
    id = models.CharField(max_length=36L)
    parent_id = models.CharField(max_length=36L)
    date_created = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    field_name = models.CharField(max_length=100L, blank=True)
    data_type = models.CharField(max_length=100L, blank=True)
    before_value_string = models.CharField(max_length=255L, blank=True)
    after_value_string = models.CharField(max_length=255L, blank=True)
    before_value_text = models.TextField(blank=True)
    after_value_text = models.TextField(blank=True)
    class Meta:
        db_table = 'campaigns_audit'

class Cases(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    case_number = models.IntegerField()
    type = models.CharField(max_length=255L, blank=True)
    status = models.CharField(max_length=100L, blank=True)
    priority = models.CharField(max_length=100L, blank=True)
    resolution = models.TextField(blank=True)
    work_log = models.TextField(blank=True)
    account_id = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'cases'

class CasesAudit(models.Model):
    id = models.CharField(max_length=36L)
    parent_id = models.CharField(max_length=36L)
    date_created = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    field_name = models.CharField(max_length=100L, blank=True)
    data_type = models.CharField(max_length=100L, blank=True)
    before_value_string = models.CharField(max_length=255L, blank=True)
    after_value_string = models.CharField(max_length=255L, blank=True)
    before_value_text = models.TextField(blank=True)
    after_value_text = models.TextField(blank=True)
    class Meta:
        db_table = 'cases_audit'

class CasesBugs(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    case_id = models.CharField(max_length=36L, blank=True)
    bug_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'cases_bugs'

class Config(models.Model):
    category = models.CharField(max_length=32L, blank=True)
    name = models.CharField(max_length=32L, blank=True)
    value = models.TextField(blank=True)
    class Meta:
        db_table = 'config'

class Contacts(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    salutation = models.CharField(max_length=255L, blank=True)
    first_name = models.CharField(max_length=100L, blank=True)
    last_name = models.CharField(max_length=100L, blank=True)
    title = models.CharField(max_length=100L, blank=True)
    department = models.CharField(max_length=255L, blank=True)
    do_not_call = models.IntegerField(null=True, blank=True)
    phone_home = models.CharField(max_length=100L, blank=True)
    phone_mobile = models.CharField(max_length=100L, blank=True)
    phone_work = models.CharField(max_length=100L, blank=True)
    phone_other = models.CharField(max_length=100L, blank=True)
    phone_fax = models.CharField(max_length=100L, blank=True)
    primary_address_street = models.CharField(max_length=150L, blank=True)
    primary_address_city = models.CharField(max_length=100L, blank=True)
    primary_address_state = models.CharField(max_length=100L, blank=True)
    primary_address_postalcode = models.CharField(max_length=20L, blank=True)
    primary_address_country = models.CharField(max_length=255L, blank=True)
    alt_address_street = models.CharField(max_length=150L, blank=True)
    alt_address_city = models.CharField(max_length=100L, blank=True)
    alt_address_state = models.CharField(max_length=100L, blank=True)
    alt_address_postalcode = models.CharField(max_length=20L, blank=True)
    alt_address_country = models.CharField(max_length=255L, blank=True)
    assistant = models.CharField(max_length=75L, blank=True)
    assistant_phone = models.CharField(max_length=100L, blank=True)
    lead_source = models.CharField(max_length=255L, blank=True)
    reports_to_id = models.CharField(max_length=36L, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    portal_name = models.CharField(max_length=255L, blank=True)
    portal_active = models.IntegerField()
    portal_app = models.CharField(max_length=255L, blank=True)
    campaign_id = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'contacts'

class ContactsAudit(models.Model):
    id = models.CharField(max_length=36L)
    parent_id = models.CharField(max_length=36L)
    date_created = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    field_name = models.CharField(max_length=100L, blank=True)
    data_type = models.CharField(max_length=100L, blank=True)
    before_value_string = models.CharField(max_length=255L, blank=True)
    after_value_string = models.CharField(max_length=255L, blank=True)
    before_value_text = models.TextField(blank=True)
    after_value_text = models.TextField(blank=True)
    class Meta:
        db_table = 'contacts_audit'

class ContactsBugs(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    contact_id = models.CharField(max_length=36L, blank=True)
    bug_id = models.CharField(max_length=36L, blank=True)
    contact_role = models.CharField(max_length=50L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'contacts_bugs'

class ContactsCases(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    contact_id = models.CharField(max_length=36L, blank=True)
    case_id = models.CharField(max_length=36L, blank=True)
    contact_role = models.CharField(max_length=50L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'contacts_cases'

class ContactsCstm(models.Model):
    id_c = models.CharField(max_length=36L, primary_key=True)
    linkedin_c = models.CharField(max_length=128L, blank=True)
    twitter_c = models.CharField(max_length=64L, blank=True)
    skype_c = models.CharField(max_length=64L, blank=True)
    google_c = models.CharField(max_length=64L, blank=True)
    contact_type_c = models.TextField(blank=True)
    seen_demo_c = models.IntegerField(null=True, blank=True)
    demo_date_c = models.DateField(null=True, blank=True)
    named_contact_c = models.IntegerField(null=True, blank=True)
    billing_contact_c = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'contacts_cstm'

class ContactsUsers(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    contact_id = models.CharField(max_length=36L, blank=True)
    user_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'contacts_users'

class Currencies(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=36L, blank=True)
    symbol = models.CharField(max_length=36L, blank=True)
    iso4217 = models.CharField(max_length=3L, blank=True)
    conversion_rate = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=100L, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=36L)
    class Meta:
        db_table = 'currencies'

class CustomFields(models.Model):
    bean_id = models.CharField(max_length=36L, blank=True)
    set_num = models.IntegerField(null=True, blank=True)
    field0 = models.CharField(max_length=255L, blank=True)
    field1 = models.CharField(max_length=255L, blank=True)
    field2 = models.CharField(max_length=255L, blank=True)
    field3 = models.CharField(max_length=255L, blank=True)
    field4 = models.CharField(max_length=255L, blank=True)
    field5 = models.CharField(max_length=255L, blank=True)
    field6 = models.CharField(max_length=255L, blank=True)
    field7 = models.CharField(max_length=255L, blank=True)
    field8 = models.CharField(max_length=255L, blank=True)
    field9 = models.CharField(max_length=255L, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'custom_fields'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200L)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    app_label = models.CharField(max_length=100L)
    model = models.CharField(max_length=100L)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40L, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100L)
    name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'django_site'

class DocumentRevisions(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    change_log = models.CharField(max_length=255L, blank=True)
    document_id = models.CharField(max_length=36L, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    filename = models.CharField(max_length=255L, blank=True)
    file_ext = models.CharField(max_length=100L, blank=True)
    file_mime_type = models.CharField(max_length=100L, blank=True)
    revision = models.CharField(max_length=100L, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    doc_id = models.CharField(max_length=100L, blank=True)
    doc_type = models.CharField(max_length=100L, blank=True)
    doc_url = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'document_revisions'

class Documents(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    document_name = models.CharField(max_length=255L, blank=True)
    active_date = models.DateField(null=True, blank=True)
    exp_date = models.DateField(null=True, blank=True)
    category_id = models.CharField(max_length=100L, blank=True)
    subcategory_id = models.CharField(max_length=100L, blank=True)
    status_id = models.CharField(max_length=100L, blank=True)
    document_revision_id = models.CharField(max_length=36L, blank=True)
    related_doc_id = models.CharField(max_length=36L, blank=True)
    related_doc_rev_id = models.CharField(max_length=36L, blank=True)
    is_template = models.IntegerField(null=True, blank=True)
    template_type = models.CharField(max_length=100L, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    doc_id = models.CharField(max_length=100L, blank=True)
    doc_type = models.CharField(max_length=100L, blank=True)
    doc_url = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'documents'

class DocumentsAccounts(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    document_id = models.CharField(max_length=36L, blank=True)
    account_id = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'documents_accounts'

class DocumentsBugs(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    document_id = models.CharField(max_length=36L, blank=True)
    bug_id = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'documents_bugs'

class DocumentsCases(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    document_id = models.CharField(max_length=36L, blank=True)
    case_id = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'documents_cases'

class DocumentsContacts(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    document_id = models.CharField(max_length=36L, blank=True)
    contact_id = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'documents_contacts'

class DocumentsOpportunities(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    document_id = models.CharField(max_length=36L, blank=True)
    opportunity_id = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'documents_opportunities'

class Eapm(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    password = models.CharField(max_length=255L, blank=True)
    url = models.CharField(max_length=255L, blank=True)
    application = models.CharField(max_length=100L, blank=True)
    api_data = models.TextField(blank=True)
    consumer_key = models.CharField(max_length=255L, blank=True)
    consumer_secret = models.CharField(max_length=255L, blank=True)
    oauth_token = models.CharField(max_length=255L, blank=True)
    oauth_secret = models.CharField(max_length=255L, blank=True)
    validated = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'eapm'

class EmailAddrBeanRel(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    email_address_id = models.CharField(max_length=36L)
    bean_id = models.CharField(max_length=36L)
    bean_module = models.CharField(max_length=100L, blank=True)
    primary_address = models.IntegerField(null=True, blank=True)
    reply_to_address = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'email_addr_bean_rel'

class EmailAddresses(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    email_address = models.CharField(max_length=255L, blank=True)
    email_address_caps = models.CharField(max_length=255L, blank=True)
    invalid_email = models.IntegerField(null=True, blank=True)
    opt_out = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'email_addresses'

class EmailCache(models.Model):
    ie_id = models.CharField(max_length=36L)
    mbox = models.CharField(max_length=60L, blank=True)
    subject = models.CharField(max_length=255L, blank=True)
    fromaddr = models.CharField(max_length=100L, blank=True)
    toaddr = models.CharField(max_length=255L, blank=True)
    senddate = models.DateTimeField(null=True, blank=True)
    message_id = models.CharField(max_length=255L, blank=True)
    mailsize = models.IntegerField(null=True, blank=True)
    imap_uid = models.IntegerField(null=True, blank=True)
    msgno = models.IntegerField(null=True, blank=True)
    recent = models.IntegerField(null=True, blank=True)
    flagged = models.IntegerField(null=True, blank=True)
    answered = models.IntegerField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    seen = models.IntegerField(null=True, blank=True)
    draft = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'email_cache'

class EmailMarketing(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    name = models.CharField(max_length=255L, blank=True)
    from_name = models.CharField(max_length=100L, blank=True)
    from_addr = models.CharField(max_length=100L, blank=True)
    reply_to_name = models.CharField(max_length=100L, blank=True)
    reply_to_addr = models.CharField(max_length=100L, blank=True)
    inbound_email_id = models.CharField(max_length=36L, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    template_id = models.CharField(max_length=36L)
    status = models.CharField(max_length=100L, blank=True)
    campaign_id = models.CharField(max_length=36L, blank=True)
    all_prospect_lists = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'email_marketing'

class EmailMarketingProspectLists(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    prospect_list_id = models.CharField(max_length=36L, blank=True)
    email_marketing_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'email_marketing_prospect_lists'

class EmailTemplates(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    published = models.CharField(max_length=3L, blank=True)
    name = models.CharField(max_length=255L, blank=True)
    description = models.TextField(blank=True)
    subject = models.CharField(max_length=255L, blank=True)
    body = models.TextField(blank=True)
    body_html = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    text_only = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    type = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'email_templates'

class Emailman(models.Model):
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    user_id = models.CharField(max_length=36L, blank=True)
    id = models.IntegerField(primary_key=True)
    campaign_id = models.CharField(max_length=36L, blank=True)
    marketing_id = models.CharField(max_length=36L, blank=True)
    list_id = models.CharField(max_length=36L, blank=True)
    send_date_time = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    in_queue = models.IntegerField(null=True, blank=True)
    in_queue_date = models.DateTimeField(null=True, blank=True)
    send_attempts = models.IntegerField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    related_id = models.CharField(max_length=36L, blank=True)
    related_type = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'emailman'

class Emails(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_sent = models.DateTimeField(null=True, blank=True)
    message_id = models.CharField(max_length=255L, blank=True)
    name = models.CharField(max_length=255L, blank=True)
    type = models.CharField(max_length=100L, blank=True)
    status = models.CharField(max_length=100L, blank=True)
    flagged = models.IntegerField(null=True, blank=True)
    reply_to_status = models.IntegerField(null=True, blank=True)
    intent = models.CharField(max_length=100L, blank=True)
    mailbox_id = models.CharField(max_length=36L, blank=True)
    parent_type = models.CharField(max_length=100L, blank=True)
    parent_id = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'emails'

class EmailsBeans(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    email_id = models.CharField(max_length=36L, blank=True)
    bean_id = models.CharField(max_length=36L, blank=True)
    bean_module = models.CharField(max_length=100L, blank=True)
    campaign_data = models.TextField(blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'emails_beans'

class EmailsEmailAddrRel(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    email_id = models.CharField(max_length=36L)
    address_type = models.CharField(max_length=4L, blank=True)
    email_address_id = models.CharField(max_length=36L)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'emails_email_addr_rel'

class EmailsText(models.Model):
    email_id = models.CharField(max_length=36L, primary_key=True)
    from_addr = models.CharField(max_length=255L, blank=True)
    reply_to_addr = models.CharField(max_length=255L, blank=True)
    to_addrs = models.TextField(blank=True)
    cc_addrs = models.TextField(blank=True)
    bcc_addrs = models.TextField(blank=True)
    description = models.TextField(blank=True)
    description_html = models.TextField(blank=True)
    raw_source = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'emails_text'

class Feeds(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    deleted = models.IntegerField()
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    title = models.CharField(max_length=100L, blank=True)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'feeds'

class FieldsMetaData(models.Model):
    id = models.CharField(max_length=255L, primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    vname = models.CharField(max_length=255L, blank=True)
    comments = models.CharField(max_length=255L, blank=True)
    help = models.CharField(max_length=255L, blank=True)
    custom_module = models.CharField(max_length=255L, blank=True)
    type = models.CharField(max_length=255L, blank=True)
    len = models.IntegerField(null=True, blank=True)
    required = models.IntegerField(null=True, blank=True)
    default_value = models.CharField(max_length=255L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    audited = models.IntegerField(null=True, blank=True)
    massupdate = models.IntegerField(null=True, blank=True)
    duplicate_merge = models.IntegerField(null=True, blank=True)
    reportable = models.IntegerField(null=True, blank=True)
    importable = models.CharField(max_length=255L, blank=True)
    ext1 = models.CharField(max_length=255L, blank=True)
    ext2 = models.CharField(max_length=255L, blank=True)
    ext3 = models.CharField(max_length=255L, blank=True)
    ext4 = models.TextField(blank=True)
    class Meta:
        db_table = 'fields_meta_data'

class Folders(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=25L, blank=True)
    folder_type = models.CharField(max_length=25L, blank=True)
    parent_folder = models.CharField(max_length=36L, blank=True)
    has_child = models.IntegerField(null=True, blank=True)
    is_group = models.IntegerField(null=True, blank=True)
    is_dynamic = models.IntegerField(null=True, blank=True)
    dynamic_query = models.TextField(blank=True)
    assign_to_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L)
    modified_by = models.CharField(max_length=36L)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'folders'

class FoldersRel(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    folder_id = models.CharField(max_length=36L)
    polymorphic_module = models.CharField(max_length=25L, blank=True)
    polymorphic_id = models.CharField(max_length=36L)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'folders_rel'

class FoldersSubscriptions(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    folder_id = models.CharField(max_length=36L)
    assigned_user_id = models.CharField(max_length=36L)
    class Meta:
        db_table = 'folders_subscriptions'

class ImportMaps(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=254L, blank=True)
    source = models.CharField(max_length=36L, blank=True)
    enclosure = models.CharField(max_length=1L, blank=True)
    delimiter = models.CharField(max_length=1L, blank=True)
    module = models.CharField(max_length=36L, blank=True)
    content = models.TextField(blank=True)
    default_values = models.TextField(blank=True)
    has_header = models.IntegerField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    is_published = models.CharField(max_length=3L, blank=True)
    class Meta:
        db_table = 'import_maps'

class InboundEmail(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    name = models.CharField(max_length=255L, blank=True)
    status = models.CharField(max_length=100L, blank=True)
    server_url = models.CharField(max_length=100L, blank=True)
    email_user = models.CharField(max_length=100L, blank=True)
    email_password = models.CharField(max_length=100L, blank=True)
    port = models.IntegerField(null=True, blank=True)
    service = models.CharField(max_length=50L, blank=True)
    mailbox = models.TextField(blank=True)
    delete_seen = models.IntegerField(null=True, blank=True)
    mailbox_type = models.CharField(max_length=10L, blank=True)
    template_id = models.CharField(max_length=36L, blank=True)
    stored_options = models.TextField(blank=True)
    group_id = models.CharField(max_length=36L, blank=True)
    is_personal = models.IntegerField(null=True, blank=True)
    groupfolder_id = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'inbound_email'

class InboundEmailAutoreply(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    autoreplied_to = models.CharField(max_length=100L, blank=True)
    ie_id = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'inbound_email_autoreply'

class InboundEmailCacheTs(models.Model):
    id = models.CharField(max_length=255L, primary_key=True)
    ie_timestamp = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'inbound_email_cache_ts'

class JobQueue(models.Model):
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    scheduler_id = models.CharField(max_length=36L, blank=True)
    execute_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20L, blank=True)
    resolution = models.CharField(max_length=20L, blank=True)
    message = models.TextField(blank=True)
    target = models.CharField(max_length=255L, blank=True)
    data = models.TextField(blank=True)
    requeue = models.IntegerField(null=True, blank=True)
    retry_count = models.IntegerField(null=True, blank=True)
    failure_count = models.IntegerField(null=True, blank=True)
    job_delay = models.IntegerField(null=True, blank=True)
    client = models.CharField(max_length=255L, blank=True)
    percent_complete = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'job_queue'

class KnowledgeCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    added = models.DateTimeField()
    lastchanged = models.DateTimeField()
    title = models.CharField(max_length=255L)
    slug = models.CharField(max_length=50L)
    class Meta:
        db_table = 'knowledge_category'

class KnowledgeQuestion(models.Model):
    id = models.IntegerField(primary_key=True)
    added = models.DateTimeField()
    lastchanged = models.DateTimeField()
    user = models.ForeignKey(AuthUser, null=True, blank=True)
    name = models.CharField(max_length=64L, blank=True)
    email = models.CharField(max_length=75L, blank=True)
    title = models.CharField(max_length=255L)
    body = models.TextField(blank=True)
    status = models.CharField(max_length=32L)
    locked = models.IntegerField()
    alert = models.IntegerField()
    class Meta:
        db_table = 'knowledge_question'

class KnowledgeQuestionCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.ForeignKey(KnowledgeQuestion)
    category = models.ForeignKey(KnowledgeCategory)
    class Meta:
        db_table = 'knowledge_question_categories'

class KnowledgeResponse(models.Model):
    id = models.IntegerField(primary_key=True)
    added = models.DateTimeField()
    lastchanged = models.DateTimeField()
    user = models.ForeignKey(AuthUser, null=True, blank=True)
    name = models.CharField(max_length=64L, blank=True)
    email = models.CharField(max_length=75L, blank=True)
    question = models.ForeignKey(KnowledgeQuestion)
    body = models.TextField(blank=True)
    status = models.CharField(max_length=32L)
    accepted = models.IntegerField()
    alert = models.IntegerField()
    class Meta:
        db_table = 'knowledge_response'

class Leads(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    salutation = models.CharField(max_length=255L, blank=True)
    first_name = models.CharField(max_length=100L, blank=True)
    last_name = models.CharField(max_length=100L, blank=True)
    title = models.CharField(max_length=100L, blank=True)
    department = models.CharField(max_length=100L, blank=True)
    do_not_call = models.IntegerField(null=True, blank=True)
    phone_home = models.CharField(max_length=100L, blank=True)
    phone_mobile = models.CharField(max_length=100L, blank=True)
    phone_work = models.CharField(max_length=100L, blank=True)
    phone_other = models.CharField(max_length=100L, blank=True)
    phone_fax = models.CharField(max_length=100L, blank=True)
    primary_address_street = models.CharField(max_length=150L, blank=True)
    primary_address_city = models.CharField(max_length=100L, blank=True)
    primary_address_state = models.CharField(max_length=100L, blank=True)
    primary_address_postalcode = models.CharField(max_length=20L, blank=True)
    primary_address_country = models.CharField(max_length=255L, blank=True)
    alt_address_street = models.CharField(max_length=150L, blank=True)
    alt_address_city = models.CharField(max_length=100L, blank=True)
    alt_address_state = models.CharField(max_length=100L, blank=True)
    alt_address_postalcode = models.CharField(max_length=20L, blank=True)
    alt_address_country = models.CharField(max_length=255L, blank=True)
    assistant = models.CharField(max_length=75L, blank=True)
    assistant_phone = models.CharField(max_length=100L, blank=True)
    converted = models.IntegerField(null=True, blank=True)
    refered_by = models.CharField(max_length=100L, blank=True)
    lead_source = models.CharField(max_length=100L, blank=True)
    lead_source_description = models.TextField(blank=True)
    status = models.CharField(max_length=100L, blank=True)
    status_description = models.TextField(blank=True)
    reports_to_id = models.CharField(max_length=36L, blank=True)
    account_name = models.CharField(max_length=255L, blank=True)
    account_description = models.TextField(blank=True)
    contact_id = models.CharField(max_length=36L, blank=True)
    account_id = models.CharField(max_length=36L, blank=True)
    opportunity_id = models.CharField(max_length=36L, blank=True)
    opportunity_name = models.CharField(max_length=255L, blank=True)
    opportunity_amount = models.CharField(max_length=50L, blank=True)
    campaign_id = models.CharField(max_length=36L, blank=True)
    portal_name = models.CharField(max_length=255L, blank=True)
    portal_app = models.CharField(max_length=255L, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    website = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'leads'

class LeadsAudit(models.Model):
    id = models.CharField(max_length=36L)
    parent_id = models.CharField(max_length=36L)
    date_created = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    field_name = models.CharField(max_length=100L, blank=True)
    data_type = models.CharField(max_length=100L, blank=True)
    before_value_string = models.CharField(max_length=255L, blank=True)
    after_value_string = models.CharField(max_length=255L, blank=True)
    before_value_text = models.TextField(blank=True)
    after_value_text = models.TextField(blank=True)
    class Meta:
        db_table = 'leads_audit'

class LinkedDocuments(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    parent_id = models.CharField(max_length=36L, blank=True)
    parent_type = models.CharField(max_length=25L, blank=True)
    document_id = models.CharField(max_length=36L, blank=True)
    document_revision_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'linked_documents'

class Meetings(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=50L, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    location = models.CharField(max_length=50L, blank=True)
    duration_hours = models.IntegerField(null=True, blank=True)
    duration_minutes = models.IntegerField(null=True, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    date_end = models.DateTimeField(null=True, blank=True)
    parent_type = models.CharField(max_length=100L, blank=True)
    status = models.CharField(max_length=100L, blank=True)
    parent_id = models.CharField(max_length=36L, blank=True)
    reminder_time = models.IntegerField(null=True, blank=True)
    outlook_id = models.CharField(max_length=255L, blank=True)
    password = models.CharField(max_length=50L, blank=True)
    join_url = models.CharField(max_length=200L, blank=True)
    host_url = models.CharField(max_length=400L, blank=True)
    displayed_url = models.CharField(max_length=400L, blank=True)
    creator = models.CharField(max_length=50L, blank=True)
    external_id = models.CharField(max_length=50L, blank=True)
    type = models.CharField(max_length=255L, blank=True)
    sequence = models.IntegerField(null=True, blank=True)
    email_reminder_time = models.IntegerField(null=True, blank=True)
    email_reminder_sent = models.IntegerField(null=True, blank=True)
    repeat_type = models.CharField(max_length=36L, blank=True)
    repeat_interval = models.IntegerField(null=True, blank=True)
    repeat_dow = models.CharField(max_length=7L, blank=True)
    repeat_until = models.DateField(null=True, blank=True)
    repeat_count = models.IntegerField(null=True, blank=True)
    repeat_parent_id = models.CharField(max_length=36L, blank=True)
    recurring_source = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'meetings'

class MeetingsContacts(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    meeting_id = models.CharField(max_length=36L, blank=True)
    contact_id = models.CharField(max_length=36L, blank=True)
    required = models.CharField(max_length=1L, blank=True)
    accept_status = models.CharField(max_length=25L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'meetings_contacts'

class MeetingsLeads(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    meeting_id = models.CharField(max_length=36L, blank=True)
    lead_id = models.CharField(max_length=36L, blank=True)
    required = models.CharField(max_length=1L, blank=True)
    accept_status = models.CharField(max_length=25L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'meetings_leads'

class MeetingsUsers(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    meeting_id = models.CharField(max_length=36L, blank=True)
    user_id = models.CharField(max_length=36L, blank=True)
    required = models.CharField(max_length=1L, blank=True)
    accept_status = models.CharField(max_length=25L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'meetings_users'

class Notes(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    name = models.CharField(max_length=255L, blank=True)
    filename = models.CharField(max_length=255L, blank=True)
    file_mime_type = models.CharField(max_length=100L, blank=True)
    parent_type = models.CharField(max_length=255L, blank=True)
    parent_id = models.CharField(max_length=36L, blank=True)
    contact_id = models.CharField(max_length=36L, blank=True)
    portal_flag = models.IntegerField(null=True, blank=True)
    embed_flag = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'notes'

class NotesCstm(models.Model):
    id_c = models.CharField(max_length=36L, primary_key=True)
    demo_c = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'notes_cstm'

class OauthConsumer(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    c_key = models.CharField(max_length=255L, unique=True, blank=True)
    c_secret = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'oauth_consumer'

class OauthNonce(models.Model):
    conskey = models.CharField(max_length=32L)
    nonce = models.CharField(max_length=32L)
    nonce_ts = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'oauth_nonce'

class OauthTokens(models.Model):
    id = models.CharField(max_length=36L)
    secret = models.CharField(max_length=32L, blank=True)
    tstate = models.CharField(max_length=1L, blank=True)
    consumer = models.CharField(max_length=36L)
    token_ts = models.BigIntegerField(null=True, blank=True)
    verify = models.CharField(max_length=32L, blank=True)
    deleted = models.IntegerField()
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    callback_url = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'oauth_tokens'

class Opportunities(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=50L, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    opportunity_type = models.CharField(max_length=255L, blank=True)
    campaign_id = models.CharField(max_length=36L, blank=True)
    lead_source = models.CharField(max_length=50L, blank=True)
    amount = models.FloatField(null=True, blank=True)
    amount_usdollar = models.FloatField(null=True, blank=True)
    currency_id = models.CharField(max_length=36L, blank=True)
    date_closed = models.DateField(null=True, blank=True)
    next_step = models.CharField(max_length=100L, blank=True)
    sales_stage = models.CharField(max_length=255L, blank=True)
    probability = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'opportunities'

class OpportunitiesAudit(models.Model):
    id = models.CharField(max_length=36L)
    parent_id = models.CharField(max_length=36L)
    date_created = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    field_name = models.CharField(max_length=100L, blank=True)
    data_type = models.CharField(max_length=100L, blank=True)
    before_value_string = models.CharField(max_length=255L, blank=True)
    after_value_string = models.CharField(max_length=255L, blank=True)
    before_value_text = models.TextField(blank=True)
    after_value_text = models.TextField(blank=True)
    class Meta:
        db_table = 'opportunities_audit'

class OpportunitiesContacts(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    contact_id = models.CharField(max_length=36L, blank=True)
    opportunity_id = models.CharField(max_length=36L, blank=True)
    contact_role = models.CharField(max_length=50L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'opportunities_contacts'

class OutboundEmail(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=50L, blank=True)
    type = models.CharField(max_length=15L, blank=True)
    user_id = models.CharField(max_length=36L)
    mail_sendtype = models.CharField(max_length=8L, blank=True)
    mail_smtpserver = models.CharField(max_length=100L, blank=True)
    mail_smtpport = models.IntegerField(null=True, blank=True)
    mail_smtpuser = models.CharField(max_length=100L, blank=True)
    mail_smtppass = models.CharField(max_length=100L, blank=True)
    mail_smtpauth_req = models.IntegerField(null=True, blank=True)
    mail_smtpssl = models.IntegerField(null=True, blank=True)
    mail_smtptype = models.CharField(max_length=20L, blank=True)
    class Meta:
        db_table = 'outbound_email'

class PbundleItems(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    bundle_id = models.CharField(max_length=36L)
    product_id = models.CharField(max_length=36L, blank=True)
    product_name = models.TextField(blank=True)
    product_description = models.TextField(blank=True)
    users = models.IntegerField(null=True, blank=True)
    ulimit = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'pbundle_items'

class Pbundles(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    available = models.IntegerField(null=True, blank=True)
    name = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'pbundles'

class Products(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    short_description = models.CharField(max_length=255L, blank=True)
    long_description = models.TextField(blank=True)
    image = models.CharField(max_length=200L, blank=True)
    image_filename = models.CharField(max_length=200L, blank=True)
    product_page_url = models.CharField(max_length=255L, blank=True)
    available = models.IntegerField(null=True, blank=True)
    list_price = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    default_users = models.IntegerField(null=True, blank=True)
    default_limit = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'products'

class Project(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    name = models.CharField(max_length=50L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    estimated_start_date = models.DateField(null=True, blank=True)
    estimated_end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=255L, blank=True)
    priority = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'project'

class ProjectTask(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    project_id = models.CharField(max_length=36L, blank=True)
    project_task_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50L, blank=True)
    status = models.CharField(max_length=255L, blank=True)
    description = models.TextField(blank=True)
    predecessors = models.TextField(blank=True)
    date_start = models.DateField(null=True, blank=True)
    time_start = models.IntegerField(null=True, blank=True)
    time_finish = models.IntegerField(null=True, blank=True)
    date_finish = models.DateField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    duration_unit = models.TextField(blank=True)
    actual_duration = models.IntegerField(null=True, blank=True)
    percent_complete = models.IntegerField(null=True, blank=True)
    parent_task_id = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    priority = models.CharField(max_length=255L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    milestone_flag = models.IntegerField(null=True, blank=True)
    order_number = models.IntegerField(null=True, blank=True)
    task_number = models.IntegerField(null=True, blank=True)
    estimated_effort = models.IntegerField(null=True, blank=True)
    actual_effort = models.IntegerField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    utilization = models.IntegerField(null=True, blank=True)
    date_due = models.DateField(null=True, blank=True)
    time_due = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'project_task'

class ProjectTaskAudit(models.Model):
    id = models.CharField(max_length=36L)
    parent_id = models.CharField(max_length=36L)
    date_created = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    field_name = models.CharField(max_length=100L, blank=True)
    data_type = models.CharField(max_length=100L, blank=True)
    before_value_string = models.CharField(max_length=255L, blank=True)
    after_value_string = models.CharField(max_length=255L, blank=True)
    before_value_text = models.TextField(blank=True)
    after_value_text = models.TextField(blank=True)
    class Meta:
        db_table = 'project_task_audit'

class ProjectsAccounts(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    account_id = models.CharField(max_length=36L, blank=True)
    project_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'projects_accounts'

class ProjectsBugs(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    bug_id = models.CharField(max_length=36L, blank=True)
    project_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'projects_bugs'

class ProjectsCases(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    case_id = models.CharField(max_length=36L, blank=True)
    project_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'projects_cases'

class ProjectsContacts(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    contact_id = models.CharField(max_length=36L, blank=True)
    project_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'projects_contacts'

class ProjectsOpportunities(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    opportunity_id = models.CharField(max_length=36L, blank=True)
    project_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'projects_opportunities'

class ProjectsProducts(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    product_id = models.CharField(max_length=36L, blank=True)
    project_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'projects_products'

class ProspectListCampaigns(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    prospect_list_id = models.CharField(max_length=36L, blank=True)
    campaign_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'prospect_list_campaigns'

class ProspectLists(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=50L, blank=True)
    list_type = models.CharField(max_length=100L, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    domain_name = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'prospect_lists'

class ProspectListsProspects(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    prospect_list_id = models.CharField(max_length=36L, blank=True)
    related_id = models.CharField(max_length=36L, blank=True)
    related_type = models.CharField(max_length=25L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'prospect_lists_prospects'

class Prospects(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    salutation = models.CharField(max_length=255L, blank=True)
    first_name = models.CharField(max_length=100L, blank=True)
    last_name = models.CharField(max_length=100L, blank=True)
    title = models.CharField(max_length=100L, blank=True)
    department = models.CharField(max_length=255L, blank=True)
    do_not_call = models.IntegerField(null=True, blank=True)
    phone_home = models.CharField(max_length=100L, blank=True)
    phone_mobile = models.CharField(max_length=100L, blank=True)
    phone_work = models.CharField(max_length=100L, blank=True)
    phone_other = models.CharField(max_length=100L, blank=True)
    phone_fax = models.CharField(max_length=100L, blank=True)
    primary_address_street = models.CharField(max_length=150L, blank=True)
    primary_address_city = models.CharField(max_length=100L, blank=True)
    primary_address_state = models.CharField(max_length=100L, blank=True)
    primary_address_postalcode = models.CharField(max_length=20L, blank=True)
    primary_address_country = models.CharField(max_length=255L, blank=True)
    alt_address_street = models.CharField(max_length=150L, blank=True)
    alt_address_city = models.CharField(max_length=100L, blank=True)
    alt_address_state = models.CharField(max_length=100L, blank=True)
    alt_address_postalcode = models.CharField(max_length=20L, blank=True)
    alt_address_country = models.CharField(max_length=255L, blank=True)
    assistant = models.CharField(max_length=75L, blank=True)
    assistant_phone = models.CharField(max_length=100L, blank=True)
    tracker_key = models.IntegerField()
    birthdate = models.DateField(null=True, blank=True)
    lead_id = models.CharField(max_length=36L, blank=True)
    account_name = models.CharField(max_length=150L, blank=True)
    campaign_id = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'prospects'

class Relationships(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    relationship_name = models.CharField(max_length=150L, blank=True)
    lhs_module = models.CharField(max_length=100L, blank=True)
    lhs_table = models.CharField(max_length=64L, blank=True)
    lhs_key = models.CharField(max_length=64L, blank=True)
    rhs_module = models.CharField(max_length=100L, blank=True)
    rhs_table = models.CharField(max_length=64L, blank=True)
    rhs_key = models.CharField(max_length=64L, blank=True)
    join_table = models.CharField(max_length=64L, blank=True)
    join_key_lhs = models.CharField(max_length=64L, blank=True)
    join_key_rhs = models.CharField(max_length=64L, blank=True)
    relationship_type = models.CharField(max_length=64L, blank=True)
    relationship_role_column = models.CharField(max_length=64L, blank=True)
    relationship_role_column_value = models.CharField(max_length=50L, blank=True)
    reverse = models.IntegerField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'relationships'

class Releases(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    name = models.CharField(max_length=50L, blank=True)
    list_order = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'releases'

class Roles(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    name = models.CharField(max_length=150L, blank=True)
    description = models.TextField(blank=True)
    modules = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'roles'

class RolesModules(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    role_id = models.CharField(max_length=36L, blank=True)
    module_id = models.CharField(max_length=36L, blank=True)
    allow = models.IntegerField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'roles_modules'

class RolesUsers(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    role_id = models.CharField(max_length=36L, blank=True)
    user_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'roles_users'

class SavedSearch(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=150L, blank=True)
    search_module = models.CharField(max_length=150L, blank=True)
    deleted = models.IntegerField()
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    contents = models.TextField(blank=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'saved_search'

class Schedulers(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    name = models.CharField(max_length=255L, blank=True)
    job = models.CharField(max_length=255L, blank=True)
    date_time_start = models.DateTimeField(null=True, blank=True)
    date_time_end = models.DateTimeField(null=True, blank=True)
    job_interval = models.CharField(max_length=100L, blank=True)
    time_from = models.TextField(blank=True) # This field type is a guess.
    time_to = models.TextField(blank=True) # This field type is a guess.
    last_run = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=100L, blank=True)
    catch_up = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'schedulers'

class SchedulersTimes(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    deleted = models.IntegerField()
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    scheduler_id = models.CharField(max_length=36L)
    execute_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'schedulers_times'

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255L)
    migration = models.CharField(max_length=255L)
    applied = models.DateTimeField()
    class Meta:
        db_table = 'south_migrationhistory'

class Sugarfeed(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    description = models.CharField(max_length=255L, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    related_module = models.CharField(max_length=100L, blank=True)
    related_id = models.CharField(max_length=36L, blank=True)
    link_url = models.CharField(max_length=255L, blank=True)
    link_type = models.CharField(max_length=30L, blank=True)
    class Meta:
        db_table = 'sugarfeed'

class Tasks(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=50L, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    status = models.CharField(max_length=100L, blank=True)
    date_due_flag = models.IntegerField(null=True, blank=True)
    date_due = models.DateTimeField(null=True, blank=True)
    date_start_flag = models.IntegerField(null=True, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    parent_type = models.CharField(max_length=255L, blank=True)
    parent_id = models.CharField(max_length=36L, blank=True)
    contact_id = models.CharField(max_length=36L, blank=True)
    priority = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'tasks'

class Tracker(models.Model):
    id = models.IntegerField(primary_key=True)
    monitor_id = models.CharField(max_length=36L)
    user_id = models.CharField(max_length=36L, blank=True)
    module_name = models.CharField(max_length=255L, blank=True)
    item_id = models.CharField(max_length=36L, blank=True)
    item_summary = models.CharField(max_length=255L, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    action = models.CharField(max_length=255L, blank=True)
    session_id = models.CharField(max_length=36L, blank=True)
    visible = models.IntegerField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'tracker'

class UpgradeHistory(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    filename = models.CharField(max_length=255L, blank=True)
    md5sum = models.CharField(max_length=32L, unique=True, blank=True)
    type = models.CharField(max_length=30L, blank=True)
    status = models.CharField(max_length=50L, blank=True)
    version = models.CharField(max_length=64L, blank=True)
    name = models.CharField(max_length=255L, blank=True)
    description = models.TextField(blank=True)
    id_name = models.CharField(max_length=255L, blank=True)
    manifest = models.TextField(blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    enabled = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'upgrade_history'

class UserPreferences(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    category = models.CharField(max_length=50L, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    assigned_user_id = models.CharField(max_length=36L)
    contents = models.TextField(blank=True)
    class Meta:
        db_table = 'user_preferences'

class Users(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    user_name = models.CharField(max_length=60L, blank=True)
    user_hash = models.CharField(max_length=255L, blank=True)
    authenticate_id = models.CharField(max_length=100L, blank=True)
    sugar_login = models.IntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=30L, blank=True)
    last_name = models.CharField(max_length=30L, blank=True)
    reports_to_id = models.CharField(max_length=36L, blank=True)
    is_admin = models.IntegerField(null=True, blank=True)
    receive_notifications = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    title = models.CharField(max_length=50L, blank=True)
    department = models.CharField(max_length=50L, blank=True)
    phone_home = models.CharField(max_length=50L, blank=True)
    phone_mobile = models.CharField(max_length=50L, blank=True)
    phone_work = models.CharField(max_length=50L, blank=True)
    phone_other = models.CharField(max_length=50L, blank=True)
    phone_fax = models.CharField(max_length=50L, blank=True)
    status = models.CharField(max_length=100L, blank=True)
    address_street = models.CharField(max_length=150L, blank=True)
    address_city = models.CharField(max_length=100L, blank=True)
    address_state = models.CharField(max_length=100L, blank=True)
    address_country = models.CharField(max_length=100L, blank=True)
    address_postalcode = models.CharField(max_length=20L, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    portal_only = models.IntegerField(null=True, blank=True)
    employee_status = models.CharField(max_length=100L, blank=True)
    messenger_id = models.CharField(max_length=100L, blank=True)
    messenger_type = models.CharField(max_length=100L, blank=True)
    is_group = models.IntegerField(null=True, blank=True)
    system_generated_password = models.IntegerField(null=True, blank=True)
    pwd_last_changed = models.DateTimeField(null=True, blank=True)
    external_auth_only = models.IntegerField(null=True, blank=True)
    show_on_employees = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'users'

class UsersCstm(models.Model):
    id_c = models.CharField(max_length=36L, primary_key=True)
    class Meta:
        db_table = 'users_cstm'

class UsersFeeds(models.Model):
    user_id = models.CharField(max_length=36L, blank=True)
    feed_id = models.CharField(max_length=36L, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'users_feeds'

class UsersLastImport(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    assigned_user_id = models.CharField(max_length=36L, blank=True)
    import_module = models.CharField(max_length=36L, blank=True)
    bean_type = models.CharField(max_length=36L, blank=True)
    bean_id = models.CharField(max_length=36L, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'users_last_import'

class UsersPasswordLink(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    username = models.CharField(max_length=36L, blank=True)
    date_generated = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'users_password_link'

class UsersSignatures(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=36L, blank=True)
    name = models.CharField(max_length=255L, blank=True)
    signature = models.TextField(blank=True)
    signature_html = models.TextField(blank=True)
    class Meta:
        db_table = 'users_signatures'

class Vcals(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    user_id = models.CharField(max_length=36L)
    type = models.CharField(max_length=100L, blank=True)
    source = models.CharField(max_length=100L, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = 'vcals'

class Versions(models.Model):
    id = models.CharField(max_length=36L, primary_key=True)
    deleted = models.IntegerField(null=True, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    name = models.CharField(max_length=255L, blank=True)
    file_version = models.CharField(max_length=255L, blank=True)
    db_version = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'versions'

