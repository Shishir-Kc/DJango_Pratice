from django.shortcuts import render
from django.http import HttpResponse

def Profile(request):
    return HttpResponse('Profile Page')
