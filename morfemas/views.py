#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from morfemas.models import *
from django.template import RequestContext,Context, loader
import calendar,datetime
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render, redirect
from django.conf import settings
import re
import json
import os
import tempfile
import zipfile 

def morfemas(request):
	t = loader.get_template('morfemas.html')
	c={'request':request}
	
	return HttpResponse(t.render(c))

def search(request):

	t = loader.get_template('search.html')
	
	q = request.GET
	keys=[i for i in q.dict().keys()]
	k = keys[0]
	
	search = Text.objects.filter(col1__contains=q[k])
	a = []
	b = []
	c = []
	for i in search:
		a.append(i.col1)
		b.append(i.col2)
		c.append(i.col3)

	s = {'col1':a,'col2':b,'col3':c}	

	c={'request':request,
		'search':s}
		
	return HttpResponse(t.render(c))

