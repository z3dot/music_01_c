from django.urls import path
from . import views

urlpatterns = [
    path('hi/', views.main, name='indexh'),
    path('<str:name>/', views.r_n, name='index_n')
]