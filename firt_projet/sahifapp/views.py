from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home (request):
    return render(request, 'sahifapp/home.html')

def about (request):
    return render(request, 'sahifapp/about.html')

def password (request):

    characters=list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('kattaharf'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('maxsus'):
        characters.extend(list('~!@#$%^&*()_+'))

    if request.GET.get('sonlar'):
        characters.extend(list('1234567890'))


    uzunlik = int(request.GET.get('uzunlik'))


    thepassword=''

    for x in range(uzunlik):
        thepassword += random.choice(characters)

    return render(request, 'sahifapp/password.html', {'password':thepassword})
