from django.urls import path
from .views import *

urlpatterns = [
    path('cv/', cview),
    path('hv/', hview),
    path('sv/', sview),
    path('uv/<int:pk>', updateview),
    path('dv/<int:x>', deleteview)
]