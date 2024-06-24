from django.urls import path
from .views import *

urlpatterns = [
    path('uv/', uview),
    path('hv/', hview),
    path('sv/', sview)
]