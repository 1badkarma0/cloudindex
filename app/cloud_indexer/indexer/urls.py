from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_storage, name='index_storage'),
    path('search/', views.full_text_search, name='full_text_search'),
]