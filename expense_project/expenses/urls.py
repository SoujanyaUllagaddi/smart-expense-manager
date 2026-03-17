from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('delete/<int:id>/', views.delete_expense, name='delete'),
    path('signup/', views.signup, name='signup'),
    path('edit/<int:id>/', views.edit_expense, name='edit'),
]