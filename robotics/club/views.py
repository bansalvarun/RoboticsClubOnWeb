from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import logout as auth_logout
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from robotics.views import *
from club.models import *
from club.forms import *

def memhome(request):
	if request.user.is_authenticated():
#		newuser = members(fname = "kushagra", lname = "singh",email = "singh.kushagra.1996@gmail.com", stream = "CSE", role = '1',batch = 'BTech2014',rollno = '2014056')
#		newuser.save()
		try:
			curruser = members.objects.get(email = request.user.email)
		except:
			return HttpResponseRedirect('/notmember')

		args = {}
		args.update(csrf(request))
		return render_to_response('memberhome.html',args)
	else:
		return HttpResponseRedirect('/')


def forum(request):
	if request.user.is_authenticated():
		try:
			curruser = members.objects.get(email = request.user.email)
		except:
			return HttpResponseRedirect('/notmember')

		if request.method == "POST":
			newpost = post(title = request.POST['title'], text = request.POST['text'], author = curruser)
			newpost.save()

		allposts = post.objects.all()
		args = {}
		args.update(csrf(request))	
		args['postform'] = postform()	
		args['allposts'] = allposts
		return render_to_response('forum.html',args)
	else:
		return HttpResponseRedirect('/')

def viewdiscussion(request,param):
	if request.user.is_authenticated():
		try:
			curruser = members.objects.get(email = request.user.email)
		except:
			return HttpResponseRedirect('/notmember')
		try:
			currdiscussion = post.objects.get(id= param)
		except:
			return HttpResponseRedirect('/')

		if request.method=="POST":
			newcomment = comment(text = request.POST['text'],author = curruser, discussion = currdiscussion)			
			newcomment.save()


		args = {}
		args.update(csrf(request))	
		args['discussion'] = currdiscussion
		args['commentform'] = commentform()
		args['comments'] = comment.objects.filter(discussion = currdiscussion)
		return render_to_response('discussion.html',args)
	else:
		return HttpResponseRedirect('/')


def skill(request):
	if request.user.is_authenticated():
		try:
			curruser = members.objects.get(email = request.user.email)
		except:
			return HttpResponseRedirect('/notmember')

		if request.method=='POST':
			newskill = skills(skill = request.POST['skill'],mem = curruser)
			newskill.save()

		args = {}
		args.update(csrf(request))
		args['skillform'] = addskill()

		return render_to_response('skill.html',args)
	else:
		return HttpResponseRedirect('/')

def interest(request):
	if request.user.is_authenticated():
		try:
			curruser = members.objects.get(email = request.user.email)
		except:
			return HttpResponseRedirect('/notmember')

		if request.method=='POST':
			newinterest = interests(interest = request.POST['interest'],mem = curruser)
			newinterest.save()

		args = {}
		args.update(csrf(request))
		args['interestform'] = addinterest()

		return render_to_response('interest.html',args)
	else:
		return HttpResponseRedirect('/')

def project(request):
	if request.user.is_authenticated():
		try:
			curruser = members.objects.get(email = request.user.email)
		except:
			return HttpResponseRedirect('/notmember')

		if request.method=='POST':
			newproject = projects(title = request.POST['title'],description = request.POST['description'], status = request.POST['status'],mem = curruser)
			newproject.save()

		args = {}
		args.update(csrf(request))
		args['projectform'] = addproject()

		return render_to_response('project.html',args)
	else:
		return HttpResponseRedirect('/')


def profile(request):
	if request.user.is_authenticated():
		try:
			curruser = members.objects.get(email = request.user.email)
		except:
			return HttpResponseRedirect('/notmember')

		args = {}
		args.update(csrf(request))	
		args['interests'] = interests.objects.filter(mem = curruser)
		args['skills'] = skills.objects.filter(mem = curruser)
		args['projects'] = projects.objects.filter(mem = curruser)
		args['user'] = curruser
		args['infoform'] = editinfoform(initial = {'fname':curruser.fname, 'lname':curruser.lname, 'rollno':curruser.rollno, 'email':curruser.email})
		args['infoform'].fields['email'].widget.attrs['readonly'] = True
		
		if request.method=='POST':
			curruser.fname = request.POST['fname']
			curruser.lname = request.POST['lname']
			curruser.stream = request.POST['stream']
			curruser.batch = request.POST['batch']
			curruser.rollno = request.POST['rollno']
			curruser.save()

		return render_to_response('profile.html',args)

	else:
		return HttpResponseRedirect('/')



