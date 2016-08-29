from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^register/$',views.register,name='register'),
	url(r'^regpro/$',views.regpro,name='regpro'),
	url(r'^logpro/$',views.logpro,name='logpro'),
	url(r'^thanks/$',views.thanks,name='thanks'),
	url(r'^login/$',views.login,name='login'),
	url(r'^sorry/$',views.sorry,name='sorry'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^main/(?P<Username>\w{1,50})/$',views.main,name='main'),
	url(r'^send/$',views.send,name='send'),
	url(r'^sorry2/$',views.sorry2,name='sorry2'),
	
]