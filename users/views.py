from django.contrib import auth, messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm

# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('all-users')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'No user found.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('all-users')
        else:
            messages.error(request, 'Username / Password Incorrect')
    context={}
    return render(request, 'users/login-registration.html', context)

def logoutUser(request):
    logout(request)
    messages.error(request, 'User Logged Out')
    return redirect('all-users')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Account created successfully')
            login(request, user)
            return redirect('all-users')
        else:
            messages.error(request, 'Error occurred during signup. Please try again.')
    context ={'page':page, 'form':form}
    return render(request, 'users/login-registration.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(username=pk)
    context = {'profile':profile}
    return render(request, 'users/user-link.html', context)

def allUsers(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/users-list.html', context)

@login_required(login_url='login')
def updateProfile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('landing-page')
    context = {'form': form, 'profile': profile}
    return render(request, 'users/user-edit.html', context)

def userProfileMain(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'users/user-profile-main.html', context)