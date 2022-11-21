from django.shortcuts import render,HttpResponse

from .models import list

# Create your views here.
def list1(request):
    if request.method == 'POST':
        add_list = request.POST.get('add_list')
        users = list()
        users.Add_list = add_list
        users.save()
    return render(request,'base.html')

def pending(request):
    details = list.objects.filter(Status=False)
    return render(request,'admin.html',{'value':details})

def approve(request,id):
    data = list.objects.get(id=id)
    data.Status = True
    data.save()
    return render(request,'admin.html')


def approved(request):
    details = list.objects.filter(Status=True)
    return render(request,'approved.html',{'value':details})

def delete(request,id):
    data1 = list.objects.filter(id=id).delete()
    return render(request,'admin.html')
