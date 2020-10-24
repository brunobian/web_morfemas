#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

from django.db import models
from django.db.models import Max, Count
from django.forms import ModelForm, CharField
from django.template import RequestContext,Context, loader
import random
import json

	
class Sufijo(models.Model):
    sufijo = models.CharField(max_length=10000)
    numero = models.CharField(max_length=10000)
    frec_afijada = models.FloatField()
    frec_pseudoafijada = models.FloatField()
    count_afijada = models.FloatField()
    count_pseudoafijada = models.FloatField()
    prop_frec_afij = models.FloatField()
    prop_count_afij = models.FloatField()
    

class Palabra(models.Model):
    palabra = models.CharField(max_length=10000)
    sufijo = models.CharField(max_length=10000)
    numero = models.CharField(max_length=10000)
    sufijada = models.CharField(max_length=10000)
    freq     = models.CharField(max_length=10000)

class Text(models.Model):
    col1= models.CharField(max_length=100000)
    col2 = models.CharField(max_length=100000)
    col3 = models.CharField(max_length=100000)
    col4 = models.CharField(max_length=100000)

    def __unicode__(self):
        return(self.body)


