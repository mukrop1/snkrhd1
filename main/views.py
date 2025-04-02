from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "SNKRHDS - Главная"
        context["content"] = "SNKRHDS"
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "SNKRHDS - О нас"
        context["content"] = "SNKRHDS"
        context["text_on_page"] = "туттутутутутуту"
        return context
