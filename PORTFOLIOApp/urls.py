from django.urls import path
from .views import index, contactme

urlpatterns = [
    path('', index, name='index'),
    path('contactme/', contactme, name='contactme'),
]
