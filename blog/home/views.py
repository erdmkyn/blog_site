from django.shortcuts import render, reverse, HttpResponseRedirect
from post.models import Post
from django.contrib.auth.decorators import login_required
from social_django.models import AbstractUserSocialAuth
from social_django.models import UserSocialAuth
from accounts.models import UserProfile
import urllib.request, json



@login_required(login_url='/accounts/login/')
def home_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    social_auth=UserSocialAuth.objects.filter(user=request.user)
    if social_auth:
        usr = UserSocialAuth.objects.get(user=request.user)
        if usr.provider == 'facebook':
            import urllib.request, json

            with urllib.request.urlopen(
                                    "http://graph.facebook.com/v2.10/" + usr.uid + "/picture?redirect=false&fields=url") as url:
                data = json.loads(url.read().decode())
                print(data['data']['url'])
                print(usr.uid)

            user_profile.user_img_path = data['data']['url']
            user_profile.userImg = user_profile.user_img_path
            user_profile.control = True
            user_profile.save()
            print(request.user.profile.user_img_path)
    else:
        usr = None


    query = (request.GET.get('q', None))
    if query:
        url = reverse('post:index')
        url += '?q=' + query
        return HttpResponseRedirect(url)
    context = {'posts': Post.objects.all()}


    return render(request, 'home.html', context)
