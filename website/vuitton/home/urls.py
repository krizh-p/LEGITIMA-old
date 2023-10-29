from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("legitima", views.legitima, name="legitima"),
    path('process_token/', views.process_token, name='process_token'),
]