from django.conf.urls import url
from . import views
from django.urls import path




urlpatterns = [
    path('home/', views.home),
    path('about/', views.about, name='monday'),
    #path('', include('alexstore.urls')),
]