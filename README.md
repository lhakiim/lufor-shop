# Lufor
### e-commerce
Luqmanul Hakim (2306152191)<br>
PBP D

PWS : [Lufor-Shop](http://luqmanul-hakim31-luforshop.pbp.cs.ui.ac.id/)
---
- [Tugas2](#Tugas-2)
- [Tugas3](#Tugas-3)
# Tugas 2
### Langkah-langkah Implementasi
##### Membuat Django baru
1. Membuat directori baru bernama lufor-shop dengan perintah
```
mkdir lufor-shop 
cd lufor-shop
```
2. Mengaktifkan Virtual Environment dengan menjalankan perintah berikut pada terminal.
```
python -m venv env
env\Scripts\activate
```
3. Membuat berkas `requirements.txt` dan menambahkan beberapa dependencies.
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
4. Install dependencies dengan requirements.txt
```
pip install -r requirements.txt
```
5. Membuat project django bernama `lufor_shop`
```
django-admin startproject lufor_shop .
```
6. Tambahkan ALLOWED_HOSTS di settings.py

##### Aplakasi Django dan Konfigurasi
1.  Membuat aplikasi `main` dalam lufor-shop
```
python manage.py startapp main
```
2. Daftarkan aplikasi `main` kedalam `setting.py` di direktori lufor_shop

3. Buka models.py dan isi dengan
```
from django.db import models

class shopEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    descriptions = models.TextField()
```
4. Membuat migrasi model dengan
```
python manage.py makemigrations
```
5. Menghubungkan view dan template dengan buka berkas `view.py` di main dan tambahkan fungsi show main
6. Konfigurasi url aplikasi `main` dengan membuat berkas `urls.py` dalam direktori main dan isi dengan kode:
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
7. Menambahkan rute URL proyek untuk menghubungkannya ke tampilan `main`. Impor fungsi
```
from django.urls import path, include
```
dan tambahkan urlpatterns
```
urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
```
8. Jalankan proyek Django dengan perintah `python manage.py runserver`
9. Bukalah http://localhost:8000/ di peramban web

##### Melakukan Deployment ke PWS
1. Buat proyek baru bernama luforshop
2. Tambahkan URL PWS pada ALLOWED HOSTS
3. Lakukan git add, commit, push

### Bagan yang berisi request client ke web aplikasi berbasis Django
![Bagan](https://github.com/lhakiim/lufor-shop/blob/main/Bagan_request_client.png)

### Fungsi Git dalam Pengembangan Perangkat Lunak
Git berfungsi sebagai sistem kontrol versi terdistribusi. Git memungkinkan kita untuk melacak setiap perubahan yang dilakukan. Git memungkinkan kita untuk berkolaborasi tim dan dapat bekerja di branch masing-masing sehingga tidak mengganggu tim lainnya.

### Alasan Framework Django dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak
Django digunakan sebagai permulaan dalam belajar karena mudah untuk dipelajari. Mulai dari bahasa yang digunakan yaitu bahasa phyton. Kesederhanaan dari django ini memudahkan bagi pemula untuk memahami konsep-konsep yang ada. 

### Mengapa Model pada Django disebut sebagai ORM?
Model django disebut sebagai ORM(Object-Relational Mapping) karena ia menggunakan ini untuk memetakan objek-objek Pyhton ke dalam tabel-tabel database. Dengan adanya ORM, antarmuka menjadi lebih mudah digunakan untuk memanipulasi data dalam database.

---

# Tugas 3

### Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery sangat penting dalam pengimplementasian sebuah platform. Hal ini karena ia memungkinkan kita untuk mengirim dan menerima data dari user dan platform. Ia juga memastikan bahwa data yang dikirim tetap akurat, efisien dan cepat sehingga menjaga kualitas informasi dan meningkatkan pengalaman dari pengguna platform.
### Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON dan XML merupakan representasi data yang digunakan pada pertukaran data antaraplikasi. Menurut saya JSON lebih baik. Hal ini karena JSON memiliki beberapa keunggulan yaitu JSON memiliki format yang sederhana. JSON memiliki sintaks yang lebih padat dan lebih mudah ditulis dan dibaca oleh manusia. Format pada JSON adalah menggunakan key and value, dibandingkan dengan XML yang memerlukan banyak tag sehingga JSON menjadi lebih efisien dan lebih cepat. 
### Fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi `is_valid()` digunakan untuk memvalidasi input dari form sebelum diproses lagi. Fungsi ini berguna untuk memastikan semua field yang dimasukkan sesuai dengan ketentuan sehingga membantu menjaga kebenaran data.
### Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` merupakan token yang berfungsi sebagai security. Token ini di-generate secara otomatis oleh django untuk menjaga keamanan dari serangan berbahaya. Ia dapat memverifikasi bahwa permintaan berasal dari sumber yang sah dan aman. Apabila token ini tidak ada maka form akan menjadi rentan terhadap serangan CSRF(Cross-Site Request Forgery). Penyerang dapat membuat permintaan jahat dan dapat mengubah data pengguna bahkan mengakses data sensitif tanpa izin.
###  Cara kamu mengimplementasikan checklist di atas secara step-by-step
#### Membuat Form Input Data
1. Membuat direktori templates yang berisikan  `base.html` yang digunakan sebagai template dasar web
2. Membuat berkas `forms.py` pada direktori main
```python
from django.forms import ModelForm
from main.models import shopEntry

class ShopEntryForm(ModelForm):
    class Meta:
        model = shopEntry
        fields = ["name", "price", "descriptions"]
```
3. Menambahkan import pada `views.py` pada direktori main dan membuat fungsi baru untuk membuat produk
```python
from django.shortcuts import render, redirect
from main.forms import MoodEntryForm
from main.models import MoodEntry
```
```python
def create_shop_entry(request):
    form = ShopEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_shop_entry.html", context)
```
4. Menambahkan urlspattern dan import pada `urls.py`
5. Membuat berkas HTML Baru `creat_shop_entry` pada main/templates
6. Tambahkan kode untuk menampilkan data shop pada `main.html`
----
#### Membuat 4 Fungsi Views dan routing URL-nya
```python
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
```
```python
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-shop-entry', create_shop_entry, name='create_shop_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```
---
#### Hasil URL pada Postman
- XML
![XML](https://github.com/user-attachments/assets/06d72c7e-304b-4824-b121-5a9e924ac1be)
- JSON
![JSON](https://github.com/user-attachments/assets/8309ea26-be2b-4e98-8e02-4b121005085a)
- XML By ID
![XML_by_ID](https://github.com/user-attachments/assets/7eaefb77-0899-4147-8bfa-a53d459b92be)
- JSON By ID
![JSON_by_ID](https://github.com/user-attachments/assets/0265c1a1-ff64-4cc4-b707-a601a71f95f2)
