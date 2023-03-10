from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,password=password, email=email)
                user.save();
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

# def index(request):
#     Task1 = task.objects.all()
#     if request.method == 'POST':
#         name = request.POST.get('Task', '')
#         priority = request.POST.get('priority', '')
#         date = request.POST.get('date','')
#         Task = task(name=name, priority=priority, date=date)
#         Task.save()
# return render(request, 'home.html', {'Task': Task1})