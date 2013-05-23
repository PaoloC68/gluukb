from django.db import models

# Create your models here.
from django.db.models import signals
from django.contrib.auth.models import Group
from knowledge.models import Question, Response
from sugarmodels.models import Case
from django.db.models.base import ObjectDoesNotExist

from django.contrib.auth.models import User
from sugarmodels.models import Account, Case, Contact, Note


@property
def is_customer(self):
    is_customer = False
    for contact in Contact.objects.filter(emails__email_address__icontains=self.email):
        try:
            account = contact.account_set.filter(account_type__icontains='customer')
            if account.count() > 0:
                is_customer = True
                break
            else:
                is_customer = False
        except ObjectDoesNotExist:
            is_customer = False
    return is_customer

@property
def is_named(self):
    is_named = False
    for contact in Contact.objects.filter(emails__email_address__icontains=self.email):
        try:
            if contact.custom.named_contact_c == 1:
                is_named = True
                break
            else:
                is_named = False
        except ObjectDoesNotExist:
            is_named = False
    return is_named

User.add_to_class("is_customer", is_customer)
User.add_to_class("is_named", is_named)


class QuestionReference(models.Model):
    case = models.OneToOneField(Case)
    question = models.OneToOneField(Question)

    def __unicode__(self):
        return 'Case {0} {1}'.format(self.case.case_number, self.case.name)

from sugarlink.signals import pre_init_callback, post_init_callback, post_save_question_callback, post_save_response_callback

signals.pre_init.connect(pre_init_callback, sender=Group)

signals.post_init.connect(post_init_callback, sender=Group)

signals.post_save.connect(post_save_question_callback, sender=Question)

signals.post_save.connect(post_save_response_callback, sender=Response)

