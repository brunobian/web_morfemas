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
import pandas as pd

def morfemas(request):
	t = loader.get_template('morfemas.html')
	c={'request':request}
	
	return HttpResponse(t.render(c))

def search(request):

	t = loader.get_template('search.html')
	
	q = request.GET
	keys=[i for i in q.dict().keys()]
	k = keys[0]
	
	warning = False
	if k == 'sufijo':
		por_palabra = False
		search = pd.DataFrame(list(Sufijo.objects.filter(sufijo=q[k]).values()))
		search = search[['sufijo', 'numero', 'count_afijada', 'frec_afijada', 'count_pseudoafijada', 'frec_pseudoafijada', 'prop_count_afij', 'prop_frec_afij']]
		search.columns = ['Sufijo', 'Número', 'Count afijadas', 'Freq afijadas', 'Count pseudoafijadas', 'Freq pseudoafijadas', 'Prop Count Afijadas', 'Prop Freq Afijadas']
		sufijo = q[k]
		if sufijo == 'aca':
			warning = True
	elif k == 'palabra':
		por_palabra = True
		search = pd.DataFrame(list(Palabra.objects.filter(palabra=q[k]).values()))
		search = search[['palabra', 'numero', 'sufijo', 'sufijada']]
		search.columns = ['Palabra', 'Número', 'Sufijo', 'Sufijada']
		sufijo = search['Sufijo'][0]
	elif k == 'palsPorSuj':
		por_palabra = True
		search = pd.DataFrame(list(Palabra.objects.filter(sufijo=q[k]).values()))		
		search = search[['palabra', 'numero', 'sufijo', 'sufijada']]
		search.columns = ['Palabra', 'Número', 'Sufijo', 'Sufijada']
		sufijo = search['Sufijo'][0]
	
	s_html = search.to_html(index=False)
	
	if q['bajar'] == 'True':
		search.to_csv(path_or_buf=response)

	c={'request':request,
		'search':s_html,
		'por_palabra':por_palabra,
		'sufijo':sufijo,
		'warning':warning}
		
	return HttpResponse(t.render(c))

