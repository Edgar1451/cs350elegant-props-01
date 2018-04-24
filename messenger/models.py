# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Message(models.Model):
	subject_char = models.CharField(max_length=128)
	message_text = models.TextField()
	date_time = models.DateTimeField(auto_now_add=True)
	email = models.EmailField(max_length=254)
	