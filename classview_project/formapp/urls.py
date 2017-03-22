from django.conf.urls import url
from .views import ContactView, Home


urlpatterns = [
	url(r'^$',Home.as_view(),name='home'),
	url(r'^contact/$', ContactView.as_view(), name='contact_form'),

]