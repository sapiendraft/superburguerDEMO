from django.contrib import admin
from django.urls import path, include
from . import views as rootview

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", include("home.urls")),
    path("", rootview.HomePage.as_view(), name = "home")
]
