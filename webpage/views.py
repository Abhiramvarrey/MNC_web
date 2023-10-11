from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import pyrebase
 
config={
  'apiKey': "AIzaSyBH_pjeB9O6IngS9L1LdXUaj_h17LoIvk4",
  'authDomain': "website-b995d.firebaseapp.com",
  'projectId': "website-b995d",
  'storageBucket': "website-b995d.appspot.com",
  'messagingSenderId': "377928329737",
  'appId': "1:377928329737:web:51a5cca996b905517526d8",
  'measurementId': "G-S60Q1YJQ3Z"
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
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