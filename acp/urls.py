from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('avancee', views.avancee, name='avancee'),
    path('info', views.info, name='info'),
    path('fight', views.fight, name='fight'),
]