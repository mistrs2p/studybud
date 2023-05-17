from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm


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

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        print(RoomForm(request.POST))
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    #     print(RoomForm(request.POST))
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    #     print(RoomForm(request.POST))
    context = {'form': form}
    return render(request, 'base/delete.html', {'obj': room})