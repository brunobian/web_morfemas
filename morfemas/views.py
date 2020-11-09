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
	
	plurYalomorfos = pd.read_csv("/data/pluralesYalomorfos.csv")

	t = loader.get_template('search.html')
	
	q = request.GET
	keys=[i for i in q.dict().keys()]
	k = keys[0]
	
	warning = False
	empty   = False
	if k == 'sufijo':
		search = pd.DataFrame(list(Sufijo.objects.filter(sufijo=q[k].lower()).values()))
		try:
			search = search[['sufijo', 'numero', 'frec_afijada', 'frec_pseudoafijada', 'prop_frec_afij', 'count_afijada', 'count_pseudoafijada',  'prop_count_afij', ]]
			search.columns = ['Sufijo', 'Número', 'Frec. Token Afijadas', 'Frec. Token Pseudoafijadas', 'Prop. Token Afijadas', 'Frec. Type Afijadas', 'Frec. Type Pseudoafijadas', 'Prop. Type Afijadas']
			
			
			q[k]
			
			
			newSearch = q[k]
			if newSearch == 'aca':
				warning = True		
		except:
			newSearch = q[k]
	elif k == 'palabra':
		search = pd.DataFrame(list(Palabra.objects.filter(palabra=q[k].lower()).values()))
		try:
			search = search[['palabra', 'numero','freq', 'sufijo', 'sufijada']]
			search.columns = ['Palabra', 'Número','Frec. léxica', 'Terminación', 'Sufijo']
			newSearch = search['Terminación'][0]
		except:	
			newSearch = ''
	elif k == 'palsPorSuf':
		search = pd.DataFrame(list(Palabra.objects.filter(sufijo=q[k].lower()).values()))		
		try:
			search = search[['palabra', 'numero','freq', 'sufijo', 'sufijada']]
			search.columns = ['Palabra', 'Número','Frec. léxica', 'Terminación', 'Sufijo']
			search['Frec. léxica'] = search['Frec. léxica'].astype(int)
			search.sort_values(['Sufijo', 'Frec. léxica'],ascending = [False, False], inplace = True)
			newSearch = search['Terminación'][0]
		except:	
			newSearch = ''
	
	search.drop_duplicates(inplace=True)
	empty  = search.empty			
	s_html = search.to_html(index=False)
	bajar  = q[k]
	search = plurYalomorfos.to_html(index=False)
	
	c={'request':request,
		'search':s_html,
		'search_type':k,
		'newSearch':newSearch,
		'bajar':bajar,
		'warning':warning,
		'empty':empty}

	if q['bajar'] == 'True':
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=export.csv'
		search.to_csv(path_or_buf=response)
	else:
		response = HttpResponse(t.render(c))
		
	return response
	
	
	













