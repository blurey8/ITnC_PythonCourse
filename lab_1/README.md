# Tutorial 1 : IDLE & Input/Output

## Daftar Isi

- [Tutorial 1 : IDLE & Input/Output](#tutorial-1--idle--inputoutput)
  - [Daftar Isi](#daftar-isi)
  - [IDLE](#idle)
    - [Membuka IDLE](#membuka-idle)
    - [Membuat *file* kode Python](#membuat-file-kode-python)
    - [Menyimpan *file* program](#menyimpan-file-program)
    - [Menjalankan program](#menjalankan-program)
  - [Membuat program sederhana](#membuat-program-sederhana)
    - [Mencetak *(print)*](#mencetak-print)
    - [Meminta masukan *(input)*](#meminta-masukan-input)
  - [Dokumentasi](#dokumentasi)
  - [Latihan : Pesan Makanan](#latihan--pesan-makanan)



## IDLE

[**IDLE**][idle docs] adalah **I**ntegrated **D**evelopment and **L**earning **E**nvironment. Pada intinya, IDLE adalah tempat untuk mengembangkan program dengan bahasa Python yang telah disediakan oleh [**Python**][python org]. Dalam tutorial kali ini, kita akan mempelajari bagaimana menggunakan IDLE untuk membuat program sederhana.



### Membuka IDLE

- **Di Windows**
Untuk membuka IDLE, cukup klik **Start** dan masukkan `IDLE` pada *search field*, lalu pilih **IDLE (Python 3.x 64-bit/32-bit)**
![IDLE search](../images/lab01_01a.jpg)

- **Di OS berbasis Unix**
Buka **Terminal**, ketik `idle`, lalu tekan <kbd>Enter</kbd>. Jika sudah ada *file* `.desktop` untuk IDLE di Desktop Environment kalian, bisa juga mengikuti langkah yang serupa dengan di Windows.
![IDLE terminal](../images/lab01_01b.jpg)

Kemudian akan muncul *window* bernama *Python Shell* seperti di bawah ini.

![IDLE window](../images/lab01_02.jpg)

Kalian bisa langsung memberi perintah pemrograman di samping tanda `>>>`, seperti contoh berikut.

![A few statements](../images/lab01_03.jpg)



### Membuat *file* kode Python

Untuk membuat ***file*** (berkas) di IDLE, cukup klik **`File`** -> **`New File`** atau menggunakan *shortcut* <kbd>Ctrl</kbd> + <kbd>N</kbd>, seperti gambar di bawah.

![New file](../images/lab01_04.jpg)

Kemudian, akan muncul *file* kosong seperti berikut.

![Empty file](../images/lab01_05.jpg)

Di sini, kalian bisa memberikan instruksi pemrograman sama seperti di IDLE tadi. **Perbedaannya** adalah program kalian tidak akan langsung dijalankan saat membuat *file* dan harus dijalankan secara manual (akan dijelaskan nanti).

**Masukkan program di bawah ini ke dalam *file* yang kalian buat.**

```python
print("Halo!")
nama = "nama kalian"
print("Selamat Datang di ITnC" ,nama)
```



### Menyimpan *file* program

Untuk menjalankan *file* program, **simpan** terlebih dahulu *file*-nya dengan **`File` -> `Save`** atau <kbd>Ctrl</kbd> + <kbd>S</kbd>, lalu beri nama *file*-nya, lalu tekan **`Save`**.

![Save file](../images/lab01_06.jpg)

*File* kalian akan tersimpan dan dapat diakses di direktori penyimpanannya.



### Menjalankan program

Untuk **menjalankan program**, cukup klik **`Run` -> `Run Module`** atau tekan <kbd>F5</kbd>. Perlu diingat bahwa IDLE tidak akan menjalankan program jika *file* belum disimpan.



## Membuat program sederhana

Coba **buat** *file* baru yang berisi kode program berikut, kemudian jalankan.

```python
nama = input("Nama: ")
angkatan = int(input("Tahun Angkatan: "))

print("Hello,", nama, "angkatan", angkatan)
print("Selamat berjuang di Fasilkom!")
```



### Mencetak *(print)*

```python
print(something)
```

Fungsi `print` adalah perintah yang dapat digunakan untuk **mencetak** (menampilkan) teks ke dalam layar. Pada dasarnya, hampir semua data bisa dicetak ke layar menggunakan fungsi `print` ini.



### Meminta masukan *(input)*

```python
input(insert question text)
```

Ada kalanya kita memerlukan informasi dari luar, misalnya dari **pengguna** *(user)*. Untuk mendapatkan informasi tersebut, kita bisa menggunakan fungsi `input`.



## Dokumentasi

Terkadang kita kebingungan mengenai kegunaan suatu fungsi. Python sudah menyediakan **dokumentasi** mengenai hal tesebut. Dokumentasi dapat kalian akses dengan mengklik **Help** -> [**Python Docs**][python docs].

![Python docs](../images/lab01_10.jpg)

Atau, kalian juga bisa menggunakan fungsi `help(parameter)` di mana `parameter`nya merupakan fungsi atau objek yang ingin kalian cari tahu.

![help() demo](../images/lab01_11.jpg)

Atau, kalian juga bisa mencarinya di [**Google**][google] atau [**StackOverflow**][stackoverflow] jika kurang paham setelah membaca dokumentasi.

## Latihan : Pesan Makanan

Buatlah program yang dapat menampilkan output seperti berikut:

```
>>> [Order-Bot] Selamat datang di BudeMahal Fried Kitchen!
>>> Tekan <Enter> untuk melanjutkan...
>>> [Order-Bot] Mau pesan apa?
>>> Masukkan nama makanan: <nama_makanan>
>>> [User] Saya ingin memesan <nama_makanan>.
>>> Tekan <Enter> untuk melanjutkan...
>>> [Order-Bot] Berapa <nama makanan> yang ingin anda pesan?
>>> Masukkan jumlah makanan: <jumlah_makanan>
>>> [User] Saya pesan <jumlah_makanan> ya
>>> Tekan <Enter> untuk melanjutkan...
>>> [Order-Bot] Oke, pesanan <jumlah_makanan> <nama makanan> akan segera diantar ya. Silahkan menunggu.
```

---
<div style="text-align:center; font-size:20pt">"If you love technology, I don't understand why you're not coding."</div>
<br>
<div style="text-align:center; font-size:15pt">- Brina Lee, Instagram Engineer</b></div>


---
Ditulis oleh: [**blurey8**](https://github.com/blurey8)
Diadaptasi dari (dengan beberapa perubahan):
- [TarungLabDDP1/lab_instructions/lab01.md](https://github.com/laymonage/TarungLabDDP1/blob/master/lab_instructions/lab01.md) oleh [laymonage](https://github.com/laymonage)
- `lab01_ddp1_rev3.pdf` oleh **IF**, **SAT**, **KF**, dan **PDD**

[idle docs]: https://docs.python.org/3/library/idle.html
[python org]: https://python.org
[python docs]: https://docs.python.org
[google]: https://google.com
[stackoverflow]: https://stackoverflow.com