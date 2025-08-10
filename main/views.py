from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories

class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - главная'
        context['content'] = 'Магазин мебели HOME'
        return context

class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - О нас'
        context['content'] = 'О нас'
        context['text_on_page'] = 'Бля магазин пизда классный, ахуеть можно от этого'
        return context

# def index(request):
#     context =  {'title': 'Home - главная', 'content': 'Магазин мебели HOME', } 
#     return render(request, "main/index.html", context)


# def about(request):
#     context =  {'title': 'Home - О нас', 'content': 'О нас', 'text_on_page': 'Бля магазин пизда классный, ахуеть можно от этого'}
#     return render(request, "main/about.html", context)