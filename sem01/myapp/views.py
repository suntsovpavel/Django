from django.shortcuts import render
from django.http import HttpResponse
import random
import logging

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse('Hello World!')

def about(request):
    return HttpResponse('About us')

def coin(request):
    return HttpResponse(random.choice(['Орел', 'Решка']))

def cube(request):
    return HttpResponse(random.randint(1,6))

def number(request):
    return HttpResponse(random.randint(0,100))