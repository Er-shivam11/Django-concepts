from django.shortcuts import render

# Create your views here.

# relative import of forms
from .models import ShivamBytes
from .forms import ShivamBytesForm


def create_view(request):
	# dictionary for initial data with 
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = ShivamBytesForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "create_view.html", context)



# relative import of forms


def list_view(request):
	# dictionary for initial data with 
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["dataset"] = ShivamBytes.objects.all()
		
	return render(request, "list_view.html", context)



# relative import of forms

# pass id attribute from urls
# def detail_view(request, id):
# 	# dictionary for initial data with 
# 	# field names as keys
# 	context ={}

# 	# add the dictionary during initialization
# 	# context["data"] = ShivamBytes.objects.get(id = id)
		
# 	return render(request, "detail_view.html", context)


