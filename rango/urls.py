from django.conf.urls import patterns, url
from rango import views

# allows regex expressions for urlpatterns
# any pattern matched by the regex expression makes Django call views.index()
# Use views.variable_name to call function

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/', views.about, name='about'),
                       )
