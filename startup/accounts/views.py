from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
def home(request):
	return HttpResponse('your in home page now ')
def register_page(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
			messages.success(request,'Your Account has been created Successfully')
	context = {'form':form}
	return render(request,'accounts/registeration_page.html',context)

def login_page(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request,'Username OR Password is incorrect ')
			
	return render(request,'accounts/login_page.html')
