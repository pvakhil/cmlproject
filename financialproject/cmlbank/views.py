from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import Branch
from .forms import RegistrationForm



def index(request):

    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid id")
            return redirect('login')
    return render(request, 'login.html')





def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password==password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save();

        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')



    return render(request, 'register.html')




def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')

    form = RegistrationForm()
    dict_form={
        'form':form
    }

    return render(request, 'registration.html', dict_form)

def get_branches(request, district_id):
    branch = Branch.objects.filter(district_id=district_id).values('id', 'name')
    return JsonResponse(list(branch), safe=False)



def branches(request):
    return render(request, 'branches.html')

def settings(request):
    return render(request, 'settings.html')