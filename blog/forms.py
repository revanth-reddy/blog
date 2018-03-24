from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    class Meta:
        model = User
        fields = ('username', 'name', 'password1', 'password2')


class Loginform(forms.ModelForm):
	class Meta:
		model =User
		fields=('username','password')