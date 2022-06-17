from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Register, name='register'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.home ,name='home'),
    path('addnote/', views.Addnote, name='add'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
    path('search/', views.search, name='search'),
    path('logout/', views.LogoutView, name='logout'),
]