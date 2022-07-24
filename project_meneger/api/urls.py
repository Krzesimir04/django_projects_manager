from django.urls import path
from .views import *

urlpatterns=[
    path('get_data',get_data),
    path('post_data/<int:pk>',post_data),
    path('put_data',put_data),
    path('delete_data/<int:pk>',delete_data),
]