from django.urls import path
from . import views

urlpatterns = [
    path("sahoo/", views.hello, name = "Bubuna")
]