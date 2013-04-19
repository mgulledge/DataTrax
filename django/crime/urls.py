from django.conf.urls import patterns, include, url
from crime import views
from django.conf import settings 


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crime.views.home', name='home'),
    # url(r'^crime/', include('crime.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^crime/$', views.inmatelist, name="inmatelist"),
    url(r'^crime/today/$', views.todayinmates, name="todayinmates"),
    url(r'^crime/active/$', views.activeinmates, name="activeinmates"),
    url(r'^main/$', views.inmate, name="inmate"),

)
