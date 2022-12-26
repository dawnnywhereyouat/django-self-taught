from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    # DJANGO sẽ biết tự tìm trong folder templates vì đã settings trong /project/settings.py
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')