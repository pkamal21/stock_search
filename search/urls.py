from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.result, name='result'),
    path('', views.query_new, name='query_new'),
]

