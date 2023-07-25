from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.


def home(request):
    recorda = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successful login")
            return redirect('home')
        else:
            messages.success(
                request, "Unsuccessful login, either username or password is incorrect")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': recorda})


def user_logout(request):
    logout(request)
    # messages.success('You have been logged out')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # AUthenticate
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have been successfully registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def record(request, pk):
    if request.user.is_authenticated:
        # Chech record
        record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'record': record})

    else:
        messages.success(
            request, "You must be logged in to view access individual records")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        # Chech record
        del_record = Record.objects.get(id=pk)
        del_record.delete()
        messages.success(request, "You have  successfully deleted the record")
        return redirect('home')
    else:
        messages.success(
            request, "You must be logged in to be able  delete a record")
        return redirect('home')


def add_new_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(
                    request, "You have  successfully added a new record")
                return redirect('home')
        return render(request, 'add_new_record.html', {'form': form})
    else:
        messages.success(
            request, "You must be logged in to be able  add a record")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        # Get record
        upd_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=upd_record)
        if form.is_valid():
            form.save()
            messages.success(
                request, "You have  successfully updated the record")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(
            request, "You must be logged in to be able  update a record")
        return redirect('home')
