from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),          # Homepage: index.html
    path('about/', views.about, name='about'),  # About page: about.html
]
