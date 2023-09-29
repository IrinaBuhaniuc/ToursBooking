from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from typing import Optional
from django.urls import reverse

from apps.user.forms import UserForm
from .models import User
# Create your views here.



def add_user(request):
    submitted = False
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-user')
    else:
        form = UserForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'user/signup.html', {'form' : form, 'submitted': submitted})


def login_view(request):
    error_message = None
    # Unbound state of our form
    form = AuthenticationForm()
    
    if request.method == "POST":
        # Bound state of our form
        form = AuthenticationForm(data=request.POST)
        
        # Validate the data
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticate the user
            user: Optional[User]= authenticate(
                username=username, 
                password=password,
                )
            # Check if User wa authenticated
            
            if user is not None:
                # use the session to keep the authenticated user's id.
                login(request,user)
                
                # Redirect user to his profile page
                # The url path name
                return redirect('profile')
                
            # TODO:If user ud not authenticated, what should you do?
            
        else:
            # User's data is not valid. So, set an error message to be displayed
            error_message = 'Sorry, something went wrong. Try again.'
            
    context = {'form': form, 'error_message': error_message}
        
    return render(request, 'user/login.html', context)
    
    
    
def profile(request):
    return render(request, "user/profile.html")