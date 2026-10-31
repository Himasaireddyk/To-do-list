from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('add/', views.addTask, name='add'),
    path('done/<int:pk>/', views.mark_as_done, name='done'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('undone/<int:pk>/', views.mark_as_undone, name='undone'),
    path('edit/<int:pk>/', views.edit, name='edit'),
]