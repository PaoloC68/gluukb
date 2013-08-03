#-*- coding: utf-8 -*-

from django.views.generic import ListView
from knowledge.models import Question, Category
from knowledge.views import get_my_questions


class IndexView(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'django_knowledge/index.html'

    def get_queryset(self):
        qs = Question.objects.can_view(self.request.user).prefetch_related('responses__question')
        return qs

    def get_context_data(self, **kwargs):
        c = super(IndexView, self).get_context_data(**kwargs)
        c['categories'] = Category.objects.all()
        c['my_questions'] = get_my_questions(self.request)
        return c