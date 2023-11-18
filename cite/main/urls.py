from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('school', views.school),
    path('school_cite', views.school_cite),
    path('school_game', views.school_game),
    path('school_2', views.school_2),
    path('school_3', views.school_3),
    path('school_google', views.school_google),
    path('school_inshe', views.school_inshe),
    path('school_cite_2', views.school_cite_2),
    path('school_inshe_2', views.school_inshe_2),
    path('school_game_2', views.school_game_2),
    path('school_game_2', views.school_game_2),
    path('school_all', views.school_all),
    path('school_all_2', views.school_all_2),
]