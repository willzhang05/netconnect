from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.contrib import messages
from django.db import transaction
from .forms import UserForm, ProfileForm, RegisterForm
from django.contrib.auth.models import User


def get_profile_values(profile_form):
    profile_values = []
    for field in profile_form.fields:
        field_name = str(field)
        attr = 'get_{}_display'.format(field_name)
        if hasattr(profile_form.instance, attr):
            temp = getattr(profile_form.instance, attr)
            result = temp()
            profile_values.append((profile_form[field_name].label, result))
        else:
            profile_values.append(
                (profile_form[field_name].label, str(profile_form[field_name].value())))
    return profile_values


@login_required
def profile(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    profile_values = get_profile_values(profile_form)
    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form, 'profile_values': profile_values})


@login_required
def view_other_profile(request, username):
    user = User.objects.get(username=username)
    user_form = UserForm(instance=user)
    profile_form = ProfileForm(instance=user.profile)
    is_other = request.user != user
    profile_values = get_profile_values(profile_form)
    return render(request, 'profile.html', {'is_other': is_other, 'user_form': user_form, 'profile_form': profile_form, 'profile_values': profile_values})


@login_required
@transaction.atomic
def register(request):
    instance = request.user.profile

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES,
                            instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered.')
            instance.completed_registration = True
            instance.match_enabled = True
            instance.save()
            if instance.search_lat == None or instance.search_lng == None:
                return redirect('map')
            else:
                return redirect('matches')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = RegisterForm(instance=instance)
    return render(request, 'register.html', {'form': form})


@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
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
    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})
