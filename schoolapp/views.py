from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.template import loader


# Create your views here.


def index(request):
    return render(request,"index.html")

def login(request):
	if request.method == 'POST':
		uname = request.POST.get('uname')
		pwd = request.POST.get('pwd')

		check_user = User.objects.filter(username=uname, password=pwd)
		if check_user:
			request.session['user'] = uname
			return redirect('loggedin')

		else:
			return HttpResponse('Please enter valid Username or Password.')

	return render(request, 'login.html')

def signup(request):
	if request.method == 'POST':
		uname = request.POST.get('uname')
		pwd = request.POST.get('pwd')
		phn= request.POST.get('phn')
		addrs=request.POST.get('address')
		# print(uname, pwd)
		if User.objects.filter(username=uname).count()>0:
			return HttpResponse('Username already exists.')
		else:
			user = User(username=uname, password=pwd,phoneno=phn,address=addrs)
			user.save()
			return redirect('login')
	else:
		return render(request, 'signup.html')

def loggedin(request):
	return render(request, "loggedin.html")