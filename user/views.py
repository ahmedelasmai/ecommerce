from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.user.is_authenticated:
        return redirect('/products/')
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            user = form.save()
            messages.success(request, 'new user created')
            login(request,user)
            return redirect('/products')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html',{'form':form})

        


