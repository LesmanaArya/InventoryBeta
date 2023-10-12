from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from main.forms import ItemForm
from django.urls import reverse
from .models import Item
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required(login_url='/login')
def home(request):
    all_items = Item.objects.all().filter(user=request.user).order_by('name').values() #Urutkan berdasarkan nama item
    total_item = Item.objects.count() #Mendapatkan total objek yang ada

    total_amount = 0
    list_nama_item = []

    for obj in Item.objects.all():
        total_amount += obj.amount #Mendapatkan total amount dari seluruh objek yang ada
        list_nama_item.append(obj.name)

    context = {
        'name': request.user.username,
        'kelas': "PBP F",
        'npm': 2206081603,
        'all': all_items, 
        'total_item': total_item,
        'total_amount': total_amount,
        'last_login': request.COOKIES['last_login'],
        'list_nama_item': list_nama_item
    }
    return render(request, 'home.html', context)  # Render isi dari data Item kita ke file home.html


def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
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


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kamu berhasil membuat akun!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_time = datetime.datetime.now()
            response = HttpResponseRedirect(reverse("main:home")) 
            response.set_cookie('last_login', current_time.strftime("%c")) #Menampilkan last login dengan format Hari-Bulan-Tanggal-Jam-Tahun
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


def increement_amount(request, id):
    updated_item = Item.objects.get(pk=id) #Ambil objek berdasarkan id
    updated_item.amount += 1 #Tambahkan nilai value sebanyak 1
    updated_item.save() #Save nilai yang baru
    return HttpResponseRedirect(reverse('main:home'))


def decreement_amount(request, id):
    updated_item = Item.objects.get(pk=id) #Ambil objek berdasarkan id
    if updated_item.amount > 0:
        updated_item.amount -= 1 #Kurangkan nilai value sebanyak 1 jika amount > 0
        updated_item.save()
    else:
        messages.error(request, f'Jumlah dari {updated_item.name} sudah 0') #Tampilkan pesan error jika amount yang ingin dikurang sudah 0
    return HttpResponseRedirect(reverse('main:home'))


def delete_item(request, id):
    deleted_item = Item.objects.get(pk=id)
    deleted_item.delete() #Delete item dengan id yang didapat
    return HttpResponseRedirect(reverse('main:home'))


def edit_product(request, id):
    # Get product berdasarkan ID
    get_item = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ItemForm(request.POST or None, instance=get_item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:home'))

    context = {'form': form}
    return render(request, "edit_product.html", context)



def get_product_json(request):
    product_item = Item.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))


@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        effect = request.POST.get("effect")
        value = request.POST.get("value")
        user = request.user

        new_product = Item(name=name, amount=amount, description=description, effect=effect, value=value,user=user)
        new_product.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

