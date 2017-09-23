from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from social_django.models import UserSocialAuth


# Create your views here.


def login_view(request):




    form = LoginForm(request.POST or None)
    print(request.GET)

    if request.method == 'POST':
        if form.is_valid():

            deneme = request.GET.get('next', '/')
            print(deneme)

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            print(type(request.user))

            if request.user.is_authenticated():
                print(user)


                print(deneme)

                print('selam')
                return HttpResponseRedirect(deneme)


        else:
            print(form.is_valid())

    return render(request, "accounts/form.html", {"form": form, 'title': 'Giriş Yap'})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data['password_confirm']
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        print(new_user)
        login(request, new_user)
        return redirect('home')

    return render(request, 'accounts/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')



