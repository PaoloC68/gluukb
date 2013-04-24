from django.db import models

# Create your models here.
from django.db.models import signals
from django.contrib.auth.models import Group
from knowledge.models import Question, Response
from sugarmodels.models import Case


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

