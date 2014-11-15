from django import forms 
from models import *


class postform(forms.ModelForm):
	title = forms.CharField(required=True,widget=forms.TextInput)
	text = forms.CharField(required=True,widget=forms.Textarea(attrs={'cols': 30, 'rows': 10}))

	class Meta:
		model = post
		fields = ('title','text')

class commentform(forms.ModelForm):
	text = forms.CharField(required=True,widget=forms.TextInput,label = ' ')

	class Meta:
		model = comment
		fields = ('text',)

class addskill(forms.ModelForm):
	skill = forms.CharField(required=True,widget=forms.TextInput)

	class Meta:
		model = skills
		fields = ('skill',)

class addinterest(forms.ModelForm):
	interest = forms.CharField(required=True,widget=forms.TextInput)

	class Meta:
		model = interests
		fields = ('interest',)

stat = (
			('0','completed'),
			('1','undergoing'),
	)


class addproject(forms.ModelForm):
	title = forms.CharField(required=True,widget=forms.TextInput)
	description = forms.CharField(required=True,widget=forms.Textarea)
	status = forms.ChoiceField(choices = stat)

	class Meta:
		model = projects
		fields = ('title','description','status')

streams = (
			('ECE','ECE'),
			('CSE','CSE'),
	)

batches = (

			('BTech2014','BTech2014'),
			('BTech2013','BTech2013'),
			('BTech2012','BTech2012'),
			('BTech2011','BTech2011'),
			('MTech2014','MTech2014'),
			('MTech2013','MTech2013'),

	)

class editinfoform(forms.ModelForm):
	fname = forms.CharField(required = True,widget = forms.TextInput, label = 'first name')
	lname = forms.CharField(required = True,widget = forms.TextInput,label = 'last name')
	email = forms.EmailField(required = True,widget = forms.TextInput)
	stream = forms.ChoiceField(choices = streams)
	batch = forms.ChoiceField(choices = batches)
	rollno = forms.IntegerField(required = True)

	class Meta:
		model = members
		fields = ('fname','lname','stream','batch','rollno')

roles = (
			('1','member'),
			('3','admin'),
	)

class adduserform(forms.ModelForm):
	email = forms.EmailField()
	role = forms.ChoiceField(choices = roles)

	class Meta:
		model = members
		fields = ('email','role',)

class anouncementform(forms.ModelForm):
	title = forms.CharField(required=True,widget=forms.TextInput)
	author = models.ForeignKey(members, null=True, blank=True)

	class Meta:
		model = anouncement
		fields = ('title',)

class eventform(forms.ModelForm):
	title = forms.CharField(required=True,widget=forms.TextInput)
	description = forms.CharField(required=True,widget=forms.Textarea)
	author = models.ForeignKey(members, null=True, blank=True)

	class Meta:
		model = event
		fields = ('title','description',)






