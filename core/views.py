from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
import json
from core.forms import InformationForm
from .models import Information


#view for display json data
def show_data(request):
    objs = Information.objects.filter(id__range=["1", "50"])
    return render(request,"core/show.html",{'objs':objs})            


#Delete View
def delete_data(request,id):
        obj_instance = Information.objects.get(pk=id)
        obj_instance.delete()
        return HttpResponseRedirect('/')

        
        
#Update View
def update_data(request,id):
    if request.method =='POST':
        pi = Information.objects.get(pk=id)
        fm = InformationForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('/')
        
    else:
        pi = Information.objects.get(pk=id)
        fm = InformationForm(instance=pi)
        
    return render(request,'core/update.html',{'form':fm})
        





