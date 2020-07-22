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
    frecuencia = models.CharField(max_length=10000)
    frecuencia2 = models.CharField(max_length=10000)

class Palabra(models.Model):
    palabra = models.CharField(max_length=10000)
    sufijo = models.CharField(max_length=10000)
