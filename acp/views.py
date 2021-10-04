from .models import information as infodb
from .models import article as articledb, userFighting
from .forms import FightForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from datetime import datetime

# Create your views here.
def home(request):

    return render(request, 'index.html')

def info(request):

    articles = list(articledb.objects.all())
    for article in articles:
        article.created_at = article.created_at.strftime('%Y-%m-%d')
        print(article)

    print(articles[0].created_at)

    return render(request, 'information_campagne.html', {'articles': articles})

def avancee(request):

    informations = list(infodb.objects.all())

    return render(request, 'avancees.html',{'infos': informations})

def fight(request):

    if request.method == 'POST':
        form = FightForm(request.POST)
        if form.is_valid():
            usr = userFighting.create(form)
            usr.save()
            messages.success(request, 'Merci pour votre soutient à bientôt')
            return render(request, 'agir.html', {'form': form})
    else:
        form = FightForm()
        return render(request, 'agir.html', {'form': form})