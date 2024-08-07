from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse


# Create your views here.
def chat(request):
    room_list = Room.objects.all()
    context = {'rooms': room_list}
    if request.method == 'POST':
        room_name = request.POST['room_name']
        username = request.POST['username']

        print(f"Room Name: {room_name}, Username: {username}")

        if Room.objects.filter(name=room_name).exists():
            return redirect(f'/chat/{room_name}/?username={username}')
        else:
            new_room = Room.objects.create(name=room_name)
            new_room.save()
            return redirect(f'/chat/{room_name}/?username={username}')
    else:
        return render(request, 'chat.html', context)


def room(request, room):
    room_list = Room.objects.all().values('name')
    username = request.GET.get('username')
    room_detail = Room.objects.get(name=room)
    context = {
        'room': room,
        'username': username,
        'room_detail': room_detail,
        'room_list': room_list
    }
    return render(request, 'room.html', context)


def send(request):
    if request.method == 'POST':
        message = request.POST['message']
        username = request.POST['username']
        room_id = request.POST['room_id']
        new_message = Message.objects.create(value=message, user=username, room=room_id)
        new_message.save()
        return HttpResponse('Message sent successfully')
    return HttpResponse('Invalid request method', status=400)


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id).values()
    return JsonResponse({"message": list(messages)})

def get_details(request, room):
    room = Room.objects.get(name=room)
    users = Message.objects.filter(room=room).values_list('user', flat=True).distinct()
    room_list = Room.objects.all().values('name')
    return JsonResponse({"users": list(users), "rooms": list(room_list)})
