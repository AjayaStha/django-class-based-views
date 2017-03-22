from django.views.generic import FormView,TemplateView
from django.shortcuts import render, redirect

from .forms import ContactForm


class ContactView(FormView):
	template_name = 'index.html'
	form_class = ContactForm
	success_url = '/Thank you/'

	def get(self,request,*args, **kwargs):
		form = self.form_class(initial=self.initial)
		return render(request,self.template_name,{'form':form})

	def post(self,request,*args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/thanks/')
		return render(request, self.template_name,{'form':form})

class Home(TemplateView):
	template_name='home.html'