from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('chapter/<int:chapter_num>/', views.chapter_view, name='chapter_view'),
    path('chapter/<int:chapter_num>/screen/<int:screen_num>/', views.screen_view, name='screen_view'),
    path('chapters/', views.chapter_list, name='chapter_list'),
    path('add_chapter/', views.add_chapter, name='add_chapter'),
    path('settings/', views.settings, name='settings'),
    path('about/', views.about, name='about'),
    path("credits/", views.credits, name="credits"),
    path('update_progress/', views.update_progress, name='update_progress'),
    path('hacking_mini_game/<int:game_id>/', views.hacking_mini_game_view, name='hacking_mini_game_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)