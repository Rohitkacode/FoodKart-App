from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm


# Create your views here.


def Index(request):
    item_list = Item.objects.all()

    context = {
        "item": item_list
    }

    return render(request, 'food/index.html', context)
    

def list(request):
    item_list = Item.objects.all()
    return HttpResponse(item_list)



def detail(request,item_id):
     item = Item.objects.get(id=item_id)
     context = {
         "item": item
    }
     
     return render(request, 'food/detail.html',context)


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:views")
    return render(request, 'food/item-form.html', {'form': form})

def update_item(request,id):
    """Update an existing item here id is id of the data, we are getting that item"""
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("food:views")
    return render(request, 'food/item-form.html', {'form': form})


def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect("food:views")
    return render(request, 'food/item-delete.html', {'item':item})


