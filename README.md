# ShopKint

**Nama : Shabrina Aulia Kinanti**
**NPM : 2306245472**
**Kelas : B**
> **Shopkint:** http://shabrina-aulia31-shopkint.pbp.cs.ui.ac.id

## **Penjelasan Tugas**
<details>
<summary> <b> Tugas 2: Implementasi Model-View-Template (MVT) pada Django </b> </summary>

## **Checklist Tugas**
* ### Membuat proyek django baru
1. Membuat direktori baru yang bernama shopkint lalu jalankan virtual environment yang ditandai dengan (env)
2. Pada direktori shopkint buat file baru bertama `requirments.txt` dan tambahkan dependencies (komponen atau modul agar perangkat lunaknya berfungsi, termasuk library, framework dan package) yang berisi 

```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
3. Intalasi terhadap dependencies dengan `pip install -r requirements.txt`
4. Buat proyek baru dengan tulisan `django-admin startproject shopkint .` di terminal direktori yang tadi
5. Django berhasil dibuat

* ### Membuat aplikasi dengan nama main pada proyek shopkint
1. Membuat repositori baru di github
2. Membuat branch utama baru dengan tulisan `git branch -M main` di terminal direktori
3. Tulis `git remote add origin https://github.com/shabrinaulia/shopkint.git` di terminal untuk menghubungkan repositori lokal dengan repositori di GitHub
4. Lakukan `git push -u origin main.` untuk menyimpan ke github
5. Jalankan perintah python manage.py startapp main di terminal. Folder main akan terbuat sebagai branch dari folder utama
6. Tambahkan main di variabel `INSTALLED_APPS` pada file `setting.py` di direkotori utama

* ### Melakukan routing pada proyek agar dapat menjalankan aplikasi main
1. Membuat file `urls.py` di folder main, lalu isi dengan 
```
from django.urls import path
from main.views import show_main

app_name = `main`

urlpatterns = [
    path(`, show_main, name=`show_main`),
]
```
2. Buka file urls.py pada folder shopkint lalu impor fungsi include dari django.urls
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(`, include(`main.urls`)),
]
```

* ### Membuat model pada aplikasi main
1. Pada `models.py` di main saya mengubah attribute dan datatypenya serta limitasi penulisan data typenya sesuai dengan ketentuan tugas
``` 
from django.db import models

class MoodEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
```
2. Jalankan `python manage.py makemigrations` untuk memberikan migrasi pada model data lalu lakukan `python manage.py migrate` untuk mengaplikasikan perubahan model ke basis data

* ### Membuat sebuah fungsi pada views.py 
1. Tambahkan import render pada file `views.py` di folder main
2. Menambahkan fungsi show_main dibawah impor untuk mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai
3. Isi fungsinya dengan `context` yaitu dictionary yg berisi data
```
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        `name` : `Liptint`,
        `price`: `600.000`,
        `description`: `NEW Liptint with high formula`,
        `rating` : `4.5/5.0`
    }

    return render(request, "main.html", context)
```
4. Return dengan format `return render(request, "main.html", context)`

* ### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
1. Tulis code di file `urls.py` di folder main
```app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
2. Buka file `urls.py` di folder shopkint tambahkan `from django.urls import path, include`
3. Pada variabel urlpatterns isi dengan  `path('', include('main.urls')),`

* ### Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Buat project baru di PWS
2. Pada settings.py di folder shopkint pada variabel `ALLOWED_HOSTS` tambahkan `shabrina-aulia31-shopkint2.pbp.cs.ui.ac.id` 
3. Lakukan `git add, commit, push` ke github
4. Jalankan `git branch -M main`
5. Lalu jalankan `git push pws main:master`
6. Tunggu build lalu selesai

* ### Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
1. Buat file `README.md` 
2. Masukin link PWS
3. Jawab pertanyaannya

## **Bagan Request Client ke Web Aplikasi Django dan Responnya** 
![Bagan](images/bagan.jpeg)
Ketika Client (Browser/User) mengirimkan permintaan HTTP ke server, server tersebut memprosesnya dengan melakukan pemetaan URL melalui file urls.py. Setelah URL yang diminta ditemukan dan dipetakan, fungsi yang relevan dalam views.py dipanggil sesuai dengan permintaan URL tersebut. Fungsi tersebut kemudian mengembalikan respons HTTP dalam bentuk halaman HTML. Lalu, views.py akan mengambil data yang diperlukan dari models.py, lalu menyajikannya menggunakan template.


## **Fungsi Git dalam Pengembangan Perangkat Lunak**
Git adalah sistem kontrol versi yang digunakan untuk melacak perubahan dalam kode selama pengembangan perangkat lunak. Fungsinya yaitu 
menyimpan versi kode sebelumnya sehingga bisa kembali ke versi sebelumnya jika diperlukan, memungkinkan pengembang bekerja bersama pada
proyek yang sama tanpa konflik melalui fitur branching dan merging, memberikan penyimpanan aman bagi kode di repository, biasanya secara
remote.

## **Alasan Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak**
1. banyak fitur bawaan sehingga pengguna tidak perlu mencari atau mengkonfigurasi banyak library eksternal buat mendapatkan fitur" umum.
2. Memudahkan pengelolaan database tanpa perlu menulis SQL secara manual.
3. Memiliki komunitas yang besar dan aktif sehingga mudah untuk mencari bantuan untuk masalah para pengguna.

## **Mengapa Model pada Django Disebut sebagai ORM?**
Model pada Django disebut ORM karena memungkinkan pengembang 
berinteraksi dengan database menggunakan objek Python, bukan 
query SQL langsung. Setiap model merepresentasikan tabel dalam 
database, dan ORM dapat melakukan operasi database seperti query, 
insert, update, dan delete dengan metode python.
</details>

<details>
<summary> <b> Tugas 3: Implementasi Form dan Data Delivery pada Django </b> </summary>

## **Checklist Tugas**
## **Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Data delivery merupakan proses pengiriman data antar berbagai 
komponen sistem, baik antar server, antar aplikasi, maupun antara 
klien dan server. Data delivery menjadi esensial karena tanpa 
proses ini, komunikasi antara komponen-komponen dalam arsitektur 
sistem tidak dapat berlangsung dengan baik. Alasan kita 
memerlukan data delivery adalah:
1. Interoperabilitas: Berbagai layanan dan aplikasi perlu saling 
berbagi data untuk berfungsi dengan baik. Misalnya, API yang 
menghubungkan frontend dengan backend atau aplikasi yang 
berkomunikasi dengan layanan eksternal.
2. Akses Data: Data yang dihasilkan atau diminta oleh pengguna 
perlu dikirimkan dari server ke client atau sebaliknya untuk 
menyediakan informasi yang dibutuhkan, seperti hasil pencarian, 
produk yang ditampilkan, dll.
3. Scalability: Dalam arsitektur microservices, data delivery 
memungkinkan berbagai komponen bekerja secara terpisah dan 
i-host pada server yang berbeda, yang meningkatkan skalabilitas 
aplikasi.
4. Sinkronisasi Data: Data delivery memungkinkan sinkronisasi 
antara database, aplikasi, atau pengguna untuk memastikan data 
yang dilihat atau diubah konsisten di seluruh platform.

## **Manakah yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
JSON umumnya dianggap lebih baik dalam konteks pertukaran data ringan, aplikasi web modern, dan API, terutama karena kesederhanaan, kecepatan, dan efisiensinya. XML tetap relevan untuk skenario yang memerlukan struktur data yang lebih kompleks dan validasi data yang ketat. Namun, untuk sebagian besar aplikasi berbasis web dan komunikasi data antara klien dan server, JSON lebih populer dan sering menjadi pilihan utama karena kemudahannya dalam penggunaan dan performa yang lebih cepat.

## **Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
Method `is_valid()` dalam Django digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form sudah valid sesuai dengan aturan yang telah ditetapkan dalam form tersebut. Method ini penting karena memastikan bahwa data yang diterima sesuai dengan tipe dan format yang diharapkan, serta menangani kesalahan input pengguna dengan menyimpan data yang valid di `cleaned_data` dan memberikan pesan kesalahan pada atribut errors jika ada input yang tidak sesuai. Penggunaan `is_valid()` sangat krusial untuk mencegah bug dan error dalam aplikasi, menjaga keamanan dari serangan seperti injection atau XSS, serta memberikan pengalaman pengguna yang lebih baik dengan memberikan umpan balik atas kesalahan input. Validasi ini juga membantu memastikan bahwa hanya data yang valid dan aman yang diproses lebih lanjut oleh aplikasi.

## **Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
`{% csrf_token %}` adalah token yang berfungsi sebagai security. Token ini di-generate secara otomatis oleh Django untuk mencegah serangan berbahaya. Kita membutuhkan `csrf_token` saat membuat form di Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF), di mana penyerang mencoba melakukan tindakan berbahaya atas nama pengguna tanpa sepengetahuan mereka.Jika kita tidak menambahkan `csrf_token`, aplikasi akan rentan terhadap serangan CSRF, memungkinkan penyerang mengirimkan permintaan atas nama pengguna yang telah login, seperti mengubah data atau melakukan transaksi berbahaya, tanpa terdeteksi sebagai tindakan ilegal oleh server. Token ini penting untuk menjaga keamanan dan integritas aplikasi Django.

## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
* ### Pembuatan Form dan Validasi dengan is_valid()
1. Buat file baru `forms.py` lalu tambahkan code untuk membuat struktur form product
```
from django.forms import ModelForm
from main.models import ProductEntry

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["product_name", "price", "description", "rating"]
```
2. Pada file `views.py` di folder main tambahkan 
```
from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import ProductEntry
```
lalu buat fungsi baru bernama `create_product_entry` yang menerima request, tambahkan code ini 
```
def create_product_entry(request):
    form = MoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
3. Sesuaikan fungsi `show_main` di `views.py` menjadi
```
def show_main(request):
    mood_entries = MoodEntry.objects.all()
    context = {
        'name': 'Shabrina Aulia Kinanti',
        'npm' : '2306245472',
        'class': 'PBP B',
        'mood_entries': mood_entries
    }

    return render(request, "main.html", context)
```
4. Pada file `urls.py` saya menambahkan `from main.views import show_main, create_product_entry` lalu menambahkan path url di file `urls.py` bagian urlpatterns `path('create-product-entry', create_product_entry, name='create_product_entry'),`
5. Buat file HTML di bagian folder templates dengan nama `create_product_entry.html` berisi
```
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add New Product" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
6. Tambahkan code dibawah ini pada `main.html`serta tombol "Add New Product Entry" yang akan balik ke halaman form
```
{% if not product_entries %}
<p>Belum ada data mengenai produk yang dijual.</p>
{% else %}
<table>
  <tr>
    <th>Product Name</th>
    <th>Price</th>
    <th>Description</th>
    <th>Rating</th>
  </tr>

  {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini 
  {% endcomment %} 
  {% for product_entry in product_entries %}
  <tr>
    <td>{{product_entry.product_name}}</td>
    <td>{{product_entry.price}}</td>
    <td>{{product_entry.description}}</td>
    <td>{{product_entry.rating}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product</button>
</a>
{% endblock content %}
```

* ### Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
Menagembalikan Data dalam Bentuk XML dan JSOON
1. Buka file `views.py` lalu tambahkan
```
from django.http import HttpResponse
from django.core import serializers
```
2. Menambahkan fungsi `show_xml` yang akan mengembalikan `HttpResponse` berisi data yang sudah menjadi XML
```
def show_xml(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
Lalu tambahkan fungsi `show_json` yang akan mengembalikan
`HttpResponse` berisi data yang sudah menjadi JSON
```
def show_json(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

Mengembalikan Data dalam Bentuk XML dan JSON Berdasarkan ID
1. Pada file `views.py` tambahkan fungsi `show_xml_by_id`yang akan mengembalikan `HttpResponse` berisi data yang sudah menjadi XML berdasarkan ID
```
def show_xml_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
Lalu tambahkan fungsi `show_json_by_id`yang akan mengembalikan `HttpResponse` berisi data yang sudah menjadi JSON berdasarkan ID
```
def show_json_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
* ### Membuat Routing URL pada Masing-Masing Views yang Telah Ditambahkan
1. Membuat routing URL setiap path di dalam `urlpatterns` menghubungkan URL yang spesifik dengan fungsi view tertentu sehingga bisa ditampilkan dalam format yang diminta (XML atau JSON) di `urls.py` yang berisi :
```
from django.urls import path
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```
2. Jalanakan proyek dengan `python manage.py runserver` lalu buka `http://localhost:8000/xml/[id]/` atau json untuk melihat proyek yang sudah dibuat

## **Screenshot Hasil Akses URL pada Postman** 
1. XML
![xml](images/xml.png)
2. JSON
![json](images/json.png)
3. XML by ID
![xml](images/xml[id].png)
4. JSON by ID
![json](images/json[id].png)

</details>

<details>
<summary> <b> Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django </b> </summary>

## **Checklist Tugas**
## **Apa perbedaan antara HttpResponseRedirect() dan redirect()**
HttpResponseRedirect() adalah sebuah kelas yang digunakan untuk melakukan redirect secara manual ke URL tertentu. redirect() adalah shortcut yang lebih mudah digunakan, karena bisa menerima URL, nama view, atau objek sebagai argumen.

## **Jelaskan cara kerja penghubungan model Product dengan User!**
Model Product memiliki ForeignKey yang menghubungkannya dengan model User, memungkinkan setiap produk untuk dimiliki oleh satu pengguna. Dengan ini, produk bisa ditautkan secara spesifik kepada pengguna yang terdaftar di aplikasi.

## **Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**
Authentication adalah proses memverifikasi identitas pengguna (contohnya, memeriksa apakah username dan password benar). Authorization adalah proses menentukan apakah pengguna yang sudah di-authenticate memiliki izin untuk mengakses sumber daya tertentu. Saat pengguna login, yang dilakukan adalah authentication, yaitu memastikan pengguna terdaftar dengan kredensial yang benar. Django menggunakan middleware untuk mengelola session dan cookies guna mengingat status login pengguna.

## **Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**
Django mengingat pengguna yang telah login menggunakan session framework, dengan menyimpan session ID unik sebagai cookie di browser pengguna. Cookies juga digunakan untuk menyimpan preferensi pengguna dan melacak aktivitas mereka. Untuk menjaga keamanan, cookies sebaiknya diberi flag HttpOnly dan secure agar tidak mudah diakses oleh skrip atau koneksi yang tidak aman. Penggunaan cookies secara default dapat aman jika developer mengikuti praktik terbaik. Namun, pengunaan cookie juga tetap memilki risiko potensial seperti :
1. Cross-Site Scripting (XSS): Serangan XSS dapat memungkinkan pencurian cookies dari pengguna jika tidak ada validasi input yang baik.
2. Cross-Site Request Forgery (CSRF): Serangan CSRF dapat memungkinkan pihak ketiga untuk membuat request yang berbahaya atas nama pengguna. Django sudah menyertakan perlindungan CSRF secara default.
3. Session Hijacking: Jika cookie tidak dienkripsi dengan baik, sesi pengguna bisa dicuri oleh pihak ketiga.

## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)**
* ### Mengimplementasikan fungsi registrasi, login, dan logout
1. Tambahkan import `UserCreationForm` dan `messages` pada file `views.py` di folder main
```
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```
2. Tambahkan fungsi `register` masih di file yang sama 
```
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
3. Membuat file baru bernama `register.html` di folder main bagian templates yang berisikan
```
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
4. Menambahkan import fungsi register dan juga path urlnya di file `urls.py`
```
from main.views import register
...
 urlpatterns = [
     ...
     path('register/', register, name='register'),
 ]
```

**login**
5. Saya membuat view login_user di `views.py` menggunakan AuthenticationForm dan metode authenticate serta login dari Django
```
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)
```
6. Membuat file `login.html` di folder main/templates berisi 
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
7. Menambahkan import di file `urls.py` seperti `from main.views import login_user` dan menambahkan path nya dalam `urlpatterns` serperti `path('login/', login_user, name='login'),`

**logout**
8. Menambahkan import `logout` di `views.py` dengan fungsi logout `from django.contrib.auth import logout` lalu tambahkan fungsi 
``` 
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
9. Tambahkan potongan kode di file `main.html`
```
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```
10. Menambahkan import di file `urls.py` seperti `from main.views import logout_user` dan menambahkan path nya dalam `urlpatterns` serperti `path('logout/', logout_user, name='logout'),`

* ### Menghubungkan model Product dengan User
1. Buka file `models.py` terus tambahkan import code `from django.contrib.auth.models import User` llau di class `ProductEntry` tambahin `user = models.ForeignKey(User, on_delete=models.CASCADE)`
2. Lalu tambahkan code ini di fungsi `create_product_entry` di file `views.py`
```
def create_mood_entry(request):
    form = MoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        mood_entry = form.save(commit=False)
        mood_entry.user = request.user
        mood_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_mood_entry.html", context)
```
3. Ubah value dr `product_entries` dan `context` di fungsi `shoe_main` lalu nanti di migrate
```
def show_main(request):
    product_entries = ProductEntry.objects.filter(user=request.user)

    context = {
         'name': request.user.username,
    }
```
4. Lalu seetelah itu tamabahin import os di `settings.py`trs ganti variabel debug nya jadi 
```
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```

* ### Pengelolaan Sesi dengan Cookies
1. Setelah login, saya menambahkan cookie last_login untuk menyimpan data waktu terakhir login. Pada file `views.py` bagian login_user, saya mengubah response untuk menyertakan cookie
```
from django.http import HttpResponseRedirect
import datetime

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
```
2. Di file `views.py` pada bagian `show_main`, saya menambahkan context untuk menampilkan last_login dari cookies
```
def show_main(request):
    context = {
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'Unknown')
    }
    return render(request, 'main.html', context)
```

* ### Keamanan Cookies
1. Saya memastikan bahwa cookie disetel dengan atribut `HttpOnly` dan `Secure` jika menggunakan HTTPS
```
response.set_cookie('last_login', str(datetime.datetime.now()), httponly=True, secure=True)
```
2. Lalu mengecek untuk memastikan cookie tidak dapat diakses oleh JavaScript dan hanya dikirim melalui koneksi HTTPS.

</details>

<details>
<summary> <b> Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS </b> </summary>

## **Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**
1. Inline Style (prioritas tertinggi): CSS yang ditulis langsung pada atribut style di elemen HTML. Contoh : `<p style="color: red;">Teks ini berwarna merah.</p>`
2. ID Selector: Selector yang menggunakan ID dari elemen. Contoh: `#main { color: blue; }`
3. Class Selector, Attribute Selector, dan Pseudo-Class Selector: Selector yang menggunakan class, atribut, atau pseudo-class seperti :hover. Contoh: 
```
.text { font-size: 16px; }
[type="text"] { color: green; }
p:hover { font-weight: bold; }
```
4. Element Selector dan Pseudo-Element Selector: Selector yang hanya menggunakan tag HTML seperti <p>, <div>, atau pseudo-element seperti ::before. Contoh: `p { margin: 20px; }`

## **Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**
Responsive design adalah konsep dalam pengembangan web yang memastikan bahwa tampilan dan layout situs web dapat menyesuaikan dengan baik pada berbagai ukuran layar dan perangkat, mulai dari desktop hingga perangkat mobile. Responsive design penting karena:
1. Pengalaman Pengguna (User Experience): Pengguna dapat melihat dan mengakses konten dengan nyaman tanpa perlu zoom in/out atau scroll ke samping.
2. SEO (Search Engine Optimization): Google dan mesin pencari lain memprioritaskan situs web yang responsif karena mereka memberikan pengalaman pengguna yang lebih baik.
3. Aksesibilitas: Situs web dapat diakses di berbagai perangkat seperti smartphone, tablet, dan komputer, sehingga meningkatkan jangkauan pengunjung.

Aplikasi yang menerapkan responsive design :
- Google.com: Memiliki tampilan yang konsisten dan mudah digunakan pada semua ukuran layar.
- Medium.com: Mengatur tata letak teks dan gambar agar nyaman dibaca baik di layar kecil maupun besar.

Aplikasi yang belum menerapkan responsive design :
- ZARA : website ZARA sering kali dikritik karena navigasi yang rumit dan tidak intuitif, terutama pada perangkat mobile.
- eBay : Teks dan elemen UI terkadang terlihat terlalu kecil, dan beberapa tombol tidak berfungsi dengan baik di layar kecil​

## **Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**
1. Margin: Jarak antara elemen dengan elemen di sekitarnya. Margin berfungsi untuk memberi ruang di luar border elemen tersebut
```
.element {
  margin: 20px; /* Menambahkan jarak 20px di luar elemen */
}
```
2. Border: Garis tepi yang mengelilingi elemen. Border memisahkan padding dan margin dari elemen.
```
.element {
  border: 2px solid black; /* Border tebal 2px berwarna hitam */
}
```
3. Padding: Ruang di dalam elemen, antara konten (teks/gambar) dan border elemen.
```
.element {
  padding: 15px; /* Menambahkan ruang 15px di dalam elemen */
}
```
**Contoh Implementasi Margin, Border, dan Padding**
```
<div style="margin: 20px; border: 2px solid black; padding: 15px;">
  Ini adalah contoh elemen dengan margin, border, dan padding.
</div>
```

## **Jelaskan konsep flex box dan grid layout beserta kegunaannya!**
- Flexbox adalah model layout satu dimensi (searah horizontal atau vertikal) yang memungkinkan Anda mengatur tata letak dan distribusi elemen di dalam container dengan fleksibel. Flexbox memudahkan pengaturan alignment (perataan), direction (arah), dan spacing (jarak antar elemen). Kegunaan Flexbox ideal untuk membuat layout yang fleksibel dan responsif seperti navbar, form, atau elemen grid sederhana. Contoh implementasi :
```
.container {
  display: flex;
  justify-content: space-between;
}
```

- Grid Layout adalah model layout dua dimensi yang memungkinkan Anda untuk membagi halaman menjadi kolom dan baris. Grid layout lebih cocok untuk membuat layout yang kompleks seperti dashboard atau halaman dengan beberapa section. Kegunaan Grid layout memungkinkan untuk pengaturan yang lebih kompleks dan terstruktur, seperti layout magazine atau layout card. Contoh implementasi :
```
.grid-container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  gap: 20px;
}
```

## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**
* ### Implementasi fungsi menghapus dan mengedit
1. Tambahkan code dibawah ini di file `views.py`
```
def edit_mood(request, id):
    # Get mood entry berdasarkan id
    mood = MoodEntry.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = MoodEntryForm(request.POST or None, instance=mood)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_mood.html", context)
```
2. Buat file baru di main/templates bernama `edit_product.html` lalau isi dengan code dibawah
```
{% extends 'base.html' %}

{% load static %}

{% block content %}

<h1>Edit Mood</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Mood"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
3. Import `edit_mood` di `urls.py` jangan lupa juga untuk menambahkan pathnya
**hapus**
1. Tambahkan fungsi `delete_mood` di `views.py`
```
def delete_mood(request, id):
    # Get mood berdasarkan id
    mood = MoodEntry.objects.get(pk = id)
    # Hapus mood
    mood.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
```
2. Import `delet_mood` dan tambahkan path url nya juga 
3. Di `main.html` tambahkan button yang bisa mengedit dan menghapusnya
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
```

* ### Kustomisasi halaman login, register dan tambah product
1. Saya menggunkan tailwind sehingga tambahin dulu tailwind ke aplikasinya di base.html
```
<head>
{% block meta %}
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
{% endblock meta %}
<script src="https://cdn.tailwindcss.com">
</script>
</head>
```
2. Membuat file `login.html` untuk melakukan stylingnya
```
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<!-- Container Utama dengan Background dan Flexbox -->
<div class="min-h-screen flex items-center justify-center w-screen bg-gradient-to-r from-[#EFE9E1] to-[#AC9C8D] relative">
  <!-- Bagian Kiri: Form Login -->
  <div class="flex flex-col justify-center items-center p-8 bg-white shadow-lg rounded-lg z-10 max-w-md w-full">
    <h2 class="mt-2 mb-4 text-3xl font-extrabold text-gray-800">
      Login to your account
    </h2>
    <form class="mt-8 space-y-6 w-full" method="POST" action="">
      {% csrf_token %}
      <div class="space-y-4">
        <div>
          <label for="username" class="sr-only">Username</label>
          <input id="username" name="username" type="text" required class="appearance-none block w-full px-3 py-2 border border-gray-300 placeholder-gray-400 text-gray-800 rounded-md focus:outline-none focus:ring-2 focus:ring-[#322D29] focus:border-transparent" placeholder="Username">
        </div>
        <div>
          <label for="password" class="sr-only">Password</label>
          <input id="password" name="password" type="password" required class="appearance-none block w-full px-3 py-2 border border-gray-300 placeholder-gray-400 text-gray-800 rounded-md focus:outline-none focus:ring-2 focus:ring-[#322D29] focus:border-transparent" placeholder="Password">
        </div>
      </div>
      <!-- Tombol Login -->
      <div>
        <button type="submit" class="w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#72383D] hover:bg-[#AC9C8D] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#322D29] transition duration-150 ease-in-out">
          Sign in
        </button>
      </div>
    </form>
    <!-- Pesan Kesalahan -->
    {% if messages %}
    <div class="mt-4 w-full">
      {% for message in messages %}
      <div class="p-4 rounded-md {{ message.tags }} bg-red-100 border border-red-400 text-red-700">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}
    <!-- Link ke Register -->
    <div class="text-center mt-4">
      <p class="text-sm text-[#322D29]">
        Don't have an account yet?
        <a href="{% url 'main:register' %}" class="font-medium text-[#72383D] hover:text-[#AC9C8D]">
          Register Now
        </a>
      </p>
    </div>
  </div>
  
  <!-- Bagian Kanan: Background Gambar -->
  <div class="hidden md:block md:w-1/2 h-screen absolute right-0 top-0">
    <img src="{% static 'images/bg-login.png' %}" alt="bg-login" class="w-full h-full object-cover rounded-l-lg shadow-lg">
  </div>
</div>
{% endblock content %}
```
3. Untuk register juga sama membuat file baru bernama `register.html` di main/templates/ Setelah pengguna berhasil mendaftar, redirect ke halaman login.
4. Menambah product pertama-tama desain form untuk menambah produk agar terlihat lebih menarik, Tambahkan input untuk meng-upload gambar produk dan pastikan tampil di preview sebelum disimpan.

* ### Kustomisasi Halaman Daftar Produk
1. Ubah tampilan daftar produk menggunakan card untuk setiap produk. Setiap card harus memiliki:
Gambar produk
Nama produk
Deskripsi produk
Dua tombol untuk edit dan delete produk.
2. Jika tidak ada produk, tampilkan pesan yang menyatakan bahwa tidak ada produk yang terdaftar dan sertakan gambar sedih (misalnya, icon).
3. Memastikan semua elemen dapat menyesuaikan ukuran layar, baik di desktop maupun mobile.

* ### Membuat dua button untuk mengedit dan menghapus
1. Menambahkan dua button
```
<div class="flex space-x-2">
  <a href="{% url 'main:edit_product' product_entry.pk %}" class="w-full text-center bg-[#72383D] hover:bg-[#AC9C8B] text-white py-1 px-2 rounded-md transition duration-200 text-xs"> <!-- Kurangi padding tombol -->
      Edit
  </a>
  <a href="{% url 'main:delete_product' product_entry.pk %}" class="w-full text-center bg-red-500 hover:bg-red-600 text-white py-1 px-2 rounded-md transition duration-200 text-xs"> <!-- Kurangi padding tombol -->
      Delete
  </a>
</div>
```

* ### Membuat Navigation Bar
1. Membuat navigation bar yang responsif untuk desktop dan juga mobile
```
{% load static %}

<!-- Navbar Utama: Gabungan Logo, Search Bar, Menu Items, Welcome, dan Logout -->
<nav class="bg-white shadow-md fixed top-0 left-0 z-40 w-screen border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
            <!-- Logo -->
            <div class="flex items-center">
                <a href="#">
                    <img src="{% static 'images/shopkint-logo.png' %}" alt="Shopkint Logo" class="h-14 w-auto">
                </a>
            </div>
            <!-- Search Bar -->
            <div class="hidden md:block flex-grow mx-4">
                <div class="relative">
                    <input type="text" placeholder="Search..." class="w-full bg-gray-100 border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:ring-2 focus:ring-[#72383D] focus:border-transparent">
                    <span class="absolute inset-y-0 right-0 flex items-center pr-3">
                        <svg class="h-5 w-5 text-gray-400" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                            <path d="M21 21l-4.35-4.35m0 0A7.5 7.5 0 1116.5 3.5a7.5 7.5 0 010 15z"></path>
                        </svg>
                    </span>
                </div>
            </div>
            <!-- Menu Items -->
            <div class="hidden md:flex items-center space-x-8">
                <a href="{% url 'main:show_main' %}" class="text-gray-600 hover:text-[#72383D] px-3 py-2 text-sm font-medium">Home</a>
                <a href="{% url 'main:show_main' %}" class="text-gray-600 hover:text-[#72383D] px-3 py-2 text-sm font-medium">Products</a>
                <a href="{% url 'main:show_main' %}" class="text-gray-600 hover:text-[#72383D] px-3 py-2 text-sm font-medium">Brands</a>
                <a href="{% url 'main:show_main' %}" class="text-gray-600 hover:text-[#72383D] px-3 py-2 text-sm font-medium">Categories</a>
            </div>
            <!-- Welcome Message and Logout for Desktop -->
            <div class="hidden md:flex items-center space-x-8 ml-16"> <!-- Menambahkan margin left (ml-16) untuk jarak antara Categories dan Welcome -->
                <span class="text-gray-600 flex items-center">Welcome, <span class="font-semibold text-[#72383D] ml-2">{{ user.username }}</span></span>
                <a href="{% url 'main:logout' %}" class="text-center text-[#7E102C] border border-[#7E102C] hover:bg-[#7E102C] hover:text-white rounded-md px-4 py-2 text-sm font-medium">
                    Logout
                </a>
            </div>
            <!-- Hamburger menu button for Mobile -->
            <div class="md:hidden flex items-center">
                <button class="mobile-menu-button focus:outline-none">
                    <svg class="w-6 h-6 text-gray-500" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                        <path d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>
        </div>
    </div>
</nav>

<!-- Mobile Menu yang muncul ketika Hamburger ditekan -->
<div class="mobile-menu hidden md:hidden px-4 w-full bg-white border-t border-gray-200 fixed top-16 shadow-lg z-40 h-auto max-h-[70vh] overflow-y-auto">
    <div class="pt-2 pb-3 space-y-1 mx-auto">
        <a href="#" class="block text-gray-600 px-3 py-2 rounded-md text-base font-medium hover:bg-gray-100">Home</a>
        <a href="#" class="block text-gray-600 px-3 py-2 rounded-md text-base font-medium hover:bg-gray-100">Products</a>
        <a href="#" class="block text-gray-600 px-3 py-2 rounded-md text-base font-medium hover:bg-gray-100">Brands</a>
        <a href="#" class="block text-gray-600 px-3 py-2 rounded-md text-base font-medium hover:bg-gray-100">Categories</a>
        <!-- Welcome Message and Logout for Mobile -->
        <div class="mt-4 border-t border-gray-200 pt-4">
            <span class="block text-gray-600">Welcome, <span class="font-semibold" style="color: #7E102C;">{{ user.username }}</span></span>
            <a href="{% url 'main:logout' %}" class="block text-center text-[#7E102C] border border-[#7E102C] hover:bg-[#7E102C] hover:text-white rounded-md px-4 py-2 text-sm font-medium mt-4">
                Logout
            </a>
        </div>
    </div>
</div>

<!-- Script untuk Toggle Menu Mobile -->
<script>
    // Toggle Mobile Menu
    const btn = document.querySelector("button.mobile-menu-button");
    const menu = document.querySelector(".mobile-menu");

    btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
    });
</script>
```

</details>

<details>
<summary> <b> Tugas 6: JavaScript dan AJAX </b> </summary>

## **Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!**
1. Interaktivitas dinamis: Memungkinkan perubahan konten tanpa reload.
2. AJAX: Mendukung pengambilan dan pengiriman data tanpa memuat ulang halaman.
3. Validasi input di frontend: Mengurangi kesalahan input sebelum data dikirim ke server.
4. Integrasi API: Menghubungkan aplikasi dengan layanan eksternal.

## **Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?**
await digunakan untuk menunggu hasil dari operasi asynchronous seperti fetch() sebelum melanjutkan ke eksekusi kode berikutnya. fetch() mengembalikan sebuah promise yang mewakili operasi jaringan (HTTP request), dan await memastikan bahwa kita mendapatkan hasil dari promise tersebut (entah itu respons atau error) sebelum melanjutkan kode. Jika await tidak digunakan, JavaScript akan melanjutkan eksekusi kode berikutnya tanpa menunggu hasil dari fetch(). Akibatnya, variabel yang diharapkan berisi respons dari fetch() hanya akan berupa promise yang belum diselesaikan (pending), dan jika kita mencoba menggunakan datanya, bisa menyebabkan error atau output yang tidak diinginkan.

## **Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?**
csrf_exempt digunakan untuk menonaktifkan validasi CSRF di view tertentu, seperti pada permintaan POST AJAX, yang mungkin tidak menyertakan CSRF token. Jika tidak digunakan, permintaan POST tanpa token ini akan ditolak oleh server untuk alasan keamanan.

## **Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?**
Pembersihan data di backend tetap diperlukan karena:
1. Keamanan: Mencegah manipulasi data oleh pengguna dan melindungi dari serangan seperti SQL Injection dan XSS.
2. Integritas Data: Backend memastikan data sesuai aturan dan konsisten.
3. Akses Non-browser: API atau aplikasi eksternal juga bisa mengirimkan data, jadi backend harus tetap memvalidasi.
4. Lapisan Perlindungan: Backend jadi perlindungan terakhir jika validasi frontend gagal.
Pembersihan data tidak cukup dilakukan di frontend saja karena frontend bisa dimanipulasi oleh pengguna, misalnya dengan menonaktifkan JavaScript atau memodifikasi validasi. Ini membuat input tidak aman dan rentan terhadap serangan seperti SQL Injection atau XSS, yang hanya bisa ditangani di backend. Selain itu, data bisa datang dari aplikasi non-browser atau API, sehingga validasi frontend tidak relevan. Backend selalu menjadi lapisan terakhir yang dapat dipercaya untuk memastikan semua data yang diterima valid dan sesuai aturan.

## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**
* ### Membuat Fungsi untuk Menambahkan Produk dengan AJAX
1. Pada file `views.py` tambahkan code berikut ini 
```
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    product_name = strip_tags(request.POST.get("product_name"))
    price = strip_tags(request.POST.get("price"))
    description = request.POST.get("description")
    rating = request.POST.get("rating")

    # Ambil gambar dari request.FILES
    image = request.FILES.get("image")
    user = request.user

    # Simpan entri produk baru
    new_product = ProductEntry(
        product_name=product_name,
        price=price,
        description=description,
        rating=rating,
        image=image,  # Gambar dari request.FILES
        user=user
    )
    new_product.save()

    # Kirim response dalam bentuk JSON yang bisa digunakan oleh JavaScript
    response_data = {
        "product_name": new_product.product_name,
        "price": new_product.price,
        "description": new_product.description,
        "rating": new_product.rating,
        "image": new_product.image.url if new_product.image else None  # URL gambar
    }

    return HttpResponse(b"CREATED", status=201)
```
2. Jangan lupa untuk merouting fungsi tersebut di `urls.py`
```
from main.views import ..., add_product_entry_ajax
urlpatterns = [
    ...
    path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
]
```

* ### Menampilkan Data Mood Entry dengan fetch() API
1. Mengubah baris pertama show_json dan show_xml di `views.py` menjadi 
```
data = Productntry.objects.filter(user=request.user)
```
2. Menambhakan implementasi modal pada `main.html`
```
 async function getProductEntries(){
      return fetch("{% url 'main:show_json' %}").then((res) => res.json())
    }

    async function refreshProductEntries() {
        document.getElementById("product_entry_cards").innerHTML = "";
        document.getElementById("product_entry_cards").className = "";
        const productEntries = await getProductEntries();
        let htmlString = "";
        let classNameString = "";

        if (productEntries.length === 0) {
            classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
            htmlString = `
                <div class="text-center">
                    <img src="{% static 'images/cart-empty.png' %}" alt="No Products" class="mx-auto mb-5 w-1/6">
                    <p class="text-gray-500 text-lg">There are no products on ShopKint</p>
                </div>`;
        } else {
            classNameString = "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4"; // Grid layout
            productEntries.forEach((item) => {
                const product_name = DOMPurify.sanitize(item.fields.product_name);
                const price = DOMPurify.sanitize(item.fields.price);
                const description = DOMPurify.sanitize(item.fields.description);
                const rating = item.fields.rating;
                const image = item.fields.image ? `<img src="../../media/${item.fields.image}" alt="${product_name}" class="object-contain max-h-full max-w-full"> ` : `<span class="text-gray-500">No Image Available</span>`;
                htmlString += `
                <!-- Product Card -->
                <div class="bg-white border rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300 p-4">
                    <!-- Product Image -->
                    <div class="h-36 bg-gray-100 flex items-center justify-center overflow-hidden mb-2">
                        ${image}
                    </div>
                    <!-- Product Information -->
                    <div class="p-2">
                        <div class="flex justify-between items-center mb-1">
                            <h3 class="text-base font-bold text-gray-800">${product_name}</h3>
                            <span class="text-base text-[#72383D] font-semibold">$${price}</span>
                        </div>
                        <p class="text-sm text-gray-500 mb-1">${description}</p>
                        
                        <!-- Product Rating -->
                        <div class="flex items-center mb-2">
                            <span class="flex items-center text-yellow-500">
                                ${[...Array(rating)].map(() => `
                                <svg class="w-3 h-3" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.2 3.674a1 1 0 00.95.69h3.862c.969 0 1.371 1.24.588 1.81l-3.122 2.223a1 1 0 00-.364 1.118l1.2 3.674c.3.921-.755 1.688-1.54 1.118l-3.122-2.223a1 1 0 00-1.176 0l-3.122 2.223c-.784.57-1.838-.197-1.54-1.118l1.2-3.674a1 1 0 00-.364-1.118L2.76 9.101c-.783-.57-.38-1.81.588-1.81h3.861a1 1 0 00.951-.69l1.2-3.674z"/>
                                </svg>`).join('')}
                            </span>
                            <span class="ml-1 text-xs text-gray-500">(${rating})</span>
                        </div>
                        
                        <!-- Action Buttons -->
                        <div class="flex space-x-2">
                            <a href="/edit-product/${item.pk}" class="w-full text-center bg-[#72383D] hover:bg-[#AC9C8B] text-white py-1 px-2 rounded-md transition duration-200 text-xs">Edit</a>
                            <a href="/delete-product/${item.pk}" class="w-full text-center bg-red-500 hover:bg-red-600 text-white py-1 px-2 rounded-md transition duration-200 text-xs">Delete</a>
                        </div>
                    </div>
                </div>`;
            });
        }
        
        document.getElementById("product_entry_cards").className = classNameString;
        document.getElementById("product_entry_cards").innerHTML = htmlString;
    }
    refreshProductEntries();
```

* ### Membuat Modal Sebagai Form untuk Menambahkan Produk
1. Menambahkan kode berikut untuk mengimplementasikan modal (Tailwind) pada aplikasi saya
```
<div class="max-w-5xl mx-auto lg rounded-lg p-4"> <!-- Kurangi padding untuk container utama -->
    <div class="flex justify-between items-center mb-4">
        <h2 class="text-xl font-semibold text-[#72383D]">Product List</h2> <!-- Kurangi ukuran font -->
        <a href="{% url 'main:create_product_entry' %}" class="bg-[#AC9C8B] hover:bg-[#72383D] text-white font-bold py-1 px-3 rounded-md transition duration-200 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
            Add Product
        </a>
        <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="bg-[#AC9C8B] hover:bg-[#72383D] text-white font-bold py-1 px-3 rounded-md transition duration-200 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
            Add New Product Entry by AJAX
          </button>
    </div>

    <div id="product_entry_cards"></div>
    <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
        <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
          <!-- Modal header -->
          <div class="flex items-center justify-between p-4 border-b rounded-t">
            <h3 class="text-xl font-semibold text-gray-900">
              Add New Product Entry
            </h3>
            <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
              <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
              </svg>
              <span class="sr-only">Close modal</span>
            </button>
          </div>
          <!-- Modal body -->
          <div class="px-6 py-4 space-y-6 form-style">
            <form id="productEntryForm" enctype="multipart/form-data">
              <div class="mb-4">
                <label for="product_name" class="block text-sm font-medium text-gray-700">Product Name</label>
                <input type="text" id="product_name" name="product_name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter product name" required>
              </div>
              <div class="mb-4">
                <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
                <input type="number" id="price" name="price" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter product price" required>
              </div>
              <div class="mb-4">
                <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                <textarea id="description" name="description" rows="3" class="mt-1 block w-full resize-none border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter product description" required></textarea>
              </div>
              <div class="mb-4">
                <label for="rating" class="block text-sm font-medium text-gray-700">Rating (1-5)</label>
                <input type="number" id="rating" name="rating" min="1" max="5" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" required>
              </div>
              <div class="mb-4">
                <label for="image" class="block text-sm font-medium text-gray-700">Image</label>
                <input type="file" id="image" name="image" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700">
              </div>
            </form>
          </div>
          <!-- Modal footer -->
          <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
            <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
            <button type="submit" id="submitProductEntry" form="productEntryForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
          </div>
        </div>
    </div>

    <div class="bg-white shadow-lg rounded-lg p-2 mb-3 mx-auto max-w-4xl">
        <!-- Membuat elemen-elemen card menyamping dengan flexbox -->
        <div class="flex justify-center space-x-2 mt-3 items-center">
            {% include "card_info.html" with title='NPM' value=npm %}
            {% include "card_info.html" with title='Name' value=name %}
            {% include "card_info.html" with title='Class' value=class %}
        </div>
        <div class="mt-6 w-full flex justify-center">
            <p class="text-gray-600 text-sm text-center bg-gray-100 rounded-lg px-4 py-2 shadow-md">
                <span class="font-semibold">Last Login: </span>{{ last_login }}
            </p>
        </div>
    </div>
```

* ### Menambahkan Data Produk dengan AJAX
1. Membuat fungsi `addProductEntry` pada `main.html` 
```
function addProductEntry() {
        fetch("{% url 'main:add_product_entry_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#productEntryForm')),
        })
        .then(response => {
            refreshProductEntries();
            document.getElementById("productEntryForm").reset(); 
            hideModal();  // Tambahkan ini untuk menutup modal setelah produk berhasil ditambahkan
        })
        .catch(error => {
            console.error("Error adding product:", error);
        });
        return false;
    }
```
2. lalu jangan lupa untuk menambahkan event listener untuk ngejalanin fungsi `addProductEntry()`
```
document.getElementById("moodEntryForm").addEventListener("submit", (e) => {
    e.preventDefault();
    addProductEntry();
  })
```
