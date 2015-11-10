"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

# urls.py, a Python script to store URL patterns for your project; and

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')), # tuple links the main urls.py w/ the rango app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Use the Django 1.8 to add the URL patterns for the Static Media


# shows the routes of the static directory, Django doesn't normally let you see the routes
# if not settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Handles dispatching media
# if settings.DEBUG:
#     urlpatterns += (
#         'django.views.static',
#         (r'^media/(?P<path>.*)',
#         'serve',
#         {'document_root': settings.MEDIA_ROOT}), )
