from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include
from django.urls import re_path

from . import views
# from views import index

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('run_gedit/', views.GeditView.as_view(), name='run_gedit'),
    path('run_spotify/', views.SpotifyView.as_view(), name='run_spotify'),
    path('run_vk/', views.VkView.as_view(), name='run_vk'),
    path('run_tg/', views.VkView.as_view(), name='run_tg'),
    path('run_yandex/', views.YandexView.as_view(), name='run_yandex'),
    path('run_youtube/', views.YouTubeView.as_view(), name='run_youtube'),
    path('run_inst/', views.InstView.as_view(), name='run_inst'),
    path('run_camera/', views.CameraView.as_view(), name='run_camera'),
    path('run_calendar/', views.CalendarView.as_view(), name='run_calendar'),
    path('run_discord/', views.DiscordView.as_view(), name='run_discord'),
    path('run_lightup_full/', views.LightFullView.as_view(), name='run_lightup_full'),
    path('run_lightup_low/', views.LightLowView.as_view(), name='run_lightup_low'),
    path('run_lightup_plus/', views.LightPlusView.as_view(), name='run_lightup_plus'),
    path('run_lightup_minus/', views.LightMinusView.as_view(), name='run_lightup_minus'),
    path('run_tab/', views.TabView.as_view(), name='run_tab'),
    path('run_screenshot/', views.ScreenshotView.as_view(), name='run_screenshot'),
    path('run_space/', views.SpaceView.as_view(), name='run_space'),
    path('run_enter/', views.EnterView.as_view(), name='run_enter'),
]