from django.http import HttpResponseRedirect
from django.shortcuts import  redirect, render
import json
from core.forms import InformationForm
from .models import Information




#view for display json data
def show_data(request):
    objs = Information.objects.filter(id__range=["1", "200"])
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
        



#chart select
def chart_view(request):
    return render(request, 'core/visualization.html')


#bar chart
def bar_chart_view(request):
    data = Information.objects.all().order_by('date')
    context = {
        'chart_data': data,
        
    }
    return render(request, 'core/bar.html', context)


#line chart
def line_chart_view(request):
    data = Information.objects.all().order_by('date')
    context = {
        'chart_data': data,
        
    }
    return render(request, 'core/line.html', context)






