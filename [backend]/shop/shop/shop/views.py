from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("<a href='/v1/'>v1</a>")