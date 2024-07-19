# from django.contrib import admin
from django.urls import path, include
from USERS.views import home_view
from django.views.generic import RedirectView


urlpatterns = [

    path('users/', include('USERS.urls')),
    path('location/', include('LOCATION.urls')),
    # path('', home_view, name='home'),
    path('', RedirectView.as_view(url='users/login/')),
]