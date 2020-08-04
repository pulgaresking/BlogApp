from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name='Store'),
    path('about/', views.about, name='About'),
]