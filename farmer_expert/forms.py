from django import forms
from . models import FarmerQuery,ExpertReply
from django.contrib.auth.forms import UserCreationForm
from .models import User


class FarmerQueryForm(forms.ModelForm):
    class Meta:
        model = FarmerQuery
        fields = ['first_name', 'last_name', 'email', 'title_of_query','description_of_query']


class ExpertFeedbackForm(forms.ModelForm):
    class Meta:
        model = ExpertReply
        fields = ['first_name', 'last_name','email', 'expert_reply']





class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_farmer', 'is_expert')
