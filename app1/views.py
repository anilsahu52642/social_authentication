from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth as model2

# for signup ...................
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            userid=User.objects.get(username=username).id
            if model2.objects.filter(user_id=userid).exists():
                print('success .................................1 userid is:',userid)
                messages.error(request,'user allready exist with username......')
        elif User.objects.filter(email=email).exists() or model2.objects.filter(uid=email).exists():
            print('success ..................................2')
            un=User.objects.get(email=email).username
            context={'username':un}
            messages.error(request,'email id is allready in used... with username')
            return render(request, 'home.html', context)

        else :
            fm=User(username=username,first_name=username,email=email,password=make_password(password))
            fm.save()
            print('success .....................................3')
            userinstance=User.objects.get(username=username)
            fm2=model2(user=userinstance,provider='default signup',uid=email)
            fm2.save()
            messages.info(request,'user successfully added .......')
    return render(request,'home.html')

# for signin of user...................
def signin(request):
    if request.method=='POST':
        un=request.POST['username']
        ps=request.POST['password']
        x=authenticate(username=un,password=ps)
        if x is not None:
            login(request,x)
            return HttpResponseRedirect('/profile/')
        else:
            messages.error(request,'sorry username or password is incorrect...')
    return render(request, 'auth.html')


# for profile page...........
# @login_required
def profile(request):
    return render(request,'profile.html')

# @login_required
def mylogout(request):
    logout(request)
    return HttpResponseRedirect('/signin/')

