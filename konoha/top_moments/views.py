from django.shortcuts import render
from .models import Top, TheTop

def index(request):
    """Домашняя страница всего проекта."""
    return render(request, 'top_moments/index.html')

def top(request):
    """Страница с топами."""
