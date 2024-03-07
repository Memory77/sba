from django.shortcuts import render
from .models import Functionalities
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from main.models import User

class FunctionalitiesListView(LoginRequiredMixin, ListView):
    model = Functionalities
    template_name = "functionalities/funct_list.html"


class FunctionalitiesDetailView(DetailView):
    model = Functionalities
    template_name = "functionalities/funct_detail.html"

class FunctionalitiesCreateView(CreateView):
    model = Functionalities
    template_name = "functionalities/funct_create.html"
    fields= "__all__"
    success_url = reverse_lazy('func_list')

class UserCreationFromCustom(UserCreationForm):
    class Meta(UserCreationForm.Meta) :
        model = User

        fields = ['username', 'password1', 'password2', 'email', 'birth_date']

class SignupView(CreateView):
    form_class = UserCreationFromCustom
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'