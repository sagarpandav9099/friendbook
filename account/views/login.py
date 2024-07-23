from django.shortcuts import render, redirect
from ..forms.login import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth


def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("/")
        
    context = {'form': form}
    return render(request, 'login/my_login.html', context=context)
