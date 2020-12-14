from django.shortcuts import render
from django import template
from django.http import HttpResponse



def home(request):
 return render(request, 'templates/static-handler.html')

def hello(request):
 return HttpResponse(u'Привет, мир!')
# Create your views here.
