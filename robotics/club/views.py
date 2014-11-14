from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import logout as auth_logout
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from robotics.views import *

def memhome(request):
	if request.user.is_authenticated():


		args = {}
		args.update(csrf(request))
		return render_to_response('memberhome.html',args)
	else:
		return HttpResponseRedirect('/')
