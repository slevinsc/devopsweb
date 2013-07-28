from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'website.views.home', name='home'),
                       # url(r'^website/', include('website.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/',
                       # include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'view.index'),
                       url(r'.*css/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': '/home/slevin/workspace/website/static/css'}
                           ),
                       url(r'.*js/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': '/home/slevin/workspace/website/static/js'}
                           ),
                       url(r'.*img/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': '/home/slevin/workspace/website/static/img'}
                           ),
                       url(r'^article', 'view.index'),
                       url(r'^deploy', 'view.index'),



                       )
