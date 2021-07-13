from django import urls
from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.show_index), 
    path('result/', views.show_result)
]


