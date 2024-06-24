from django.urls import path
from .views import *

urlpatterns = [
    path('ev/', eview),
    path('hv/', hview),
    path('sv/', sview)
]