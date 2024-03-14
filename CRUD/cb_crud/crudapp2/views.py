from typing import Any
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

# relative import of forms
from .models import ShivamBytes
from .forms import ShivamBytesForm
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateView,RedirectView
from django.views import View
class AddandShowView(TemplateView):
    template_name='create_view.html'
    def get_context_data(self, *args, **kwargs):
        fm= ShivamBytesForm()
        dmx = ShivamBytes.objects.all()
        context={'form':fm,'dataset':dmx}
        return context
    
    def post(self,request):
         fm=ShivamBytesForm(request.POST)
         if fm.is_valid():
              nm=fm.cleaned_data['name']
              ci=fm.cleaned_data['city']
              form=ShivamBytes(name=nm,city=ci)
              form.save()
              return HttpResponseRedirect('/')
# def create_view(request):
# 	# dictionary for initial data with 
# 	# field names as keys
# 	context ={}

# 	# add the dictionary during initialization
# 	form = ShivamBytesForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
		
# 	context['form']= form
# 	context["dataset"] = ShivamBytes.objects.all()

# 	return render(request, "create_view.html", context)



# relative import of forms


def list_view(request):
	# dictionary for initial data with 
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["dataset"] = ShivamBytes.objects.all()
		
	return render(request, "list_view.html", context)


# def update_view(request, pk):
#     context = {}
#     obj = get_object_or_404(ShivamBytes, pk=pk)
#     form = ShivamBytesForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#         return redirect('home')  
#     # Redirect to the show view after updating
#     context['form'] = form
#     return render(request, "update_view.html", context)

# def delete_view(request, pk):
#     obj=ShivamBytes.objects.get(pk=pk)
#     print(obj)
    
#     delete_user_form=ShivamBytesForm(instance=obj)

#     if request.method == 'POST':
#         obj.delete()
#         return redirect('home')
#     else:
#         return HttpResponse('You are not allowed to delete this object.')



class DeleteView(RedirectView):
     url='/'
     def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        del_id=kwargs['id']
        ShivamBytes.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
     
class UpdateView(View):
    def get(self,request,id):
         ud=ShivamBytes.objects.get(pk=id)
         fm=ShivamBytesForm(instance=ud)
         return render(request,'update_view.html',{'form':fm})
    def post(self,request,id):
         ud=ShivamBytes.objects.get(pk=id)
         fm=ShivamBytesForm(request.POST,instance=ud)
         if fm.is_valid():
              fm.save()
         return HttpResponseRedirect('/')

        