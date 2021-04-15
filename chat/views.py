from django.shortcuts import render
from django.contrib.auth.models import User
#from forms import UserForm, ProfileForm

# Create your views here.
def chat_index(request):

    return render(request, 'chat_index.html', {})

def room(request, username):
    return render(request, 'chat_room.html', {
        'room_name': username
    })