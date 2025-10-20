from django.urls import path

from . import views

urlpatterns = [
    path('<str:value>/', views.square_view, name='square'),
]
