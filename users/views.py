from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.contrib import messages
from django.db import transaction
from .forms import UserForm, ProfileForm, RegisterForm
from django.contrib.auth.models import User


def questionnaire(request):
    return render(request, 'questionnaire.html')


@login_required
def profile(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def view_other(request, person_name):
    user1 = User.objects.get(username = person_name)
    user_form = UserForm(instance=user1)
    profile_form = ProfileForm(instance=user1.profile)
    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
@transaction.atomic
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES,
                            instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = RegisterForm(instance=request.user.profile)
    return render(request, 'register.html', {'form': form})


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile successfully updated.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})
