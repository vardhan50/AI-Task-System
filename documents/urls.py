from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_document),
    path('', views.get_documents),
    path('<int:id>/', views.get_document),
    path('search/', views.search_documents),
]