from django.shortcuts import render
from .models import Post


def store(request):
    context = {
        'Title': 'Store',
        'Post': Post.objects.all(),
    }
    return render(request, 'store/store.html', context)


def about(request):
    return render(request, 'store/about.html', {'title': 'About'})
