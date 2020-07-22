from django.conf.urls import include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from morfemas import views
from django.views.static import *

admin.autodiscover()

urlpatterns = [
	# Examples:
	url(r'^$', views.morfemas, name = "home"),
	url(r'^search/$', views.search, name = "search"),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', admin.site.urls),
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

	url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
	]
