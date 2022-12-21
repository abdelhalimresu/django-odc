from django.shortcuts import render
from contact.forms import ContactForm
from django.contrib import messages


# Create your views here.
def contact(request):
	if request.method == "POST":
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			contact_form.save()
			messages.success(request, ('Your message was successfully added!'))
		else:
			messages.error(request, 'Error saving form')
	contact_form = ContactForm()
	return render(request=request, template_name="contact.html", context={'form':contact_form})