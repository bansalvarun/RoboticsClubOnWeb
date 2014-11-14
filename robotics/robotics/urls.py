from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'robotics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^logout/', 'robotics.views.logout'),
    url(r'^$', 'robotics.views.welcome', name='welcome.html' ),
    url(r'^notmember/', 'robotics.views.notmember', name='notmember.html' ),
    (r'^home/', include('club.urls')),

)
