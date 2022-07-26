from django.urls import path
from .views import *

urlpatterns=[
    path('', Index_view.as_view(), name='index'),
    path('edit/<str:pk>', edit, name='edit'),
    path('delete/<str:pk>', delete, name='delete'),
    path('add', add, name='add'),
    ]