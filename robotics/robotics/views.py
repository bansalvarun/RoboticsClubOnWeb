from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import logout as auth_logout
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from club.views import *
from django.http import HttpResponseRedirect
from club.models import *
def welcome(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/home')
	else:
		args = {}
		args.update(csrf(request))
		return render_to_response('welcome.html',args)


def logout(request):
	auth_logout(request)
	args = {}
	args.update(csrf(request))
	return HttpResponseRedirect('/')

def about(request):
	return render_to_response('about.html')

def events(request):
	eventset = event.objects.all()
	return render_to_response('events.html',{'events':eventset})


def notmember(request):
	if request.user.is_authenticated():
		args = {}
		args.update(csrf(request))	
		args['message'] = "you are nto a member"	
		return render_to_response('welcome.html',args)
	else:
		return HttpResponseRedirect('/')