from django.conf.urls import url
from . import views
from django.urls import path




urlpatterns = [
    path('', views.home,name='alexstore-home'),
    path('about/', views.about, name='alexstore-about'),
    #path('', include('alexstore.urls')),
]