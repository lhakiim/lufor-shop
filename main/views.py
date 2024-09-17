from django.shortcuts import render
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ShopEntryForm
from main.models import shopEntry
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    shop_entries = shopEntry.objects.all()

    context = {
        'npm' : '2306152191',
        'name': 'Luqmanul Hakim',
        'class': 'PBP D',
        'shop_entries': shop_entries
    }

    return render(request, "main.html", context)

def create_shop_entry(request):
    form = ShopEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_shop_entry.html", context)

def show_xml(request):
    data = shopEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = shopEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = shopEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = shopEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")