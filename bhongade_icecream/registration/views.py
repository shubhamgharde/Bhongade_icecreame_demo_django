from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def homepage(request):
    return render(request, 'home.html')


def SignUpPage(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mob = request.POST['mob']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username):
                messages.info(request, 'Email is exist')
                return redirect('signup')

            else:
                my_user = User.objects.create_user(username=username, first_name=first_name,
                                                   last_name=last_name, email=email,password=password1)

                my_user.mobile_no = mob

                my_user.set_password(password1)
                my_user.save()
                return redirect('login')

        else:
            messages.info(request, 'password are not matching')
            return redirect('signup')

    else:
        return render(request, 'signup.html',{})


def LoginPage(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request, username=name, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':"Invalid Credentials..!!"})


    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')
