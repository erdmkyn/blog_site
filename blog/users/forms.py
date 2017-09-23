from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import AuthenticationForm


class profileForm(forms.ModelForm):
    userImg=forms.ImageField(required=False)
    user_bio=forms.CharField(widget=forms.Textarea(),required=False)



    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','userImg','user_bio']

    def __init__(self, *args, **kwargs):
        super(profileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control '}





