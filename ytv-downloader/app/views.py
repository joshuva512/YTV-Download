from django.shortcuts import render
from pytube import YouTube
import os.path
from django.contrib import messages


def home(request):
    try:
        savevdo = os.path.expanduser("~")
        if request.method =="POST":
            url=request.POST.get('videourl')
            YouTube(url).streams.first().download(savevdo + '/Downloads')
            messages.success(request, " |  " + YouTube(url).title + "  |<<== Downloaded 👍👍👍")
    except:
        messages.success(request, " |  " + url.title + "  |<<== Unable to download 😐😐😐")
    return render(request, 'home.html')