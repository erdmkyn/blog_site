from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect,HttpResponse,get_object_or_404,render_to_response, Http404
from social_django.models import UserSocialAuth
from django.contrib.auth.models import  User
from django.shortcuts import get_object_or_404,reverse
from .forms import profileForm


def user_screen(request,username):
    print('dfd')
    print('fdfdfdfd')

    user = get_object_or_404(User, username=username)
    form = profileForm(data=request.POST or None, files=request.FILES or None, instance=request.user, initial={'userImg':user.profile.userImg,'user_bio':user.profile.user_bio})
    if request.user != user:
        return render(request, '404.html', {'form': form})

    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.profile.user_bio = form.cleaned_data['user_bio']

            try:
                user_img = request.FILES['userImg']
                user.profile.userImg = user_img
            except:
                user_img = None
            user.profile.save()
            user.save()


    return render(request, 'users/user_screen.html', {'form': form})


def edit_profile(request,username):
    user = get_object_or_404(User, username=request.user.username)
    form = profileForm(request.POST or None,request.FILES or None,instance=request.user,initial={'user_bio':user.profile.user_bio,'userImg':user.profile.userImg})
    if request.user != user :
        return render(request, '404.html', {'form': form})

    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            user.profile.user_bio = form.cleaned_data['user_bio']
            print(user.profile.user_bio)
            try:
                user_img = request.FILES['userImg']
                print(user_img)
                user.profile.userImg = user_img
                print(user.profile.userImg)
            except:
                user_img = None
            user.profile.save()
            user.save()
            print(user)
            print(user.profile)

    return render(request,'users/user_updates.html',context={'form':form})











