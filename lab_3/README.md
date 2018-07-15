# Tutorial 2 : Percabangan / Seleksi

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


## Selection

*Selection* (seleksi) adalah bagaimana program membuat suatu pilihan berdasarkan data yang ada. Hal ini lah, yang membuat program "menjadi" pintar.
Salah satu cara seleksi pada Python adalah dengan menggunakan **if-statement**.

### Boolean Expressions

*Boolean Expression* mempunyai nilai **True** atau **False**. Boolean expression digunakan sebagai kondisi untuk menentukan alur dari seleksi atau repetisi. Jika kondisi True, lakukan suatu hal, jika kondisi False, lakukan hal lainnya.

> Boolean berasal dari nama [George Boole](https://en.wikipedia.org/wiki/George_Boole), seorang ahli matematika, filsuf, dan ahli logika asal Inggris. Terkenal dengan bukunya The Laws of Thought (1854) yang berisi aljabar Boolean di dalamnya.

Python menyediakan tipe data yang dapat menampung nilai True atau False yang bernama **bool type**.

Contoh boolean expression:
```py
>>> x = 10
>>> x > 5
True

>>> y = 11
>>> 1 < y < 5
False
```

Boolean expression dibentuk menggunakan operator relasi.

| Python | Math | Deskripsi                    |
| ------ | ---- | ---------------------------- |
| <      | <    | Kurang dari                  |
| <=     | ≤    | Kurang dari atau sama dengan |
| ==     | =    | Sama dengan                  |
| >=     | >    | Lebih dari                   |
| >      | ≥    | Lebih dari atau sama dengan  |
| !=     | ≠    | Tidak sama dengan            |

> Pada Python, `==` menyatakan persamaan, `=` menyatakan assignment.

### If Statement (One-way Decisions)

```py
if <condition> :
    <body>
```
`condition` berisi boolean expression
`body` berisi sebuah statement atau lebih yang berada di bawah `if` dan posisinya di-indentasi.

- Jika `condition` bernilai **True**, maka statement pada `body` akan dijalankan. 
- Jika `condition` bernilai **False**, maka statement pada `body` akan dilewati (tidak dijalankan).

Setelah itu, program akan berlanjut pada statement selanjutnya di luar if statement.

> Perhatikan masalah indentasi karena berpengaruh pada program. Indentasi dapat dilakukan dengan tab maupun 4 spasi tetapi dalam sebuah program cara indentasinya harus seragam.

Contoh:

```py
suhu = 25

if suhu < 30:
    print("Brr... dingin euy!")
if suhu > 50:
    print("Tolong saya meleleh.")
```

> Apa yang terjadi jika `suhu = 30` ?

### If-else Statement (Two-way Decisions)

```py
if <condition> :
    <body-1>
else:
    <body-2>
```

`if-else` statement mirip seperti `if` statement, tetapi jika `condition` bernilai False, statement pada `body-2` yang akan dijalankan.

```py
nilai = 80

if (nilai >= 75) :
    print("Selamat! Kamu lulus.")
else:
    print("Maaf, anda kurang be...lajar.")
```


### If-elif-else Statement (Multi-way Decisions)

```py
if <condition-1> :
    <case-1 statements>
elif <condition-2>
    <case-2 statements>
elif <condition-3>
    <case-3 statements>
...
else:
    <default statements>
```

> `elif` merupakan singkatan dari `else if`

Python mengecek kondisi secara berurutan dari atas ke bawah. Jika ditemukan kondisi yang bernilai True, maka blok statements yang berada di bawah kondisi tersebut akan dijalankan. Kemudian berlanjut ke statement di luar `if-elif-else` statement.
Jika kondisi tidak ada yang bernilai True, maka statement di bawah else yang akan dijalankan.

```py
ritcher = 5.7

if (ritcher >= 8.0):
    report = "Banyak bangunan rata dengan tanah"
elif (ritcher >= 7.0):
    report = "Banyak bangunan hancur"
elif (ritcher >= 6.0):
    report = "Banyak bangunan rusak"
elif (ritcher >= 4.5):
    report = "Sedikit bangunan rusak"
elif (ritcher >= 3.5):
    report = "Tidak ada kerusakan"
elif (ritcher >= 0):
    report = "Tidak terasa oleh manusia"
else:
    report = "Bilangan negatif tidak valid"

print(report)
```

## Tambahan

<!-- TODO: Complete this -->

### (More) Boolean Expression

#### True dan False di Python

#### Setara vs Sama

#### Assignment berantai

#### Truth Tables

#### Presedensi

---

## Latihan : *Number to Letter Score*

Buatlah program yang dapat mengkonversi nilai dalam bentuk angka ke bentuk huruf.

| Angka  | Huruf |
| ------ | :---: |
| 85-100 | A     |
| 80-85  | A-    |
| 75-80  | B+    |
| 70-75  | B     |
| 65-70  | B-    |
| 55-65  | C     |
| 45-55  | D     |
| 0-45   | E     |

> Range angka **exclusive end**

Jika input angka di luar range yang diberikan, print pesan error buatan kalian sendiri.

**contoh:**
```
Masukkan nilai angka: 73

Nilai huruf kamu adalah: B
```
```
Masukkan nilai angka: 80

Nilai huruf kamu adalah: A-
```
```
Masukkan nilai angka: 105

Wah, ambis kamu ya.
```
**Hint:** Tidak ada.

---

## Tugas : *< Judul Tugas >*

### Deskripsi Soal

#### Jadi, ceritanya...

< Cerita soal >

#### Spesifikasi program

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