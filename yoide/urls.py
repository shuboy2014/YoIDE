from django.conf.urls import url
from django.contrib import admin
from ide import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^compile-and-run/$', views.compile_and_run),
    url(r'^contact-us/$', views.contact_us),
    url(r'^feedback/$', views.feedback)
]
