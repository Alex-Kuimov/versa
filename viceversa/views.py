from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('this about text')

def home(request):
    return render(request, 'home.html', {'text': 'Hello!'})

def reverse(request):
    user_text = request.GET['usertext']
    words = user_text.split()
    number_of_word = len(words)
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text, 'numberofword': number_of_word})