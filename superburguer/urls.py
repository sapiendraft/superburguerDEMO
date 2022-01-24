from django.contrib import admin
from django.urls import path, include
from . import views as rootview
from home import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", include("home.urls")),
    path("", v.CardListView.as_view()),
]
