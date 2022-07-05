from django.shortcuts import render
from .models import Top, TheTop

def index(request):
    """Домашняя страница всего проекта."""
    return render(request, 'top_moments/index.html')

def top(request):
    """Страница с топами."""
    tops = Top.objects.all()
    context = {'tops' : tops}
    return render(request, 'top_moments/tops.html', context)

def moment(request):
    """Страница с лучшими моментами."""
    top = Top.objects.get(id=1)
    moments = top.thetop_set.all()
    context = {'top': top, 'moments': moments}
    return render(request, 'top_moments/moments.html', context)