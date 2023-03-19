from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _
from .models import upload
class signupforms(UserCreationForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm Password (again)",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
       
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':"Email",'last_name':'Last Name','first_name':"First Name"}   
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),'first_name':forms.TextInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.TextInput(attrs={'class':'form-control'})}

class loginforms(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofucus':True,'class':'form-control'}))
    password=forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':True,'class':'form-control'}))



class Postform(forms.ModelForm):
    class meta:
        model=upload
        fields=['title','desc']
        labels={'title':'Title','desc':'Description'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),'desc':forms.Textarea(attrs={'class':'form-control'})}