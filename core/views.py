from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    return render(request, 'login.html')


def questionnaire(request):
    return render(request, 'questionnaire.html')


def profile(request):
    return render(request, 'profile.html')


# @login_required
# def home(request):
#  return render(request, 'index.html')


# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.save()
