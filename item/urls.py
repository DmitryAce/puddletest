from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('<str:clean>', views.itemsC, name='itemsC'),
    path('new/', views.new, name='new'),
    path('category/<int:pk>/', views.category, name='category'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:creator>/<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]
