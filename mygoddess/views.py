from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from mygoddess.models import *
from mygoddess.forms import *
from django.core.files.storage import default_storage
import os
import random
import shutil
# Create your views here.
def is_login(request):
    try:
        if request.user.id:
            return True
    except Exception as e:
        print(e)
    return False

def home(request):
    users = User.objects.all()
    return render(request,'mygoddess/index.html',context={'users':users})

@login_required
def nayanathara_devotee(request):
    users = User.objects.all()
    return render(request,'mygoddess/nayanathara_devotee.html',context={'users':users})

def kajal_devotee(request):
    users = User.objects.all()
    return render(request,'mygoddess/kajal_devotee.html',context={'users':users})

def anushka_devotee(request):
    users = User.objects.all()
    return render(request,'mygoddess/anushka_devotee.html',context={'users':users})

def signup(request):
    if is_login(request):
        return redirect("home")
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        check =request.POST.get('check')
        try:
            index = email.find("@")
        except:
            pass
        if check ==  'True':
            if len(name) == 0:
                messages.error(request, 'Please Enter Name')
            elif len(email) == 0:
                messages.error(request, 'Please Enter Email')
            elif len(username)==0:
                messages.error(request, 'Please Enter Username')
            elif len(password)==0:
                messages.error(request, 'Please Enter Password')
            elif len(re_password)==0:
                messages.error(request, 'Please Confirm Password')
            elif password != re_password:
                messages.error(request, 'Password did not match!')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Exists')
            elif email[index+1:] != "trishadevotee.com":
                messages.error(request, 'Your Email must be end with trishadevotee.com')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Exists')
            else:
                user = User.objects.create_user(first_name=name, username=username, email=email, password=password)
                if user.is_active:
                    print("register")
                    login(request,user)
                    messages.success(request, "మీరు అదృష్టవంతులు కావున త్రిషా అమ్మవారికి భక్తులయ్యారు")
                else:
                    print("error")
                    messages.error(request, "Please Enter Correct Details!")
        else:
            messages.error(request,"Sorry! You should be Live as a GoddessTrisha Devotee,So Please Check The Box.")
        context={'name':name,'email':email,'username':username,'password':password,'re_password':re_password}
        return render(request, 'mygoddess/signup.html',context)
    users = User.objects.all()
    return render(request, 'mygoddess/signup.html',{'users':users})

@login_required
def user_add_profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST,request.FILES)
        if profile_form.is_valid():
            profile_form.cleaned_data['slave'] = request.user
            profile = Profile(**profile_form.cleaned_data)
            if Profile.objects.filter(slave = request.user).exists():
                return JsonResponse({"status":"మీరు ఇదివరకు పూర్వమే త్రిషాదేవి పాదదాసులయ్యారు!"})
            else:
                profile.save()
                return JsonResponse({"status":"అభినందనలు మీరు పూర్తిగా త్రిషాదేవి పాదదాసులయ్యారు!"})
        else:
            return JsonResponse({"status":"దయచేసి అన్నీ వివరాలు సరిగ్గా నమోదు చేయండి!"})
    else:
        profile_form = ProfileForm()
    users = User.objects.all()
    context = {'profile_form':profile_form,'users':users}
    return render(request,'mygoddess/add_profile.html',context)

@login_required
def profile_detail(request,id):
    profile = Profile.objects.get(slave = User.objects.get(id=id))
    users = User.objects.all()
    if request.method == "POST":
        trisha_slave_form = TrishaSlaveForm(request.POST,request.FILES)
        if trisha_slave_form.is_valid():
            picture = i = str("_".join(str(trisha_slave_form.cleaned_data['image']).split()))
            if default_storage.exists(os.path.join(str(os.getcwd()),'media\\trisha_slaves',picture)):
                return JsonResponse({"status":"Image Already Exists!"})
            elif default_storage.exists(os.path.join(str(os.getcwd()),'media\\trisha_slaves',str(trisha_slave_form.cleaned_data['image']))):
                return JsonResponse({"status":"Image Already Exists!"})
            else:
                trisha_slave_form.cleaned_data['name'] = profile
                trisha_slave = TrishaSlave(**trisha_slave_form.cleaned_data)
                trisha_slave.save()
                return JsonResponse({"status":"Uploaded Successfully!"})
        else:
            return JsonResponse({"status":"Error while uploading!"})
    else:
        trisha_slave_form  = TrishaSlaveForm()
    context = {'users':users,'profile':profile,'trisha_slave_form':trisha_slave_form}
    return render(request,'mygoddess/profile_detail.html',context)

@login_required
def goddess_trisha_slaves(request,id):
    try:
        slave_img = TrishaSlave.objects.filter(name = Profile.objects.get(id=id))
    except:
        return HttpResponse("No Profiles Found!")
    users = User.objects.all()
    return render(request,'mygoddess/slave_pics.html',context={'users':users,'slave_pics':slave_img})


def user_login(request):
    if is_login(request):
        return redirect("home")
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return JsonResponse({"status":"Login Successful!"})
        else:
            if len(username) == 0:
                return JsonResponse({'status':'Enter Username'})
            elif len(password) == 0:
                return JsonResponse({'status':'Enter Password'})
            else:
                return JsonResponse({'status':'Invalid Credentials'})
    users = User.objects.all()
    return render(request, 'mygoddess/login.html',context={'users':users})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def devotees(request):
    if request.method == "POST":
        name = request.POST.get('name')
        form = DevoteesForm(request.POST,request.FILES)
        if Devotees.objects.filter(name = name).exists():
            messages.error(request, "Devotee Already Exists!")
        elif form.is_valid():
            form.save()
            messages.success(request,"Congrats You Became GoddessTrisha Devotee!")
        else:
            messages.error(request, "Congrats You Became GoddessTrisha Devotee!")
    else:
        form = DevoteesForm()
    users = User.objects.all()
    return render(request, 'mygoddess/devotees.html', context={'form': form,'users':users})

@login_required
def goddess_temple(request):
    if request.method=="POST":
        devotee = request.POST.get('devotee')
        name = request.POST.get('name')
        date = request.POST.get('date')
        form = SevaForm(request.POST)
        if Seva.objects.filter(Q(devotee = devotee)&Q(date=date)).exists():
            return JsonResponse({"status": "Devotee Already Booked a Slot on this date!"})
        if form.is_valid():
            form.save()
            sevas = Seva.objects.values()
            seva_edit = list(sevas)
            return JsonResponse({"status": "1","status_message":"Slot Booked for Serving  Goddess Trisha!","sevas":seva_edit})
        else:
            return JsonResponse({'status_message': 'Failed to Book a Slot'})
    else:
        form = SevaForm()
    sevas = Seva.objects.all()
    users = User.objects.all()
    return render(request,'mygoddess/goddess_temple.html',context={'form':form,'sevas':sevas,'users':users})

@login_required
def editseva(request):
    edit_id = request.POST.get('edit_id')
    devotee =request.POST.get('devotee')
    name = request.POST.get('name')
    date = request.POST.get('date')
    Seva.objects.filter(id=edit_id).update(devotee=devotee,name=name,date=date)
    sevas = Seva.objects.values()
    seva_edit = list(sevas)
    return JsonResponse({"status": "1","status_message":"Seva Updated Successfully!", "sevas": seva_edit})

@login_required
def deleteseva(request):
    delete_id=request.GET.get("delete_id")
    print(delete_id)
    Seva.objects.filter(id=delete_id).first().delete()
    sevas=Seva.objects.values()
    seva_edit=list(sevas)
    return JsonResponse({"status":"1","status_message":"Seva Deleted Successfully!","sevas":seva_edit})

@login_required
def slaves(request):
    users = User.objects.all()
    return render(request,'mygoddess/slaves.html',context={'users':users})


