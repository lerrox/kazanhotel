#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from hotel.models import  Hotel


def index(request):
    hotels = Hotel.objects.all()
    myContext = Context({'hotels':hotels})
    return render_to_response('find.html', myContext)