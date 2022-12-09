from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='animes'),
    path('about', views.about, name='authors')
]
