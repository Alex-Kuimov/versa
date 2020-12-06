from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('this about text')

def home(request):
    return render(request, 'home.html', {'text': 'Hello!'})
