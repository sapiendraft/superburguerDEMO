from django.shortcuts import render
from django.views.generic import ListView
from home.models import IndexCards

class CardListView(ListView):
    model = IndexCards