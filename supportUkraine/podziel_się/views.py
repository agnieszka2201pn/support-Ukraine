from django.shortcuts import render
from django import views
from django.views.generic.list import ListView
from podziel_się.models import CurrentNeeds
from django.views import View
from podziel_się.forms import UserForm
from django.contrib.auth.models import User


class MainView(ListView):
    model = CurrentNeeds
    template_name = 'podziel_się/mainview.html'
    context_object_name = 'current_needs'

class RegisterView(View):

    def get(self, request):
        if request.method == 'GET':
            register_form = UserForm
            return render(request, 'podziel_się/register.html', {'form': register_form})

    def post(self, request):
        if request.method == "POST" and 'register' in request.POST:
            form = UserForm(request.POST)
            if form.is_valid():
                new_user = User.objects.create_user(username=form.cleaned_data['username'])

                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                message = f"User added successfully"
                return render(request, 'podziel_się/register.html', {'form':form, 'message': message, })
            else:
                message = f"Incorrect data!"
                return render(request, 'podziel_się/register.html', {'form':form, 'message': message, })

