from django.conf.urls import url
import views

urlpatterns=[
	url(r'^$',views.index),
	url(r'^login$',views.login),
	url(r'^register$',views.registration),
	url(r'^success$',views.success),
]