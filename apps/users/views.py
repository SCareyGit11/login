from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def welcome(request):
	form = RegisterForm()
	context = {
	'regform' : form
	}
	return render(request, 'users/welcome.html', context)

def register(request):
	pass