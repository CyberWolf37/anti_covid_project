from .models import information as infodb
from .models import article as articledb
from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'index.html')

def info(request):

    articles = list(articledb.objects.all())
    print(articles[0].created_at)

    return render(request, 'information_campagne.html', {'articles': articles})

def avancee(request):

    informations = list(infodb.objects.all())

    return render(request, 'avancees.html',{'infos': informations})

def fight(request):

    return render(request, 'agir.html')