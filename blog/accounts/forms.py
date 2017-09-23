from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions


from django.contrib.auth.forms import AuthenticationForm


class LoginForm(forms.Form):
    # username = forms.CharField(max_length=100, label='Kullanıcı Adı',widget=forms.TextInput(attrs={'class':'form-control'}))
    # password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, label='username',
                               widget=forms.TextInput)
    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)

    def clean_user(self):

        username = self.cleaned_data['username']
        password = self.data['password']
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Kullanıcı adı veya şifreyi yanlış girdiniz!")
        return super(LoginForm, self).clean()


class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    password_confirm=forms.CharField(widget=forms.PasswordInput)




    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password','password_confirm']

    def clean_password2(self):
        password = self.cleaned_data.get('password1')
        password_confirm = self.cleaned_data.get('password2')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Parolalar eşleşmiyor!')
        return password_confirm



