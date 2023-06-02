from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    return render(request,'signup.html')
def loginpage(request):
    return render(request,'login.html')

@login_required(login_url='login')
def about(request):
    return render(request,'about.html')


def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']  
        last_name=request.POST['second_name']  
        username=request.POST['user_name']  
        password=request.POST['password']  
        cpassword=request.POST['cpassword']
        email=request.POST['email']  


        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This user name already exists!!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                print('Succeed....')
        else:
            messages.info(request,'Password doesnt match!!!!!')
            print('Password is not matching')
            return redirect('signup')
        return redirect('loginpage')
    else:
        return render(request,'signup.html')
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
           auth.login(request,user)
           messages.info(request,f'Welcome {username}')
           return redirect('about')
        
        else:
            messages.info(request, 'Invalid Username or Pssword.Try again')
            return redirect('loginpage')
    else:
        return redirect('loginpage')
def logout(request):
    auth.logout(request)
    return redirect('home')


                

