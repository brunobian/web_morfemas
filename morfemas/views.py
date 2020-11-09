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
	
	plurYalom = pd.read_csv("/var/www/html/web_morfemas/data/pluralesYalomorfos.csv")

	t = loader.get_template('search.html')
	
	q = request.GET
	keys=[i for i in q.dict().keys()]
	k = keys[0]
	
	warning = False
	empty   = False
	if k == 'sufijo':
		sing    = plurYalom.loc[plurYalom['singular'] == q[k]]
		v_sing1 = plurYalom.loc[plurYalom['var_sing1'] == q[k]]
		v_sing2 = plurYalom.loc[plurYalom['var_sing2'] == q[k]]
		v_sing3 = plurYalom.loc[plurYalom['var_sing3'] == q[k]]
		v_sing4 = plurYalom.loc[plurYalom['var_sing4'] == q[k]]
		
		plur = plurYalom.loc[plurYalom['plural'] == q[k]]
		v_plur1 = plurYalom.loc[plurYalom['var_plur1'] == q[k]]
		v_plur2 = plurYalom.loc[plurYalom['var_plur2'] == q[k]]
		v_plur3 = plurYalom.loc[plurYalom['var_plur3'] == q[k]]
		v_plur4 = plurYalom.loc[plurYalom['var_plur4'] == q[k]]
		
		tmp = pd.concat([sing, v_sing1, v_sing2, v_sing3, v_sing4, 
						 plur, v_plur1, v_plur2, v_plur3, v_plur4])
		
		search = pd.DataFrame(list(Sufijo.objects.filter(sufijo=tmp['singular'].iloc[0]).values()))		
		try:
			search = search[['sufijo', 'numero', 'frec_afijada', 'frec_pseudoafijada', 'prop_frec_afij', 'count_afijada', 'count_pseudoafijada',  'prop_count_afij', ]]
			search.columns = ['Sufijo', 'Número', 'Frec. Token Afijadas', 'Frec. Token Pseudoafijadas', 'Prop. Token Afijadas', 'Frec. Type Afijadas', 'Frec. Type Pseudoafijadas', 'Prop. Type Afijadas']
			newSearch = q[k]
			if tmp["var_sing1"].notna().values[0]:
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
	
	
	empty  = search.empty			
	s_html = search.to_html(index=False)
	tmp.drop_duplicates(inplace=True)
	# ~ s_html = tmp.to_html(index=False)

	bajar  = q[k]
	
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
	
	
	













