# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect
from models import *
import bcrypt
# Create your views here.
def index(request):
	request.session['log'] = False
	return render(request,"reg_login/index.html")
def registration(request):
	if request.method == "POST":
		request.session['log_reg']='reg'
		errors = User.objects.reg_validator(request.POST)
		if len(errors):
			for tag,error in errors.iteritems():
				messages.error(request,error,extra_tags=tag)
			return redirect('/')
		print request.POST['email']
		user = User.objects.filter(email = request.POST['email'])
		if user:
			messages.error(request,"Please enter a valid email",extra_tags="email")
			return redirect('/')
		secure_password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
		User.objects.create(first_name=request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'],password = secure_password)
		request.session['log'] = True
		request.session['user_id'] = User.objects.last().id
		return redirect('/success')
	return redirect('/')

	return redirect('/')
def login(request):
	if request.method == "POST":
		request.session['log_reg'] = 'log'
		user = User.objects.filter(email = request.POST['email'])
		if user and bcrypt.checkpw(request.POST['password'].encode(),user[0].password.encode()):
			request.session['log'] = True
			request.session['user_id'] = user[0].id
			return redirect('/success')
		else:
			messages.error(request,"Email and password not match",extra_tags="login")
			return redirect('/')
	return redirect('/')
def success(request):
	if "log" in request.session and request.session['log']:
		user = User.objects.get(id=request.session['user_id'])
		context = {
			'user': user
		}
		return render(request,"reg_login/success.html",context)
	return redirect('/')