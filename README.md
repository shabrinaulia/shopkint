# ShopKint

**Nama : Shabrina Aulia Kinanti**
**NPM : 2306245472**
**Kelas : B**
> **Shopkint:** http://shabrina-aulia31-shopkint2.pbp.cs.ui.ac.id

## **Penjelasan Tugas**
<summary> <b> Tugas 2: Implementasi Model-View-Template (MVT) pada Django </b> </summary>

## **Checklist Tugas**
* ### Membuat proyek django baru
1. Membuat direktori baru yang bernama shopkint lalu jalankan virtual environment yang ditandai dengan (env)
2. Pada direktori shopkint buat file baru bertama 'requirments.txt' dan tambahkan dependencies (komponen atau modul agar perangkat lunaknya berfungsi, termasuk library, framework dan package) yang berisi 

```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
3. Intalasi terhadap dependencies dengan 'pip install -r requirements.txt'
4. Buat proyek baru dengan tulisan 'django-admin startproject shopkint .' di terminal direktori yang tadi
5. Django berhasil dibuat

* ### Membuat aplikasi dengan nama main pada proyek shopkint
1. Membuat repositori baru di github
2. Membuat branch utama baru dengan tulisan 'git branch -M main' di terminal direktori
3. Tulis 'git remote add origin https://github.com/shabrinaulia/shopkint.git' di terminal untuk menghubungkan repositori lokal dengan repositori di GitHub
4. Lakukan 'git push -u origin main.' untuk menyimpan ke github
5. Jalankan perintah python manage.py startapp main di terminal. Folder main akan terbuat sebagai branch dari folder utama
6. Tambahkan main di variabel 'INSTALLED_APPS' pada file 'setting.py' di direkotori utama

* ### Melakukan routing pada proyek agar dapat menjalankan aplikasi main
1. Membuat file 'urls.py' di folder main, lalu isi dengan 
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
2. Buka file urls.py pada folder shopkint lalu impor fungsi include dari django.urls
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
]
```

* ### Membuat model pada aplikasi main
1. Pada 'models.py' di main saya mengubah attribute dan datatypenya serta limitasi penulisan data typenya sesuai dengan ketentuan tugas
``` 
from django.db import models

class MoodEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
```
2. Jalankan 'python manage.py makemigrations' untuk memberikan migrasi pada model data lalu lakukan 'python manage.py migrate' untuk mengaplikasikan perubahan model ke basis data

* ### Membuat sebuah fungsi pada views.py 
1. Tambahkan import render pada file 'views.py' di folder main
2. Menambahkan fungsi show_main dibawah impor untuk mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai
```
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Liptint',
        'price': '600.000',
        'description': 'NEW Liptint with high formula',
        'rating' : '4.5/5.0'
    }

    return render(request, "main.html", context)
```
3. Isi fungsinya dengan 'context' yaitu dictionary yg berisi data
4. Return dengan format 'return render(request, "main.html", context)'

* ### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
1. Tulis code app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
] di file urls.py di folder main
2. Buka file urls.py di folder shopkint tambahkan from django.urls import path, include
3. Pada variabel urlpatterns isi dengan  path('', include('main.urls')),

* ### Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Buat project baru di PWS
2. Pada settings.py di folder shopkint pada variabel 'ALLOWED_HOSTS' tambahkan 'shabrina-aulia31-shopkint2.pbp.cs.ui.ac.id' 
3. Lakukan 'git add, commit, push' ke github
4. Jalankan 'git branch -M main'
5. Lalu jalankan 'git push pws main:master'
6. Tunggu build lalu selesai

* ### Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
1. Buat file 'README.md' 
2. Masukin link PWS
3. Jawab pertanyaannya

## **Bagan Request Client ke Web Aplikasi Django dan Responnya** 
![Bagan](images/bagan.png)
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
Model pada Django disebut ORM karena memungkinkan pengembang berinteraksi dengan database menggunakan objek Python, bukan query SQL
langsung. Setiap model merepresentasikan tabel dalam database, dan ORM dapat melakukan operasi database seperti query, insert, update, dan 
delete dengan metode python.