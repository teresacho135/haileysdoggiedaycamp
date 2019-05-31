from django.shortcuts import render
# IMPORT DJANGO AUTH
from django.contrib import auth
# IMPORT
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

def register(request):
  if request.method == 'POST':
    #GET form values
    name = request.POST['name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    #password validation
    if password == password2:
      #Check username exists
      if User.objects.filter(username=username).exists():
        return render(request, 'accounts/register.html', {'error': 'Username has already been registered. Please try a different username'})
      else:
        #Check if email exists
        if User.objects.filter(email=email).exists():
          return render(request, 'accounts/register.html', {'error': 'Email has already been registered'})

        else: 
          #Register User
          user = User.objects.create_user(
            username=username, password=password, email=email, name=name)
          user.save()
          return redirect('login')
    else:
      return render(request, 'accounts/register.html', {'error': 'Passwords do not match'})
  else:
    return render(request, 'accounts/register/html')

def login(request):
    if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']

      user = auth.authenticate(username=username, password=password)

      if user is not None:
        auth.login(request, user)
        return redirect('campers_list')
      else:
        return render(request, 'accounts/login.html', {'error': 'Invalid Credentials...'})

    else:
        return render(request, 'accounts/login.html')
