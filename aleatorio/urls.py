from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index_aleatorio),
    path('vaciar/', views.vaciar),
]