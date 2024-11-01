from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('chapter/<int:chapter_id>/', views.chapter_view, name='chapter_view'),
    path('chapters/', views.chapter_list, name='chapter_list'),
    path('add_chapter/', views.add_chapter, name='add_chapter'),
]