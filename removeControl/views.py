import webbrowser
from subprocess import call, run

import pyautogui
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic, View
import requests
from django.shortcuts import redirect
import os
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import RedirectView


# Create your views here.
class HomeView(View):
    @staticmethod
    def get(request):
        return render(request, 'removeControl/index.html')


class GeditView(View):
    @csrf_exempt
    def post(self, request):
        os.system("gedit")
        return HttpResponse(status=204)


class SpotifyView(View):
    @csrf_exempt
    def post(self, request):
        os.system("spotify")
        return HttpResponse(status=204)


class VkView(View):
    @csrf_exempt
    def post(self, request):
        webbrowser.open("https://www.vk.com")
        return HttpResponse(status=204)


class TgView(View):
    @csrf_exempt
    def post(self, request):
        webbrowser.open("https://web.telegram.org/a/")
        return HttpResponse(status=204)


class YandexView(View):
    @csrf_exempt
    def post(self, request):
        webbrowser.open("https://yandex.by/")
        return HttpResponse(status=204)


class YouTubeView(View):
    @csrf_exempt
    def post(self, request):
        webbrowser.open("https://www.youtube.com/")
        return HttpResponse(status=204)


class InstView(View):
    @csrf_exempt
    def post(self, request):
        webbrowser.open("https://www.instagram.com/")
        return HttpResponse(status=204)


class CameraView(View):
    @csrf_exempt
    def post(self, request):
        os.system('cheese')
        return HttpResponse(status=204)


class CalendarView(View):
    @csrf_exempt
    def post(self, request):
        os.system("gnome-calendar")
        return HttpResponse(status=204)


class DiscordView(View):
    @csrf_exempt
    def post(self, request):
        os.system("discord")
        return HttpResponse(status=204)


class LightFullView(View):
    @csrf_exempt
    def post(self, request):
        call(["amixer", "-D", "pulse", "sset", "Master", "100%"])
        return HttpResponse(status=204)


class LightLowView(View):
    @csrf_exempt
    def post(self, request):
        call(["amixer", "-D", "pulse", "sset", "Master", "toggle"])
        return HttpResponse(status=204)


class LightPlusView(View):
    @csrf_exempt
    def post(self, request):
        call(["amixer", "-D", "pulse", "sset", "Master", "10%+"])
        return HttpResponse(status=204)


class LightMinusView(View):
    @csrf_exempt
    def post(self, request):
        call(["amixer", "-D", "pulse", "sset", "Master", "10%-"])
        return HttpResponse(status=204)


class TabView(View):
    @csrf_exempt
    def post(self, request):
        pyautogui.hotkey('tab')
        return HttpResponse(status=204)


class ScreenshotView(View):
    @csrf_exempt
    def post(self, request):
        pyautogui.screenshot()
        return HttpResponse(status=204)


class SpaceView(View):
    @csrf_exempt
    def post(self, request):
        pyautogui.hotkey('space')
        return HttpResponse(status=204)


class EnterView(View):
    @csrf_exempt
    def post(self, request):
        pyautogui.hotkey('enter')
        return HttpResponse(status=204)
