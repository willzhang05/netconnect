from django.shortcuts import render
from django.http import HttpResponseForbidden, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
#from forms import UserForm, ProfileForm

@login_required
def room(request, user_one, user_two):
    username = request.user.get_username()

    # if the chat doesn't involve us, we shouldn't be able to chat
    if username != user_one and username != user_two:
        return HttpResponseForbidden()

    matches = {profile.user.username for profile in request.user.profile.matches.all()}

    # if we haven't matched, we shouldn't be able to chat
    if username == user_one and user_two not in matches:
        return HttpResponseForbidden()
    if username == user_two and user_one not in matches:
        return HttpResponseForbidden()
        
    # ensure that both orders are the same room
    if user_one < user_two:
        room_name = user_one + '-' + user_two
    else:
        room_name = user_two + '-' + user_one

    messages = Message.objects.filter(room=room_name)[0:25]
    return render(request, 'chat_room.html', {
        'room_name': room_name,
        'username': username,
        'messages': messages
    })
