
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.template import RequestContext, loader

from .forms import RegisterForm
from .models import User,Message
# Create your views here.
def login(request):
	template = loader.get_template('Messenger/login.html')
	context=RequestContext(request,{})
	return HttpResponse(template.render(context))

def register(request):
	template = loader.get_template('Messenger/register.html')
	context=RequestContext(request,{
		'form':RegisterForm() ,
		})
	return HttpResponse(template.render(context))

def regpro(request):
	if request.method=='POST':
		Username=request.POST['Username']
		u=User.objects.filter(username=Username)
		if len(u)==0:
			name=request.POST['Name']
			username=request.POST['Username']
			password=request.POST['Password']
			contact=request.POST['Contact']
			#return render(request,'test.html',{'username':username, 'pass':password})
			u=User()
			u.name=name
			u.username=username
			u.password=password
			u.contact=contact
			u.save()
			return HttpResponseRedirect('../thanks')
		else:
			return HttpResponseRedirect('../sorry')
	else:
		template = loader.get_template('Messenger/register.html')
		context=RequestContext(request,{})
		return HttpResponse(template.render(context))

def logpro(request):
	if request.method=='POST':
		Username=request.POST['Username']
		Password=request.POST['Password']
		request.session['username']=Username
		u=User.objects.filter(username=Username,password=Password)
		if(len(u)==0):
			return HttpResponseRedirect('../sorry')
		
		u.update(logged_in=True)
		return HttpResponseRedirect('../main/'+request.session['username'])

def logout(request):
	request.session['username']="admin"

	#User.objects.filter(request.).update(logged_in=False)
	return HttpResponseRedirect('../login')



def thanks(request):
	template=loader.get_template('Messenger/thanks.html')
	context=RequestContext(request,{})
	return HttpResponse(template.render(context))

def sorry(request):
	template=loader.get_template('Messenger/sorry.html')
	context=RequestContext(request,{})
	return HttpResponse(template.render(context))

def main(request,Username):
	u=User.objects.get(username=Username)
	#context=RequestContext(request,{'session':request.session['username'],'user':u})
	return render(request, 'Messenger/main.html', {'session':request.session['username'],'user':u})

def sorry2(request):
	template=loader.get_template('Messenger/sorry2.html')
	context=RequestContext(request,{
		'session':request.session['username']
		})
	return HttpResponse(template.render(context))

def send(request):
	if request.method=='POST':
		receiver_name=User()
		
		#m.user=u
		receiver_check=User.objects.filter(username=request.POST['receiver_name'])
		if len(receiver_check)>0:
			receiver_name=User.objects.get(username=request.POST['receiver_name'])
			Message.objects.create(message_text=request.POST['message'],receiver=receiver_name,sender=request.session['username'])
			return HttpResponseRedirect('../main/'+request.session['username'])
		
		else:
			'''template=loader.get_template('Messenger/sorry2.html')
			context=RequestContext(request,{
				'session':request.session['username']
				})
			return HttpResponse(template.render(context))'''
			return HttpResponseRedirect('../sorry2/')

