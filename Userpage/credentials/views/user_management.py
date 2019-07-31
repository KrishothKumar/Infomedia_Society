from django.shortcuts import render, redirect
from credentials.models import Register
from django.contrib.auth.models import auth
from django.contrib import messages

def login(request):
    print("debugging")
    if request.method =="POST":

        e_mail = request.POST.get('username', '')
        password =request.POST.get('password','')

        user = auth.authenticate(e_mail = e_mail, password = password)

        if user:
            auth.login(request, user)
            return redirect('/activities')

        else:

            messages.info(request, "Username or Password may incorrect")
            return redirect('/login')

    else:

        return render(request, 'home.html')

def register(request):
    if request.method =="POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        e_mail = request.POST['e_mail']
        # skills = request.POST['skills']
        password1 = request.POST['password1']
        password2 = request.POST['password1']

        if password1 == password2:
            if Register.objects.filter(e_mail= e_mail).exists():

                messages.info(request, 'E-mail is already exists')
                return redirect('/register')

            elif Register.objects.filter(username= username).exists():

                messages.info(request, 'Username is already exists')
                return redirect('/register')

            else:
                user = Register.objects.create_user(e_mail=e_mail, password= password1,
                                                    first_name=first_name, last_name =last_name,
                                                    username= username)
                user.save()
                messages.info(request, 'Sign Up successfully')
                return redirect('/')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
