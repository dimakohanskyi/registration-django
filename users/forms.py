from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
'class': 'username-input' }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
            'class': 'email-input'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'password1-input'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password2-input' }))



    class Meta:
        model = User
        fields = ( 'username', 'email', 'password1', 'password2')



class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'l-username-input'}))

    password = forms.CharField(label='Password' ,widget=forms.PasswordInput(attrs={
    'class':  'l-password-input' }))

    class Meta:
        model =User
        fields = ('username', 'password')






class UserProfileForm(UserChangeForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'user-name-block', 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'email-block', 'readonly': True}))


    class Meta:
        model = User
        fields = ('username', 'email')









