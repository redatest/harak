from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import settings

urlpatterns = patterns('',
    # Examples:
      url(r'^$', 'app.views.home', name='home'),
      #url(r'^$', 'app.views.test', name='test'),
      url(r'^img/$', 'app.views.show_img', name='show_img'),
      url(r'^album/$', 'app.views.show_album', name='show_album'),
      
      url(r'^news/$', 'app.views.show_news', name='show_news'),
      url(r'^news/(?P<num>[\d+])/$', 'app.views.show_new', name = "show_new"),
      
      url(r'^watchnews/$', 'app.views.show_watchnews', name='show_watchnews'),
      url(r'^watchnews/(?P<num>[\d+])/$', 'app.views.show_watchnew', name = "show_watchnew"),
      url(r'^statement/$', 'app.views.state', name='state'),
      url(r'^statement/(?P<num>[\d+])/$', 'app.views.show_state', name = "show_state"),
      
      #search
      url(r'^search/$', 'app.views.search', name='search'),
		
    #admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^vid/$', 'app.views.vid', name='vid'),
)



urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*/)$', 'flatpage'),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

