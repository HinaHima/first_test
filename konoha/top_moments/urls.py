"""URl схемы для Top moments."""

from django.urls import path

from . import views

app_name = 'top_moments'
urlpatterns = [
    #Домашняя страница
    path('', views.index, name='index'),
    path('tops/', views.top, name='tops'),
    path('tops/moments/', views.moment, name='moments'),
]