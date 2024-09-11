# Lufor
### e-commerce
Luqmanul Hakim (2306152191)<br>
PBP D

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
2. Daftarkan aplikasi `main` kedalam setting.py di direktori lufor_shop

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
5. Menghubungkan view dan template dengan buka berkas view.py di main dan tambahkan fungsi show main
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
8. Jalankan proyek Django dengan perintah python `manage.py` runserver
9. Bukalah http://localhost:8000/ di peramban web

##### Melakukan Deployment ke PWS
1. Buat proyek baru bernama luforshop
2. Tambahkan URL PWS pada ALLOWED HOSTS
3. Lakukan git add, commit, push

### Bagan yang berisi request client ke web aplikasi berbasis Django
![Bagan](https://github.com/lhakiim/lufor-shop/blob/main/Bagan_request_client.png)

### Fungsi Git dalam Pengembangan Perangkat Lunak

### Alasan Framework Django dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak

### Mengapa Model pada Django disebut sebagai ORM?
