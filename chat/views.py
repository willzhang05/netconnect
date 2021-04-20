from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Message
#from forms import UserForm, ProfileForm


# Create your views here.
def index(request):
    #username = request.user.get_username()
    return render(request, 'chat_index.html', {
     #   'username': username,
    })

def room(request, room_name):
    username = request.user.get_username()
    messages = Message.objects.filter(room=room_name)[0:25]
    return render(request, 'chat_room.html', {
        'room_name': room_name,
        'username': username,
        'messages': messages
    })
