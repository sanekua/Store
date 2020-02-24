from django.conf.urls import url
from . import views
from django.urls import path




urlpatterns = [
    path('home/', views.about),
    path('about/', views.home, name='monday'),
    #path('', include('alexstore.urls')),
]