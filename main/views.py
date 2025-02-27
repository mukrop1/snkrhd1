from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):


    context = {
        "title": "SNKRHDS - Главная",
        "content": "SNKRHDS",
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "SNKRHDS - О нас",
        "content": "SNKRHDS",
        "text_on_page": "туттутутутутуту",
    }
    return render(request, "main/about.html", context)
