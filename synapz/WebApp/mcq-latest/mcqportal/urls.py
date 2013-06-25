from django.conf.urls import patterns, url

from mcqportal import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
#	url(r'^p1_submit/$', views.p1_submit, name='index'),
	url(r'^pg1$', views.chksession, name='pg1'),
    url(r'^pg2$', views.chksession, name='pg2'),
	url(r'^pg3$', views.chksession, name='pg3'),
	url(r'^pg4$', views.chksession, name='pg4'),
	url(r'^pg5$', views.pg5, name='pg5'),
	url(r'^login', views.login, name='login'),
	url(r'^signin$', views.signin, name='signin'),
	url(r'^signup$', views.signup, name='signup'),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^fbsave', views.save, name='save'),
)
