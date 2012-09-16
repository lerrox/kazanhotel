#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render_to_response


def index(request):
    
    myContext = Context({'l':"python"})
    return render_to_response('find.html', myContext)