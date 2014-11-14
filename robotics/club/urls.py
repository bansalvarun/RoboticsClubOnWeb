from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'robotics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'club.views.memhome', name='memberhome.html' ),
    url(r'^forum/', 'club.views.forum', name='forum.html' ),
    url(r'^profile/', 'club.views.profile', name='profile.html' ),
    url(r'^addskill', 'club.views.skill', name='skill.html' ),
    url(r'^addinterest', 'club.views.interest', name='interest.html' ),
    url(r'^addproject', 'club.views.project', name='project.html' ),
    url(r'^viewdiscussion/(?P<param>.+)', 'club.views.viewdiscussion', name='discussion.html' ),

)
