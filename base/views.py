from django.http import HttpResponse
from django.shortcuts import render
from .models import Room

# Create your views here.
def home(request):
    # DJANGO sẽ biết tự tìm trong folder templates vì đã settings trong /project/settings.py
    rooms = Room.objects.all()
    print(rooms)
    context = {
        'rooms': rooms
    }
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    print(room)
    return render(request, 'base/room.html', context=context)