
from django.shortcuts import render, redirect, get_object_or_404
from .models import Registration
from .forms import RegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_registrations')
    else:
        form = RegistrationForm()
    return render(request, 'registerapp/register.html', {'form': form})

def list_registrations(request):
    registrations = Registration.objects.all()
    return render(request, 'registerapp/list.html', {'registrations': registrations})

def update_registration(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('list_registrations')
    else:
        form = RegistrationForm(instance=registration)
    return render(request, 'registerapp/register.html', {'form': form})

def delete_registration(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        registration.delete()
        return redirect('list_registrations')
    return render(request, 'registerapp/confirm_delete.html', {'registration': registration})

def practice(request):
    return render(request, 'registerapp/practice.html')