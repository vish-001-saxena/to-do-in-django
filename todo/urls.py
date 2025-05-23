from django.urls import path,include
from ..core import views  # Import your views file

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('', include('core.urls')), 
]
