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
    content = top.thetop_set.all()
    context = {'top': top, 'content': content}
    return render(request, 'top_moments/moments.html', context)

def kunoichi(request):
    """Страница с лучшими куноичи."""
    top = Top.objects.get(id=2)
    content =  top.thetop_set.all()
    context = {'top': top, 'content' : content}
    return render(request, 'top_moments/kunoichi.html', context)