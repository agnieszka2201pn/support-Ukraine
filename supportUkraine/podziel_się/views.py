from django.shortcuts import render
from django import views
from django.views.generic.list import ListView
from podziel_się.models import CurrentNeeds


class MainView(ListView):
    model = CurrentNeeds
    template_name = 'podziel_się/mainview.html'
    context_object_name = 'current_needs'

