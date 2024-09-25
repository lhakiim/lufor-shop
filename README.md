# Lufor
### e-commerce
Luqmanul Hakim (2306152191)<br>
PBP D

PWS : [Lufor-Shop](http://luqmanul-hakim31-luforshop.pbp.cs.ui.ac.id/)
---
- [Tugas2](#Tugas-2)
- [Tugas3](#Tugas-3)
- [Tugas4](#Tugas-4)
# Tugas 2
<details>
<summary>Tugas 2</summary>

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
</details>

# Tugas 3

<details>

<summary>Tugas 3</summary>

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

</details>

# Tugas 4

### Perbedaan antara HttpResponseRedirect() dan redirect()
- `HttpResponseRedirect()` merupakan class dasar django yang digunakan untuk membuat respon dengan kode 302 (sementara) yang mengarahkan pengguna ke halaman url tertentu
- `redirect()` merupakan fungsi modul `django.shortcuts` yang secara implisit membungkus `HttpResponseRedirect`. `redirect()` lebih praktis dan fleksibel dalam menerima argumen karena selain dapat menerima url ia juga dapat menerima model, view, dan nama url.
### Cara kerja penghubungan model Product dengan User
Setiap model `Product` dihubungkan/dikaitkan dengan user menggunakan `ForeginKey`. Setiap user dapat memiliki banyak product tetapi satu product hanya dapat dimiliki oleh satu `User`.
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut!
Authentication dan Authorization merupakan dua konsep keamanan dengan peran yang berbeda. 
- Authentication<br>
Proses verifikasi identitas pengguna. Pengguna memasukkan kredensial seperti username dan password yang kemudian dicocokkan dengan data yang tersimpan pada database.

- Authorization<br>
Proses menentukan hak akses pengguna setelah terautentikasi. Setelah login, sistem memeriksa peran dari pengguna untuk menentukan tingkat hak aksesnya.<br>

**Proses saat login**<br>
Pengguna memasukkan kredensial dan kemudian akan diverifikasi. Jika kredensial valid, pengguna akan dianggap terautentikasi dan pengguna mendapatkan hak akses berdasarkan perannya. <br>
**Implementasi di Django** <br>
Django menyimpan data pengguna yang telah terautentikasi di objek sebagai `request.user`. Otorasi django dikelola dengan permission dan group pada model dan view.
### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
- Saat pengguna login, Django membuat session pengguna dan menyimpan di dalam cookies. 
- Saat request selanjutnya, cookies session inilah yang akan dikirimkan kembali ke server. 
- Cookies ini menyimpan kredensial dan aktivitas pengguna. Kemudian data di cookies ini yang akan memnentukan kevalidan data.<br>
**Kegunaan lain cookies**
- Menyimpan preferensi pengguna
- Pelacakan aktivitas pengguna<br>
Tidak semua Cookies aman untuk digunakan. Cookies yang tidak terenkripsi mereka rentan terhadap seragan. Jadi, jangan menyimpan data informasi secara langsung dicookies untuk menjaga data kita.

###  Cara kamu mengimplementasikan checklist di atas secara step-by-step
1. Membuat `UserCreationForm` yang berguna untuk mendaftarkan pengguna. Tambahkan fungsi register pada `views.py`.
```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
2. Tambahkan berkas HTML baru yaitu `register.html` untuk menampilkan form registrasi
3. **Login** Tambahkan fungsi login_user pada `views.py` kemudian buat template HTML login.html untuk menampilkan form login
4. **Logout** Tambahkan fungsi logout_user pada `views.py` kemudian tambahkan Hyperlink logout pada main.html
5. Tambahkan cookie last_login pada login_user
```python
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```
6. Tambahkan context baru pada show_main dan tambahkan cookie last login pada logout_user
```python
'last_login': request.COOKIES['last_login']
```
7. Tambahkan output lastlogin pada main.html
8. Hubungkan shopEntry dengan user
```python
class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
9. Setelah semuanya dilakukan lakukan migrasi
```python
python manage.py makemigrations
python manage.py migrate
```