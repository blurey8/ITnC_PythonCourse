# Tutorial 0 : < Judul Tutorial >

## Daftar Isi

- [Tutorial 1 : Program Sederhana](#tutorial-1--program-sederhana)
  - [Daftar Isi](#daftar-isi)
  - [IDLE](#idle)
    - [Membuka IDLE](#membuka-idle)
    - [Membuat *file* kode Python](#membuat-file-kode-python)
    - [Menyimpan *module* python](#menyimpan-module-python)
    - [Menjalankan program](#menjalankan-program)
  - [Membuat program sederhana](#membuat-program-sederhana)
    - [Meminta masukan *(input)*](#meminta-masukan-input)
      - [Assignment](#assignment)
      - [Konversi](#konversi)
    - [Mencetak keluaran *(print)*](#mencetak-keluaran-print)
  - [Tambahan](#tambahan)
    - [Errors](#errors)
    - [Syntax](#syntax)
    - [Whitespace](#whitespace)
    - [Continuation](#continuation)
    - [Comments](#comments)
    - [Dokumentasi](#dokumentasi)
  - [Latihan : *Profit Calculator*](#latihan--profit-calculator)
  - [Tugas : *Circle Area & Perimeter*](#tugas--circle-area--perimeter)
    - [Deskripsi Soal](#deskripsi-soal)
      - [Contoh](#contoh)
      - [Hint](#hint)
    - [Bonus](#bonus)
    - [Komponen penilaian](#komponen-penilaian)


## Identifiers

Identifier adalah nama yang diberikan kepada variable, modules, fungsi, dll.
> Kita akan mempelajari modules dan fungsi di lab-lab berikutnya

Setiap identifier hanya boleh terdiri dari huruf, angka dan underscore `_`. Namun, identifier tidak boleh diawali oleh angka.
Identifier itu *case sensitive* (huruf kecil dan besar berbeda) dan tidak memiliki batasan jumlah karakter.

Masing-masing identifier berikut valid dan berbeda satu sama lainnya:
- smanitra61
- Spam
- spam
- spAm
- Spam_and_Eggs
- Spam_And_Eggs

#### Naming Conventions

Cara standar dalam menulis variable di Python adalah huruf kecil dengan underscore (*snake_case*).
- nilai_ujian
- kelas_ipa_7

Identifier harus memiliki makna. Berilah nama variable **harga**, jangan hanya **h**.

#### Reserved Words

Ada identifier yang merupakan bagian dari bahasa Python sehingga tidak dapat digunakan sebagai variable, dll. Inilah yang disebut *reserved words*.

Berikut daftar lengkap *reserved words* di Python3:

|        |          |         |          |        |
| ------ | -------- | ------- | -------- | ------ |
| False  | class    | finally | is       | return |
| None   | continue | for     | lambda   | try    |
| True   | def      | from    | nonlocal | while  |
| and    | del      | global  | not      | with   |
| as     | elif     | if      | or       | yield  |
| assert | else     | import  | pass     |        |
| break  | except   | in      | raise    |        |

### Variable

*Variable* adalah bagian dari memori komputer yang diberikan **nama** untuk merepresentasikan suatu objek dalam program. 
Misalnya variable dengan nama `jumlah` memiliki nilai 30. Berarti, nama `jumlah` merepesentasikan nilai 30.

#### Assignment

Untuk memasangkan suatu nilai dengan variable, lakukan *assignment*.

```py
>>> jumlah = 30 # artinya nilai 30 dihubungkan dengan variable jumlah
>>> jumlah
30
>>> keuntungan = (5000-1000) * 3 # artinya hasil operasi di sebelah kanan dihubungkan dengan variable keuntungan
>>> keuntungan
12000
```

#### Tipe Data

Variable tidak hanya dapat menampung nilai yang berbentuk angka saja, tetapi bisa juga tulisan dan tipe-tipe lainnya.
Berikut tipe-tipe data yang ada di python dan contohnya:

- Integers (int): **5**
- Floats (float): **1.2**
- Booleans (bool): **True** atau **False**
- Strings (str): **"ini tulisan"** atau **'Ini juga tulisan'**
- Lists (list): **['a', 1, 1.3]**
- tipe data lain akan dipelajari nanti

Di Python, kita tidak perlu mendefinisikan tipe data dari sebuah variable. Tipe data sebuah variable juga dapat berubah.

```py
>>> var = 5     # Variable di python tidak perlu didefinisikan apa tipe datanya
>>> type(var)   # Tipe data suatu variable mengikuti tipe data dari isinya
<class 'int'>
>>> type(5)
<class 'int'>

>>> var = 2.5
>>> type(var)   # Tipe data suatu variable dapat berubah
<class 'float'>

>>> var = "bravo"
>>> type(var)
<class 'str'>
```

Tipe data pada variable berfungsi untuk menentukan operasi apa yang dapat dilakukan oleh variable tersebut. Misalkan `'ini tulisan'.capitalize()` adalah method yang bisa dilakukan pada *strings*, tetapi tidak pada *integers*.

#### Konversi Tipe Data

*to be continued...*

<!-- TODO: lanjutkanP -->

---

## Latihan : *< Judul Latihan >*

< spesifikasi program >

**contoh:**
```
< contoh simulasi program 1 >
```
```
< contoh simulasi program 2 >
```
```
< contoh simulasi program 3 >
```
**Hint:** < info yang membantu >

---

## Tugas : *< Judul Tugas >*

### Deskripsi Soal

< Cerita soal >

< Spesifikasi soal >

#### Contoh

```
< contoh simulasi program 1 >
```
```
< contoh simulasi program 2 >
```
```
< contoh simulasi program 3 >
```

#### Hint

< info yang membantu >

### Bonus

< tambahan spesifikasi untuk menambah nilai>

### Komponen penilaian

[ ] Hasil output (95)
[ ] < Penilaian lainnya > (xx)
[ ] < Penilaian lainnya > (xx)
[ ] Kerapihan kode (5)
[ ] Bonus (10)
<!-- Penilaian bebas, ini hanya contoh -->
<!-- Max nilai 110 -->

---

<!-- quote -->
<div style="text-align:center; font-size:20pt">"Berilah anak-anak kita kutipan menginspirasi. Biar keren."</div>
<br>
<div style="text-align:center; font-size:15pt">- Saya, Bukan Siapa-siapa</b></div>

---

Ditulis oleh: [**< nama mu >**](https://link.github/sosmed-lain)
Referensi:
- `fprog17-01.pdf` oleh **L. Y. Stefanus**
- [`lab01.md`](https://github.com/laymonage/TarungLabDDP1/blob/master/lab_instructions/lab01.md) oleh [**laymonage**](https://github.com/laymonage)
- < referensi lain>
- Referensi ini hanya contoh