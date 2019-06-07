from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing(request):
  pass
  return render(request, 'daycamp/landing.html')

@login_required 
def camper(request):
  pass
  return render(request, 'daycamp/camper.html')
