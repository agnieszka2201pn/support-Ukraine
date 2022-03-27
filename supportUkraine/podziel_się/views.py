from django.shortcuts import render
from django import views

class MainView(views.View):
    def get(self, request):
        return render(request, 'podziel_się/mainview.html')

