from django.urls import path
from home import views

urlpatterns = [
    path("", views.CardListView.as_view(), name = "card_list"),
    ]