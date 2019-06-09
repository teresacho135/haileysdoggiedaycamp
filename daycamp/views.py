from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Camper, Schedule, Payment
from .forms import CamperForm
from django.contrib.auth.models import User


# Create your views here.
def landing(request):
  pass
  return render(request, 'daycamp/landing.html')

@login_required
def camper_detail(request, pk):
    camper = Camper.objects.get(pk=pk)
    print(camper)
    form = CamperForm(instance=camper)
    print(form)
    return render(request, 'daycamp/camper_form.html', {'form':form, 'camper':camper})

@login_required
def camper(request):
  if request.user.is_superuser:
    campers = Camper.objects.all()
  else:
    campers = Camper.objects.filter(owner = request.user)
  return render(request, 'daycamp/camper.html', {'campers':campers})

@login_required 
def camper_create(request):
  if request.method == 'POST':
    form = CamperForm(request.POST)
    if form.is_valid():
        camper = form.save()
        camper.save()
        return redirect('camper')
    else: 
      return render(request, 'daycamp/camper.html', {'form': form, 'errors': 'Error Occurred...'})
  else:  
    form = CamperForm()
  return render(request, 'daycamp/camper_form.html', {'form':form})

@login_required
def camper_edit(request, pk): 
  camper = Camper.objects.get(pk=pk)
  print (camper)
  if request.method == 'POST':
    form = CamperForm(request.POST, instance=camper)
    if form.is_valid():
      camper = camper.save()
      return redirect('camper')
    else:
      form = CamperForm(instance=camper)
    return render(request, 'daycamp/camper_form.html', {'form':form})

@login_required
def camper_delete(request, pk):
  Camper.objects.get(id=pk).delete()
  return redirect('camper')