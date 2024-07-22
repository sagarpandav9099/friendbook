from django.shortcuts import render, redirect
from ..forms.registretion import CreateUserForm

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            return redirect('/')
        
    context = {'form': form}

    return render(request, 'registration/register.html', context=context)
