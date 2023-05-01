from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
rooms = [
    {'id': 1, 'name': 'Lets learn Python'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Developers'},
]

# Create your views here.


def home(request):
    # return HttpResponse('Home Page')
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)

    context = {'room': room}
    # return HttpResponse('Room Page')
    return render(request, 'base/room.html', context)
