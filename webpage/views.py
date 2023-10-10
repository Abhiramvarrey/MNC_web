from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return  render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def register_user(request):
    if request.method=='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Hello {username}, your account has been created please login")
            return redirect(login)
        else:
            form = NewUserForm()
    form = NewUserForm()
    return render(request,'register.html',{'register_form':form})

@login_required
def profile(request):
    return render(request, 'profile.html')