from django.shortcuts import render

from .models import *
def register(request):
    pass

def home(request):
    popular_categories = Category.objects.filter(is_popular=True)[:3]
    bestsellers = Product.objects.filter(is_bestseller=True, available=True)[:8]
    slider_images = [
        {'title': 'Акция недели', 'subtitle': 'Скидка до 30%', 'url': '/'},
        {'title': 'Акция недели', 'subtitle': 'Скидка до 30%', 'url': '/'},
        {'title': 'Акция недели', 'subtitle': 'Скидка до 30%', 'url': '/'}
    ]
    return render(request, 'index.html', {
        'popular_categories': popular_categories,
        'bestsellers': bestsellers,
        'slider_images': slider_images
    })

