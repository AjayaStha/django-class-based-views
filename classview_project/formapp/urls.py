from django.conf.urls import url
from .views import ContactView


urlpatterns = [
	url(r'^contact/$', ContactView.as_view(), name='contact_form'),

]