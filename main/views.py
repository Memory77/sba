from django.shortcuts import render
from .functions import multiplicate_by_5

def home_page(request):
    weekdays = [
        'lundi',
        'mardi',
        'mercredi',
        'jeudi',
        'vendredi',
        'samedi',
        'dimanche',
    ]

    context = {
        "test" : multiplicate_by_5(5),
        "weekdays":weekdays
    }
    
    return render(request, 'main/home_page.html', context = context)


def about_page(request):
    return render(request, "main/about_page.html")

def form_page(request):
    return render(request, "main/form_page.html")