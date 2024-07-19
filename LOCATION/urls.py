from django.urls import path
from .views import track_view
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('track/', login_required(track_view), name='track')
]