from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# relative import of forms
from .models import ShivamBytes
from .forms import ShivamBytesForm
from django.shortcuts import get_object_or_404, redirect

def create_view(request):
	# dictionary for initial data with 
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = ShivamBytesForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	context["dataset"] = ShivamBytes.objects.all()

	return render(request, "create_view.html", context)



# relative import of forms


def list_view(request):
	# dictionary for initial data with 
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["dataset"] = ShivamBytes.objects.all()
		
	return render(request, "list_view.html", context)


def update_view(request, pk):
    context = {}
    obj = get_object_or_404(ShivamBytes, pk=pk)
    form = ShivamBytesForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('home')  
    # Redirect to the show view after updating
    context['form'] = form
    return render(request, "update_view.html", context)

def delete_view(request, pk):
    obj=ShivamBytes.objects.get(pk=pk)
    print(obj)
    
    delete_user_form=ShivamBytesForm(instance=obj)

    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    else:
        return HttpResponse('You are not allowed to delete this object.')



