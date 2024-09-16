# ac_data/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.ac_dashboard, name='ac_dashboard'),
    path('optimize-energy/', views.optimize_energy_view, name='optimize_energy'),
]
