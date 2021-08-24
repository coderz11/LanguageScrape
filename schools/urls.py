from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('list/', views.list, name='list'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),    
]