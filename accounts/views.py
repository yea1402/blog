from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user( username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('blog')
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')
