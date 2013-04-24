from __future__ import unicode_literals
from django.db import models
from django_uuid.fields import UUIDField
from model_utils import Choices


PRIORITY = Choices(
    ('P0', 'Community'),
    ('P1', 'High'),
    ('P2', 'Medium'),
    ('P3', 'Low')
)
STATUS = Choices("New", "Assigned", "Closed", "Pending Input", "Rejected", "Duplicate")
TYPE = Choices(
    "Administration",
    "Product",
    "User"
)


class Account(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    name = models.CharField(max_length=150L, blank=True)
    date_entered = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
    modified_by_user = models.ForeignKey('SugarUser', db_column='modified_user_id', related_name='accounts_modified',
                                         null=True, blank=True)
    created_by = models.ForeignKey('SugarUser', related_name='account_created_by_user', db_column='created_by',
                                   null=True,
                                   blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(editable=False, default=0)
    assigned_user = models.ForeignKey('SugarUser', db_column='assigned_user_id', related_name='accounts_assigned',
                                      null=True, blank=True)
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
    parent_id = models.ForeignKey('Account', db_column='parent_id', null=True, blank=True)
    sic_code = models.CharField(max_length=10L, blank=True)
    contacts = models.ManyToManyField(
        'Contact',
        through='AccountContact',
    )
    emails = models.ManyToManyField(
        'EmailAddress',
        through='EmailAccount',
    )

    # campaign_id = models.CharField(max_length=36L, blank=True)

    def __unicode__(self):
        return self.name


    class Meta:
        db_table = 'accounts'
        managed = False
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'


class AccountBug(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    account_id = models.CharField(max_length=36L, blank=True)
    bug_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)

    class Meta:
        db_table = 'accounts_bugs'
        managed = False


class AccountCase(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    account_id = models.ForeignKey('Account', db_column='account_id')
    case = models.ForeignKey('Case', db_column='case_id')
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)

    class Meta:
        db_table = 'accounts_cases'
        managed = False


class AccountContact(models.Model):
    id = UUIDField(primary_key=True, auto=True)
    contact = models.ForeignKey('Contact', db_column='contact_id')
    account = models.ForeignKey('Account', db_column='account_id')
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)

    def __unicode__(self):
        return '{0} -> {1}'.format(self.contact.last_name, self.account.name)

    class Meta:
        db_table = 'accounts_contacts'
        managed = False


class AccountCstm(models.Model):
    id_c = models.CharField(max_length=36L, primary_key=True)
    domain_c = models.CharField(max_length=255L, blank=True)

    class Meta:
        db_table = 'accounts_cstm'
        managed = False


class AccountOpportunity(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    opportunity_id = models.CharField(max_length=36L, blank=True)
    account_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)

    class Meta:
        db_table = 'accounts_opportunities'
        managed = False


class AddressBook(models.Model):
    assigned_user_id = models.CharField(max_length=36L)
    bean = models.CharField(max_length=50L, blank=True)
    bean_id = models.CharField(max_length=36L)

    class Meta:
        db_table = 'address_book'
        managed = False


class Case(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    name = models.CharField(max_length=255L, blank=True, null=True)
    date_entered = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
    modified_by_user = models.ForeignKey('SugarUser', db_column='modified_user_id', related_name='cases_modified',
                                         blank=True, null=True, editable=False)
    created_by = models.ForeignKey('SugarUser', related_name='cases_created',
                                   blank=True,
                                   null=True,
                                   db_column='created_by',
                                   editable=False)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(editable=False, default=0)
    assigned_user = models.ForeignKey('SugarUser', db_column='assigned_user_id', related_name='cases_assigned',
                                      null=True,
                                      blank=True)
    case_number = models.IntegerField(null=True, editable=False)
    type = models.CharField(choices=TYPE, max_length=255L, blank=True, default=TYPE.Administration, null=True)
    status = models.CharField(choices=STATUS, max_length=100L, default=STATUS.New, null=True)
    priority = models.CharField(choices=PRIORITY, max_length=100L, default=PRIORITY.P1, null=True)
    resolution = models.TextField(blank=True, null=True)
    work_log = models.TextField(blank=True, null=True)
    account = models.ForeignKey('Account', db_column='account_id', null=True)
    contacts = models.ManyToManyField(
        'Contact',
        through='ContactCase',
        related_name='cases'
    )

    def __unicode__(self):
        return str(self.case_number) + ' ' + self.name

    class Meta:
        db_table = 'cases'
        managed = False
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'


class Contact(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    date_entered = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
    modified_by_user = models.ForeignKey('SugarUser', db_column='modified_user_id', related_name='contacts_modified',
                                         null=True, blank=True, editable=False)
    created_by = models.ForeignKey('SugarUser', db_column='created_by', related_name='contacts_created', null=True,
                                   blank=True, editable=False)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(editable=False, default=0)
    assigned_user = models.ForeignKey('SugarUser', related_name='contacts_assigned',
                                      null=True, blank=True)
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
    reports_to = models.ForeignKey('Contact', db_column='reports_to_id', null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    portal_name = models.CharField(max_length=255L, blank=True)
    portal_active = models.IntegerField(editable=False, default=0)
    portal_app = models.CharField(max_length=255L, blank=True)
    # campaign_id = models.CharField(max_length=36L, blank=True)
    emails = models.ManyToManyField(
        'EmailAddress',
        through='EmailContact',
    )

    def __unicode__(self):
        return self.last_name

    class Meta:
        db_table = 'contacts'
        managed = False
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class ContactCase(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    contact = models.ForeignKey('Contact', db_column='contact_id')
    case = models.ForeignKey('Case', db_column='case_id')
    contact_role = models.CharField(max_length=50L, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)

    class Meta:
        db_table = 'contacts_cases'
        managed = False


class ContactCstm(models.Model):
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
        managed = False


class ContactsUsers(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    contact_id = models.CharField(max_length=36L, blank=True)
    user_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)

    class Meta:
        db_table = 'contacts_users'
        managed = False


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
    deleted = models.IntegerField(editable=False, default=0)

    class Meta:
        db_table = 'custom_fields'
        managed = False


class DocumentRevisions(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    change_log = models.CharField(max_length=255L, blank=True)
    document_id = models.CharField(max_length=36L, blank=True)
    date_entered = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.CharField(max_length=36L, blank=True)
    filename = models.CharField(max_length=255L, blank=True)
    file_ext = models.CharField(max_length=100L, blank=True)
    file_mime_type = models.CharField(max_length=100L, blank=True)
    revision = models.CharField(max_length=100L, blank=True)
    deleted = models.IntegerField(editable=False, default=0)
    date_modified = models.DateTimeField(auto_now=True)
    doc_id = models.CharField(max_length=100L, blank=True)
    doc_type = models.CharField(max_length=100L, blank=True)
    doc_url = models.CharField(max_length=255L, blank=True)

    class Meta:
        db_table = 'document_revisions'
        managed = False


class Documents(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    date_entered = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(editable=False, default=0)
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
        managed = False


class DocumentsAccounts(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)
    document_id = models.CharField(max_length=36L, blank=True)
    account_id = models.CharField(max_length=36L, blank=True)

    class Meta:
        db_table = 'documents_accounts'
        managed = False


class DocumentsCases(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)
    document_id = models.CharField(max_length=36L, blank=True)
    case_id = models.CharField(max_length=36L, blank=True)

    class Meta:
        db_table = 'documents_cases'
        managed = False


class DocumentsContacts(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)
    document_id = models.CharField(max_length=36L, blank=True)
    contact_id = models.CharField(max_length=36L, blank=True)

    class Meta:
        db_table = 'documents_contacts'
        managed = False


class DocumentsOpportunities(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)
    document_id = models.CharField(max_length=36L, blank=True)
    opportunity_id = models.CharField(max_length=36L, blank=True)

    class Meta:
        db_table = 'documents_opportunities'


class EmailAccount(models.Model):
    email_accounts_id = UUIDField(primary_key=True, auto=True, null=False, db_column='id')
    email_address = models.ForeignKey('EmailAddress', db_column='email_address_id', related_name='accounts_of_email')
    account = models.ForeignKey('Account', editable=False, db_column='bean_id', related_name='emails_of_account',
                                null=True)
    bean_module = models.CharField(max_length=100L, blank=True, editable=False, default='Accounts')
    primary_address = models.IntegerField(null=True, blank=True, default=1)
    reply_to_address = models.IntegerField(null=True, blank=True, editable=False, default=0)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)

    class Meta:
        db_table = 'email_addr_bean_rel'
        managed = False
        verbose_name = 'Account Email'
        verbose_name_plural = 'Account Emails'


class EmailContact(models.Model):
    email_contacts_id = UUIDField(primary_key=True, auto=True, null=False, db_column='id')
    email_address = models.ForeignKey('EmailAddress', db_column='email_address_id', related_name='contacts_of_email')
    account = models.ForeignKey('Contact', editable=False, db_column='bean_id', related_name='email_of_contact',
                                null=True)
    bean_module = models.CharField(max_length=100L, blank=True, editable=False, default='Contacts')
    primary_address = models.IntegerField(null=True, blank=True, default=1)
    reply_to_address = models.IntegerField(null=True, blank=True, editable=False, default=0)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)

    class Meta:
        db_table = 'email_addr_bean_rel'
        managed = False
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'


class EmailAddress(models.Model):
    email_id = UUIDField(primary_key=True, auto=True, null=False, db_column='id')
    email_address = models.CharField(max_length=255L, blank=True)
    email_address_caps = models.CharField(max_length=255L, blank=True, editable=False)
    invalid_email = models.IntegerField(null=True, blank=True, default=0)
    opt_out = models.IntegerField(null=True, blank=True, default=0)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)

    def __unicode__(self):
        return self.email_address

    def save(self, **kwargs):
        self.email_address_caps = self.email_address.capitalize()
        super(EmailAddress, self).save(**kwargs)

    class Meta:
        db_table = 'email_addresses'
        managed = False


class LinkedDocuments(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    parent_id = models.CharField(max_length=36L, blank=True)
    parent_type = models.CharField(max_length=25L, blank=True)
    document_id = models.CharField(max_length=36L, blank=True)
    document_revision_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)

    class Meta:
        db_table = 'linked_documents'
        managed = False


class Note(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    date_entered = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
    modified_by_user = models.ForeignKey('SugarUser', db_column='modified_user_id', related_name='notes_modified')
    created_by = models.ForeignKey('SugarUser', related_name='notes_created', db_column='created_by')
    name = models.CharField(max_length=255L, blank=True)
    filename = models.CharField(max_length=255L, blank=True)
    file_mime_type = models.CharField(max_length=100L, blank=True)
    parent_type = models.CharField(max_length=255L, blank=True)
    parent_id = models.CharField(max_length=36L, blank=True)
    contact = models.ForeignKey('Contact', blank=True, db_column='contact_id', related_name='notes')
    portal_flag = models.IntegerField(null=True, blank=True)
    embed_flag = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    deleted = models.IntegerField(editable=False, default=0)
    assigned_user = models.ForeignKey('SugarUser', db_column='assigned_user_id', related_name='notes_assigned')

    class Meta:
        db_table = 'notes'
        managed = False
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'


class NotesCstm(models.Model):
    id_c = models.CharField(max_length=36L, primary_key=True)
    demo_c = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'notes_cstm'
        managed = False


class Relationships(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
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
    deleted = models.IntegerField(editable=False, default=0)

    class Meta:
        db_table = 'relationships'
        managed = False


class Roles(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    date_entered = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
    modified_user_id = models.CharField(max_length=36L, blank=True)
    created_by = models.CharField(max_length=36L, blank=True)
    name = models.CharField(max_length=150L, blank=True)
    description = models.TextField(blank=True)
    modules = models.TextField(blank=True)
    deleted = models.IntegerField(editable=False, default=0)

    class Meta:
        db_table = 'roles'
        managed = False


class RolesModules(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    role_id = models.CharField(max_length=36L, blank=True)
    module_id = models.CharField(max_length=36L, blank=True)
    allow = models.IntegerField(null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)

    class Meta:
        db_table = 'roles_modules'
        managed = False


class RolesUsers(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    role_id = models.CharField(max_length=36L, blank=True)
    user_id = models.CharField(max_length=36L, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(editable=False, default=0)

    class Meta:
        db_table = 'roles_users'
        managed = False


class SugarUser(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
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
    date_entered = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
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
    deleted = models.IntegerField(editable=False, default=0)
    portal_only = models.IntegerField(null=True, blank=True)
    employee_status = models.CharField(max_length=100L, blank=True)
    messenger_id = models.CharField(max_length=100L, blank=True)
    messenger_type = models.CharField(max_length=100L, blank=True)
    is_group = models.IntegerField(null=True, blank=True)
    system_generated_password = models.IntegerField(null=True, blank=True)
    pwd_last_changed = models.DateTimeField(null=True, blank=True)
    external_auth_only = models.IntegerField(null=True, blank=True)
    show_on_employees = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.user_name

    class Meta:
        db_table = 'users'
        managed = False
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class UserCstm(models.Model):
    id_c = models.CharField(max_length=36L, primary_key=True)

    class Meta:
        db_table = 'users_cstm'
        managed = False


class UserPasswordLink(models.Model):
    id = UUIDField(primary_key=True, auto=True, null=False)
    username = models.CharField(max_length=36L, blank=True)
    date_generated = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(editable=False, default=0)

    class Meta:
        db_table = 'users_password_link'

