# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist

__author__ = 'paolo'
from sugarlink.models import QuestionReference
from sugarmodels.models import Account, Case, Contact, Note


def pre_init_callback(sender, **kwargs):
    print 'pre_init', sender, kwargs


def post_init_callback(sender, **kwargs):
    print 'post_init', sender, kwargs


def post_save_question_callback(sender, instance, created, **kwargs):
    if created:
        case_priority = u'P0'
        try:
            contact = Contact.objects.filter(emails__email_address__icontains=instance.user.email)[0]
            account = contact.account_set.all()[0]
            if account.account_type == u'Customer' or contact.custom.named_contact_c == 1:
                case_priority = u'P1'

        except (IndexError, TypeError, AttributeError, ObjectDoesNotExist):
            contact = None
            account = None



        case = Case(name=instance.title, description=instance.body, account=account, priority=case_priority)
        case.save()
        question_reference = QuestionReference(case=case, question=instance)
        question_reference.save()

        if contact:
            case.contactcase_set.create(contact=contact, case=case)

def post_save_response_callback(sender, instance, created, **kwargs):
    if created:
        question_reference = QuestionReference.objects.get(question=instance.question)
        note = Note(name= question_reference.case.name + ' (Response)', parent_type = 'Cases', parent_id = question_reference.case_id,  description = instance.body)
        note.save()

