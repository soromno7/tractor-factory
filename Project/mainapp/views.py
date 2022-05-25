from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import IsVoited, Part, Kondorse, Vote
from .forms import  KondorseForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def index(request):
    user = request.user.username
    user2 = IsVoited.objects.filter(user=user)
    data = {"user": user, "user2": user2}

    return render(request, 'index.html', context=data)



#Register/Login


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():

                 return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                user2 = username
                is_voted = False
                kekvoted = IsVoited.objects.create(is_voted=is_voted, user = user2)
                kekvoted.save()
                return redirect('login')

        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    else:

        return render(request, 'register.html')

def login(request):
     if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']

         user = auth.authenticate(username=username, password=password)

         if user is not None:
             auth.login(request, user)
             return redirect('/')
         else:

            return redirect ('login')
     else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def part(request):
    parts = Part.objects.all()
    data = {"parts": parts}
    return render(request, 'part.html', context=data)

def part_ordered_name(request):
    parts = Part.objects.order_by('name')
    data = {"parts": parts}
    return render(request, 'part.html', context=data)

def part_ordered_price(request):
    parts = Part.objects.order_by('price')
    data = {"parts": parts}
    return render(request, 'part.html', context=data)

def part_filtrated(request):
    parts = Part.objects.filter(price__lte =100)
    data = {"parts": parts}
    return render(request, 'part.html', context=data)

@login_required(login_url='login')
def vote(request):
    if request.method == 'POST':
        place1 = request.POST['place1']
        place2 = request.POST['place2']
        place3 = request.POST['place3']

        if ((place1 == place2) and (place1 == place3) and (place2 == place1) and (place2 == place3)) or ((place1 == place2) or (place2 == place3)):
            messages.info(request, 'Поставщики не могут быть одинаковыми')
            return redirect('vote')
        else:
            vote = Kondorse.objects.create(place1=place1, place2=place2, place3=place3)
            vote.save()
            user = request.user.username
            user2 = IsVoited.objects.get(user=user)
            user2.is_voted = True
            user2.save()
            return redirect('index')
    else:
        vote = Vote.objects.all()
        form = KondorseForm()
        return render(request, 'vote.html', {"form": form, "vote":vote})


def kondorse(request):
    arr = [[0, 0, 0], 
           [0, 0, 0],
           [0, 0, 0]]
    votes = Kondorse.objects.all()
    for vote in votes:
        place1 = vote.place1
        place2 = vote.place2
        place3 = vote.place3
        if place1 == '1':
            arr[0][1] +=1
            arr[0][2] += 1
            if place2 == '2':
                arr[1][2] += 1
            else:
                arr[2][1] += 1 
        if place1 == '2':
            arr[1][0] +=1
            arr[1][2] += 1
            if place2 == '3':
                arr[2][0] += 1
            else:
                arr[0][2] += 1
        if place1 == '3':
            arr[2][0] +=1
            arr[2][1] += 1
            if place2 == '2':
                arr[1][0] += 1
            else:
                arr[0][1] += 1
    a1 = arr[0][0] + arr[0][1] + arr[0][2]
    a2 = arr[1][0] + arr[1][1] + arr[1][2]
    a3 = arr[2][0] + arr[2][1] + arr[2][2]
    respose = ""
    if a1 > a2 and a1 > a3:
        response = "Наилучшие комплектующие - A"
    if a2 > a1 and a2 > a3:
        response = "Наилучшие комплектующие - B"
    if a3 > a1 and a3 > a2:
        response = "Наилучшие комплектующие - C"
    data = {"a1":a1, "a2":a2, "a3":a3, "response":response, "arr": arr}
    return render(request, 'index.html', context=data)



