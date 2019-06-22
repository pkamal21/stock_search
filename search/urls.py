from django.urls import path
from . import views

urlpatterns = [
    path('', views.query, name='query'),
    path('results/', views.result, name='result'),
    path('query/new/', views.query_new, name='query_new'),

]

