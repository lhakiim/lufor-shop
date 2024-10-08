# Lufor
### e-commerce
Luqmanul Hakim (2306152191)<br>
PBP D

PWS : [Lufor-Shop](http://luqmanul-hakim31-luforshop.pbp.cs.ui.ac.id/)
---
- [Tugas2](#Tugas-2)
- [Tugas3](#Tugas-3)
- [Tugas4](#Tugas-4)
- [Tugas5](#Tugas-5)
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
<details>
<summary>Tugas 4</summary>
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
</details>

# Tugas 5
<details>
<summary>Tugas 5</summary>

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
- Inline Styles: memiliki prioritas tertinggi karena style didefinisikan secara langsung di dalam atribut `style`.
- ID Selector : Didefinisikan dengan (#) contoh `#header`
- Class Selector : misalnya .myclass :hover
- Tag Selector : contohnya p , div, h1
- Universal selector : contoh
    ```
    * {
    color: black;
    }
    ```

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
<br>
Responsive design menjadi konsep penting dala pengembangan web dikarenakan ia memungkinkan web untuk beradaptasi dengan berbagai ukuran layar dan perangkat seperti laptop dan smartphone<br>
Kegunaan <br>
- Peningkatan penggunaan diberbagai device : karena memiliki bentuk yang fleksibel diberbagai device<br>
- Penglaman pengguna yang lebih baik
<br>
Contoh aplikasi yang sudah menerapkan responsive design seperti aplikasi instagram, facebook dll. Sedangkan aplikasi yagn belum menerapkan responsive design adalah scele 2015 dan siakng.


### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin : Ruang diluar elemen yang  mengatur elemen tersebut dengan elemen lainnya. Margin terletah di luar elemen div
  ```
  div {
    margin: 30px;
  }
  ```

- Border : Garis disekitar elemen yang membatasi area elemen.
    ```
    div {
    border: 2px solid black;
    }
    ```
- Padding : Ruang yang didalam elemen, antara konten elemen dan border. Jika sebuah elemen memiliki teks atau gambar, padding memberikan ruang antara teks dan gambar.
    ```
    div {
    padding: 20px;
    }
    ```
    ![Padding](https://github.com/user-attachments/assets/07b964bd-dfcf-4f48-9a2e-4943ebae2eee)

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
- Flexbox : merupakan sistem letak desain untuk mendeskripsikan baris atau kolom yang sangat berguna dalam pendesaian karena menjadi lebih responsif, fleksibel, dan dapat beradaptasi dengan ukuran lauar. Flexbox lebih cocok digunakan pada layout yang sederhana seperti 1 dimensi
- Grid : merupakan sistem tata letak yang lebih kompleks daripada flexbox. Grid dapat diatur baris dan kolomnya sehingga lebih fleksibel dan dapat digunakan secara 2 dimensi yang memiliki banyak kolom dan baris. Sehingga grid ini cocok untuk membuat layout halaman, dashboard dll.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

1. Edit dan remove product
<br>
membuat method untuk edit dan remove product
``` python
def edit_shop(request, id):
    # Get mood entry berdasarkan id
    shop = shopEntry.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = ShopEntryForm(request.POST or None, instance=shop)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_shop.html", context)
```
``` python
def delete_shop(request, id):
    # Get mood berdasarkan id
    shop = shopEntry.objects.get(pk = id)
    # Hapus mood
    shop.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
```
2. Buatlah html baru dengan nama edit_shop untuk edit product
3. Menambahkan url pattern pada urls.py
4. tambahkan button edit dan hapus pada main.html
```
...
<tr>
    ...
    <td>
        <a href="{% url 'main:edit_mood' mood_entry.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
    <td>
        <a href="{% url 'main:delete_mood' mood_entry.pk %}">
            <button>
                Delete
            </button>
        </a>
    </td>
</tr>
...
```
5. Buat navbar yang dapat fleksibel terhadap berbagai ukuran seperti desktop dan smartphone.
6. Kustomisasi desain menggunakan Tailwind pada setiap bagian seperti, login, register, main, add product, card info dan card product.<br><br>
</details>
---


# Tugas 6

### Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
- Membuat Web menjadi lebih menarik
  Java script dapat membuat web menjadi lebih menarik dengan konten-konten dinamisnya. Ia dapat mengupdate page tanpa perlu dilakukan reload.
- Menjalankan Web server
  Javascript dapat berjalan di sisi server dengan adanya `node.js` sehingga dapat menjalankan aplikasi dan situs web berbasis browser.
- Mudah untuk digunakan dan dipelajari
  Javascript memiliki sintaks yang lebih singkat dan sederhana sehingga mudah untuk dipelajari
- Pengalaman pengguna yang lebih baik
  Pada javascript pengolahan dapat terjadi pada sisi pengguna (client side) sehingga dapat merespons tindakan pengguna lebih cepat tanpa harus bergantung pada server.
- Memiliki komunitas dan ekosistem yang besar
  Dengan banyaknya framework, library kita dapat menjadi lebih terbantu dalam pengembangan aplikasi web. Selain itu, komunitasnya yang besar dapat membantu mencari solusi apabila terjadi bug atau masalah.

### Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Fungsi `await` digunakan untuk menunggu proses pengambilan data dari dari server sebelumnya untuk melanjutkan melakukan eksekusi berikutnya. Apabila tidak terdapat `await` ketika menggunakan fetch() kode akan melanjutkan eksekusi tanpa menunggu sehingga berkemungkinan tidak dapat mengakses hasil dari fetch() karena masih dalam keadaan pending.

### Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
`csrf_exempt` membuat Django tidak perlu untuk mengecek keberadaan dari `csrf_token` pada POST request yang dikirimkan. Dekorator ini akan mengecualikan view dari `csrf_token` sehingga memungkinkan untuk permintaan AJAX POST berjalan tanpa adanya `csrf_token`.

### Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
- Keamanan
  Validasi di frontend bisa dengan mudah diabaikan dan diubah oleh pengguna sehingga pengguna dapat memanipulasi kode javascript untuk mengirimkan permintaan secara langsung kepada server tanpa dilakukannya validasi. Pembersihan data yang dilakukan pada backend ini berguna untuk memastikan data tetap aman dan bersih.
- Mengatasi pengguna yang menonaktifkan javascript
  Jika validasi dilakukan pada frontend dan pengguna menonaktifkan javascript pada browser mereka maka ia dapat mengirimkan input yang tidak divalidasi keserver yang menyebabkan potensi keamanan dan kesalahan data.  

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

#### Ubahlah kode cards data mood agar dapat mendukung AJAX GET dan pengambilan data mood menggunakan AJAX GET.
Tambahkan sebuah fungsi baru pada `views.py` untuk add product
```python
@csrf_exempt
@require_POST
def add_shop_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    descriptions = strip_tags(request.POST.get("descriptions"))
    price = request.POST.get("price")
    user = request.user

    new_shop = shopEntry(
        name=name, descriptions=descriptions,
        price=price,
        user=user
    )
    new_shop.save()

    return HttpResponse(b"CREATED", status=201)
```
tambahkan juga routing urlnya
```python
urlpatterns = [
    ...
    path('create-shop-entry-ajax', add_shop_entry_ajax, name='add_sho[_entry_ajax'),
]
```

#### Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood.
Buat tombol pada `main.html` dibawah `shop_entry_card`
```html
<div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out bg-opacity-50 backdrop-filter backdrop-blur-md ">
      <div id="crudModalContent" class="relative bg-white rounded-3xl shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
        <!-- Modal header -->
        <div class="flex items-center justify-between p-4 border-b rounded-t-3xl bg-white">
          <h3 class="text-xl font-semibold text-gray-900">
            Add New Shop Entry
          </h3>
          <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
            <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
            </svg>
            <span class="sr-only">Close modal</span>
          </button>
        </div>
    ...
```

#### Buatlah fungsi view baru untuk menambahkan product baru ke dalam basis data.
Fungsi untuk menambahkan product dengan ajax. Apabila input valid maka ia akan otomatis refresh untuk menambah product dan langsung menutup ajax.
```js
function addShopEntry() {
    fetch("{% url 'main:add_shop_entry_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#shopEntryForm')),
    })
    .then(response => refreshShopEntries())
    hideModal();
    document.getElementById("shopEntryForm").reset(); 
    document.querySelector("[data-modal-toggle='crudModal']").click();
    return false;
  }

  document.getElementById("shopEntryForm").addEventListener("submit", (e) => {
    e.preventDefault();
    addShopEntry();
    
  })
```

#### Lakukan refresh halaman untuk menampilkan data product

```js
<script>
    async function getShopEntries(){
        return fetch("{% url 'main:show_json' %}").then((res) => res.json())
    }
    async function refreshShopEntries() {
...
</script>
```