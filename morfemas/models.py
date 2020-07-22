#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

from django.db import models
from django.db.models import Max, Count
from django.forms import ModelForm, CharField
from django.template import RequestContext,Context, loader
import random
import json

# Create your models here.
class Sufijo(models.Model):
	email = models.EmailField()
	age = models.IntegerField(blank=False, null=False)
	gender = models.CharField(max_length=3, blank=False, null=False)
	original_ip = models.GenericIPAddressField()
	sequence_number = models.IntegerField(null=True)
	experiment_sequence = models.CharField(max_length=2550)
	

	def __unicode__(self):
		return (self.email)
			
	@staticmethod
	def generate_sequence():
		# Originalmente se buscaba la cantidad total de combinaciones de listas y se dividía entre los sujetos
		# ts_num = (Subject.objects.count() % TrialSequence.objects.count() ) 
		
		# (10/07/2015) Para este experimento a todos los sujetos les doy todas las oraciones 
		ts_num = 0
		ts = TrialSequence.objects.all().order_by('id')[ts_num]
		seq_base1 = json.loads(ts.seq)
		
		# (09/07/2020)
		# Pero tengo que darlas en orden aleatorio. 
		# Primero las 105 del experimento de Lena 
		# Despues el resto del experimento de proverbios		
		Lena  = seq_base1[:105] # Las 105 primeras oraciones son de Lena
		Bruno = seq_base1[105:] # Las siguientes oraciones son de Bruno
		random.shuffle(Lena) 
		random.shuffle(Bruno)
		seq_base0 = Lena + Bruno

		# (12/07/2020)
		# Como las oraciones de Lena ya tiene bastantes datos, mezclo todas		
		random.shuffle(seq_base0)
		
		
		return (ts.id,seq_base0)       

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['email','age','gender','original_ip']
	
class Information(models.Model):
    subject = models.OneToOneField(Subject, primary_key=True, on_delete=models.CASCADE)
    native_language = models.CharField(max_length=200, choices=LANGUAGE, blank=False, null=False)
    reading_language = models.CharField(max_length=200, choices=LANGUAGE, blank=False, null=False)
    work_reading_language = models.CharField(max_length=200, choices=LANGUAGE, blank=False, null=True)
    country = models.CharField(max_length=200, choices=COUNTRIES, blank=False, null=False)
    schooling = models.CharField(max_length=200, choices=SCHOOLING, blank=False, null=False)
    books = models.CharField(max_length=200, choices=QUANTITY, blank=False, null=False)
    work_reading = models.CharField(max_length=200, choices=YES_NO, blank=False, null=False)
    computer_reading=models.CharField(max_length=200, choices=YES_NO, blank=False, null=False)
    dexterity=models.CharField(max_length=200, choices=DEXTERITY, blank=False, null=False)
    source=models.CharField(max_length=200, choices=SOURCE, blank=False, null=False)
    other_experiments=models.CharField(max_length=200, choices=YES_NO, blank=False, null=False)



class InfoForm(ModelForm):
    class Meta:
        model = Information
        fields = ['subject','native_language','country', 'schooling','books','reading_language','work_reading','work_reading_language','computer_reading','dexterity','source', 'other_experiments']

class TrialSequence(models.Model):
    seq = models.CharField(max_length=10000)

class Text(models.Model):
    textNumber = models.IntegerField()
    textClass = models.IntegerField()
    body = models.CharField(max_length=100000)

    def __unicode__(self):
        return(self.body)


class TrialOption(models.Model):
    text = models.ForeignKey(Text,on_delete=models.CASCADE)
    missing_words = models.CharField(max_length=10000) # JSON encoded list of integers.

class Trial(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    trialOpt = models.ForeignKey(TrialOption,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    initial_time = models.DateTimeField()
    words = models.CharField(max_length=10000) # JSON-encoded list of words.
    

