from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'please enter user name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'input your email'}))
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'please enter first name'}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'please enter last name'}))
    password1 = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'please enter password'}))
    password2 = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'please repeat your password'}))

    # __________________validation
    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('user exist')
        return user

    # __________________email
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل وجود دارد')
        return email

    # __________________password
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('password not mach')
        elif len(password2)<=8:
            raise forms.ValidationError('password is short')
        elif not any(i.isupper() for i in password2):
            raise forms.ValidationError('use capital word')
        return password2

class UserLoginForm(forms.Form):
    user=forms.CharField()
    password=forms.CharField()