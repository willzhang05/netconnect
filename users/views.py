from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required


def questionnaire(request):
    return render(request, 'questionnaire.html')


def profile(request):
    return render(request, 'profile.html')


@login_required
def register(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'register.html', {'form': form})


# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.save()
