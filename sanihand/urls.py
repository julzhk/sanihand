from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^checkin/$', 'sanihand.tracking.views.checkin_beacon', name='home'),
    url(r'^beacon/(.*)$', 'sanihand.tracking.views.get_beacon', name='home'),
    url(r'^$', 'sanihand.tracking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)