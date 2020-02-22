from django.conf.urls import url
from . import views
from django.urls import path




urlpatterns = [
    path('fir/', views.index),
    path('store/', include('alexstore')),
    path('', include('alexstore.urls')),
]