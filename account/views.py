from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# messages.debug, messages.info, messages.success, messages.warning, messages.error

@login_required
def profileView(request):
    return render(request, 'account/profile.html')

def home(request):
    return render(request, 'account/home.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congratulations {username}, your account was successfully created, \nYou are now able to login')
            return redirect('login')
        # else:
        #     messages.warning(request, f'An error has occourred')
    else:
        form = UserRegisterForm()

    context = {
        'form':form,
        }
    return render(request, 'account/register.html', context)


def aboutView(request):
    return render(request, 'account/about.html')