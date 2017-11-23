from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Moneybook
from .forms import CreateMoneybookForm

def calculate(qs):
    sum_expense = 0
    sum_saving = 0
    cnt=1
    
    for instance in qs:
        if instance.is_expense:
            sum_expense += int(instance.price)
            print(sum_expense)
        else:
            sum_saving += int(instance.price)                
        cnt+=1   

    result = (sum_expense, sum_saving)
    return result

def index(request):
    qs = Moneybook.objects.all()
    rest1 = calculate(qs)
    print(rest1[0])
    print(rest1[1])

    context={
        "objects" : qs,
        "expense" : rest1[0],
        "saving" : rest1[1],
        "rest" : rest1[1] - rest1[0]
    }
    
    return render(request,'moneybook/index.html',context)


def detail(request, pk):
    instance = get_object_or_404(Moneybook, pk=pk)
    return render(request,"moneybook/detail.html",{"instance":instance})


def moneybook_create(request):
    if request.method =="POST":
        form = CreateMoneybookForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
    context={"form" : form,}

    return render(request,"moneybook/create_form.html",context)
