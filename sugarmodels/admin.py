# -*- coding: utf-8 -*-
__author__ = 'paolo'
from django.contrib import admin
from models import Account, Contact, AccountContact, Case, EmailAccount, EmailContact, EmailAddress, ContactCase, ContactCstm

class ContactsAdminInline(admin.StackedInline):
    model = Contact

class ContactCstmAdmin(admin.ModelAdmin):
    inlines = (ContactsAdminInline,)

class AccountContactInline(admin.StackedInline):
    model = AccountContact
    extra = 1


class AccountEmailAddrInline(admin.StackedInline):
    model = EmailAccount


class ContactEmailAddrInline(admin.StackedInline):
    model = EmailContact


class ContactCaseInline(admin.StackedInline):
    model = ContactCase


class AccountsAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]
    inlines = (
        AccountEmailAddrInline,
        AccountContactInline,

    )


class ContactsAdmin(admin.ModelAdmin):
    search_fields = [
        'last_name',
        'first_name',
    ]

    inlines = (
        ContactEmailAddrInline,
        AccountContactInline,
    )


class CasesAdmin(admin.ModelAdmin):
    inlines = [

        ContactCaseInline,
    ]


class EmailAccountsAdmin(admin.ModelAdmin):
    pass


class EmailContactsAdmin(admin.ModelAdmin):
    pass


class EmailAddressesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Account, AccountsAdmin)
admin.site.register(Contact, ContactsAdmin)
admin.site.register(EmailAddress, EmailAddressesAdmin)
admin.site.register(Case, CasesAdmin)
admin.site.register(ContactCstm, ContactCstmAdmin)
