from re import template
from django.shortcuts import render
from django.views.generic import ListView
from home.models import IndexCards

class CardListView(ListView):
    model = IndexCards
    template = "/index.html"
    #def get_queryset(self):
    #    return IndexCards.objects.order_by("id")