from django.urls import path

from . import views

app_name = "clima"

urlpatterns = [
    path("", views.inicio, name="inicio"),
]