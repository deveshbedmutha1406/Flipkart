from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Notes
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def search(request):
    if request.method == 'POST':
        var = request.POST.get('search')
        a = Notes.objects.all().filter(tag__icontains=var, userid=User.objects.get(id=request.user.id))
        print(a)
        if len(a) == 0:
            return render(request, 'notesapp/result.html', {"result" : "Not Found"})
        return render(request, 'notesapp/result.html', context={"data":a})
    return render(request, 'notesapp/result.html', context={"data":"a"})

@login_required(login_url='login')
def update(request, pk):
    if request.method == 'POST':
        note = request.POST["addtxt"]   
        tag = request.POST["addtag"]
        heading = request.POST["addtitle"]
        obj = Notes.objects.get(id=pk)
        obj.body=note
        obj.tag=tag
        obj.heading=heading
        obj.save()
        return redirect('home')
    else:
        obj = Notes.objects.get(id=pk)
        a = obj.body
        b = obj.heading
        c = obj.tag
        return render(request, 'notesapp/update.html', {"id" : pk, "body" : a, "heading" : b, "tag" : c})

@login_required(login_url='login')
def delete(request, pk):
    obj = Notes.objects.get(id=pk)
    obj.delete()
    return redirect('home')

@login_required(login_url='login')
def Addnote(request):
    if request.method == 'POST':
        note = request.POST["addtxt"]
        tag = request.POST["addtag"]
        heading = request.POST["addtitle"]

        obj2 = Notes(userid=User.objects.get(pk=request.user.id), heading=heading,body=note, tag=tag)
        obj2.save()

        context = {"notes" : obj2}
        return redirect('home')

@login_required(login_url='login')
def home(request):
    user = User.objects.get(pk=request.user.id)
    obj = Notes.objects.all().filter(userid=user)

    return render(request, 'notesapp/home.html', {"notes":obj})

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'notesapp/login.html', {"WA" : "Incorrect Credentials"})
    return render(request, 'notesapp/login.html')


def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        fname = request.POST['fname']
        lname = request.POST['lname']
        obj = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname)
        obj.save()

        return redirect('login')
    return render(request, 'notesapp/register.html')

def LogoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, "notesapp/login.html")
    else:
        return redirect('login')
