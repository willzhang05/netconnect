from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required

@login_required
def register(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserChangeForm()
    return render(request, 'register.html', {'form': form})
