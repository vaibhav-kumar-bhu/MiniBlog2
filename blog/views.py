from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import signups,loginform,postform,commentform
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .models import post,addcomment
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
	posts=post.objects.all()
	comment=addcomment.objects.all()
	
	if request.user.is_authenticated:
		
		context={'posts':posts,'comment':comment,'User':request.user}
		return render(request,'core/home.html',context)
	else:
		context={'posts':posts,'comment':comment,'User':None}

		return render(request,'core/home.html',context)

	
	
	

def about(request):
	if request.user.is_authenticated:
		data=User.objects.filter(username=request.user)
		ip=request.session.get('ip',0)
		return render(request,'core/about.html',{'fm':data,'ip':ip})
	else:
		return HttpResponseRedirect('/login/')

def user_login(request):
	if not request.user.is_authenticated:
		if request.method=='POST':
			fm=loginform(request=request,data=request.POST)
			if fm.is_valid():
				nm=fm.cleaned_data['username']
				ps=fm.cleaned_data['password']
				user=authenticate(username=nm,password=ps)
				if user is not None:
					login(request,user)
					messages.success(request,'welcome to the dashboard')

					return HttpResponseRedirect('/dashboard/')
		else:
			fm=loginform()
		return render(request,'core/login.html',{'fm':fm})
	else:
		return HttpResponseRedirect('/dashboard/')

def signup(request):
	if not request.user.is_authenticated:
		if request.method=='POST':
			form=signups(request.POST)
			if form.is_valid():
				form.save()
				form=signups()
				messages.success(request,'Welcome you are now member')
		else:
			form=signups()
		return render(request,'core/signup.html',{'fm':form})
	else:
		return HttpResponseRedirect('/dashboard/')

def contact(request):
	if request.method=='POST':
		message=request.POST['message']
		subjects = request.POST['email']
		if message!='':
			send_mail(
				subject=subjects,
				message=message,
				from_email=settings.EMAIL_HOST_USER,
				recipient_list=['vaibhavakumarsoni@gmail.com'])
			return HttpResponseRedirect('/contact/')
		else:
			HttpResponseRedirect('/contact/')
	return render(request,'core/contact.html')

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/login/')

def dashboard(request):
	if request.user.is_authenticated:
		posts=post.objects.filter(Name=request.user)
		
		return render(request,'core/dashboard.html',{'posts':posts,'name':request.user})
	else:
		return HttpResponseRedirect('/login/')

# add post here 

def addpost(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			fm=postform(request.POST)
			if fm.is_valid():
				tl=fm.cleaned_data['title']
				desc=fm.cleaned_data['description']
				
				pst=post(title=tl , description=desc, Name=request.user)
				pst.save()
				messages.success(request,"congrats Your post successfully posted")
				fm=postform()
		else:
			fm=postform()
		return render(request,'core/addpost.html',{'fm':fm})
	else:
		return HttpResponseRedirect('/login/')
def updatepost(request,id):
	if request.user.is_authenticated:
		if request.method=='POST':
			pi=post.objects.get(pk=id)
			fm=postform(request.POST,instance=pi)
			if fm.is_valid():
				fm.save()
		else:
			pi=post.objects.get(pk=id)
			fm=postform(instance=pi)
		return render(request,'core/updatepost.html',{'fm':fm})
	else:
		return HttpResponseRedirect('/login/')
def deletepost(request,id):
	if request.user.is_authenticated:
		if request.method=='POST':
			pi=post.objects.get(pk=id)
			pi.delete()
			return HttpResponseRedirect('/dashboard/')
	else:
		return HttpResponseRedirect('/login/')

def addcomments(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			comment=request.POST.get('comment')
			user=request.user
			postsno=request.POST.get('postsno')
			posts=post.objects.get(id=postsno)
			if comment=='':
				return HttpResponseRedirect('/')
			else:
				comment=addcomment(comment=comment,user=user,post=posts,comment_id=postsno)
				comment.save()
				messages.success(request,'your comment successfully posted')
			return HttpResponseRedirect('/addcomment/')
				
				
			
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/login/')

'''def imageuploader(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			if 'image' in request.FILES:
				image = images(image=request.FILES['image'])
				image.save()
				image=images()
				messages.success(request,'your post successfully posted')
				img = images.objects.all()
				return render(request,'core/profilepic.html',{'images':img,'media_url':settings.MEDIA_URL})
			else:
				img = images.objects.all()
				return render(request,'core/profilepic.html',{'images':img,'media_url':settings.MEDIA_URL})
		else:
			return HttpResponseRedirect('/dashboard/')
	else:
		return HttpResponseRedirect('/login/')
'''

def deletecomment(request,sno):
	if request.user.is_authenticated:
		if request.method=='POST':
			pi=addcomment.objects.get(pk=sno)
			pi.delete()
			return HttpResponseRedirect('/')

	else:
		return HttpResponseRedirect('/login/')

def editcomment(request,sno):
	if request.user.is_authenticated:
		if request.method=='POST':
			pi=addcomment.objects.get(pk=sno)
			fm=commentform(request.POST,instance=pi)
			if fm.is_valid():
				fm.save()
				return HttpResponseRedirect('/')

		else:
			pi=addcomment.objects.get(pk=sno)
			fm=commentform(instance=pi)
		return render(request,'core/editcomment.html',{'fm':fm})
	else:
		return HttpResponseRedirect('/login/')



