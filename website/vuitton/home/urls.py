from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("legitima", views.legitima, name="legitima"),
    path('process_token/', views.process_token, name='process_token'),
    path('invalid_token/', views.invalid_token, name='invalid_token'),
    path('report/', views.report, name='report'),
    path('thank_you/', views.thank_you, name='thank_you'),
]