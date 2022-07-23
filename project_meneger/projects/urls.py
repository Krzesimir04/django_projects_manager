from django.urls import path
from .views import *

urlpatterns=[
    path('', Index_view.as_view(), name='index'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete'),
    path('add', add, name='add'),
    ]