# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic

from .models import Message

# Create your views here.
class MessageListView(generic.ListView):
    model = Message
    template_name = "messenger/list.html"

class MessageDetailView(generic.DetailView):
    model = Message
    template_name = "messenger/detail.html"
