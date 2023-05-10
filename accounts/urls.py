from django.urls import path, include
from . import views

# for MediaFile
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('registeruser', views.registerUser, name='registeruser'),
]