from django.urls import path
from . import views

urlpatterns = [
    path('front/', views.front, name='front'),
    path('list/', views.list, name='list'),
    path('index/', views.index, name='index'),    
    path('detail/<int:pk>', views.detail, name='detail'),
    path('detail2/<int:pk>', views.detail2, name='detail2'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),    
    path('scrape/', views.scrape, name='scrape'), 
]