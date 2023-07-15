from django.urls import path
from .views import hello_world

# Create your views here.
urlpatterns = [
    path('hello/', hello_world),
]