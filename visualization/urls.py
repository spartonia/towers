from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

from visualization import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)