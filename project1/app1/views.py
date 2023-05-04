from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import LoginForm,SignupForm,UpdateForm,ChangePassword
from .models import userdata

def index(request):
    return render(request,"index.html")

def login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
           
            user=userdata.objects.get(Email=email)
            if not user:
                messages.warning(request,"Email does not exist")
                return redirect('/login')
            elif password!=user.Password:
                messages.warning(request,"password incorrect")
                return redirect('/login')
            else:
                messages.warning(request,"success")
                return redirect('/home/%s' % user.id)
            
            
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})
                    

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            phone=form.cleaned_data['Phone']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']

            user=userdata.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,'email already exist')
                return redirect('/login')
            else:
                add=userdata(Name=name,Age=age,Place=place,Phone=phone,Email=email,Password=password)
                add.save()
                messages.success(request,'Data Saved')
                return redirect('/')
    else:
        form=SignupForm()
    return render(request,"signup.html",{'form':form})

def update(request,id):
    user=userdata.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'success')
            return redirect('/home/%s' %user.id)

            
    else:
        form=UpdateForm(instance=user)
    return render(request,"update.html",{'user':user,'form':form})

def changepassword(request,id):
    user=userdata.objects.get(id=id)
    if request.method=='POST':
        form=ChangePassword(request.POST or None)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            
            if oldpassword!=user.Password:
                messages.warning(request,'incorrect')
                return redirect('/changepassword/%s' %user.id)
            elif oldpassword==newpassword:
                messages.warning(request,'similar password')
                return redirect('/changepassword/%s' %user.id)
            elif newpassword!=confirmpassword:
                messages.warning(request,'not same')
                return redirect('/changepassword/%s' %user.id)
            else:
                user.Password=newpassword
                user.save()
                messages.success(request,"change success")
    else:
        form=ChangePassword()
        
    return render(request,"changepassword.html",{'user':user,'form':form})

def home(request,id):
    user=userdata.objects.get(id=id)
    return render(request,"home.html",{'user':user})

def gallery(request):
    return render(request,"gallery.html")

