from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'index.html')

def info(request):

    return render(request, 'information_campagne.html')

def avancee(request):

    return render(request, 'avancees.html')

def fight(request):

    return render(request, 'agir.html')