from django.urls import path

from . import views

app_name = 'vocab'
urlpatterns = [
    path('', views.homePage, name='homepage'),
    path('main', views.index, name='index'),
    path('<int:vocab_id>/', views.detail , name='detail'),
    path('addPage/', views.addWordPage , name='addPage'),
    path('add/', views.addWord , name='add'),
]