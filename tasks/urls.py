from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_task),
    path('', views.get_tasks),
    path('update/<int:id>/', views.update_task),
]