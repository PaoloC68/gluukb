#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import template

register = template.Library()

@register.filter
def in_category(things, category):
    return things.filter(categories=category)