from django.urls import path
from . import views  # Import your views file

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
