from django.http import HttpResponse
from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Learn Python'},
    {'id': 2, 'name': 'Learn Java'},
    {'id': 3, 'name': 'Learn Rust'},
]

# Create your views here.
def home(request):
    # DJANGO sẽ biết tự tìm trong folder templates vì đã settings trong /project/settings.py
    # print(request)
    context = {
        'rooms': rooms
    }
    return render(request, 'base/home.html', context)

def room(request, pk):
    # bên base/urls.py nhận pk là str nên phải chuyển thành int
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    print(room)
    return render(request, 'base/room.html', context=context)