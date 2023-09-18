from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from .models import Item
from django.http import HttpResponse
from django.core import serializers


# Create your views here.

def home(request):
    all_items = Item.objects.all()
    total_item = Item.objects.count()

    total_amount = 0
    for obj in Item.objects.all():
        total_amount += obj.amount

    return render(request, 'home.html',
                  {'all': all_items, 'total_item': total_item,
                   'total_amount': total_amount})  # Render isi dari data Item kita ke file home.html


def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:home'))

    context = {'form': form}
    return render(request, 'create_product.html', context)


def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
