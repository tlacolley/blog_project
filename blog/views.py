# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from .models import Article 

# Create your views here.
class IndexView(ListView):
	model = Article