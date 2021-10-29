from django.db.models.base import Model
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        labels = {
            'email':'Email',

        }
    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profileImage','firstName','lastName','username', 'email', 'socialTitle1', 'socialLink1', 
        'socialTitle2', 'socialLink2', 'socialTitle3', 'socialLink3',
        'socialTitle4', 'socialLink4', 'socialTitle5', 'socialLink5']
        labels = {
            'profileImage':'Profile Image',
            'userStatus':'User Quote',
            'firstName':'First Name',
            'lastName':'Last Name',
            'socialTitle1':'Button Title - 1',
            'socialTitle2':'Button Title - 2',
            'socialTitle3':'Button Title - 3',
            'socialTitle4':'Button Title - 4',
            'socialTitle5':'Button Title - 5',
            'socialLink1':'Button Link - 1',
            'socialLink2':'Button Link - 2',
            'socialLink3':'Button Link - 3',
            'socialLink4':'Button Link - 4',
            'socialLink5':'Button Link - 5',
        }
    def __init__(self,*args,**kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
    
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})