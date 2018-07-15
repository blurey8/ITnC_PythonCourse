# Tutorial 2 : Variable dan Tipe Data

## Daftar Isi

- [Tutorial 2 : Variable dan Tipe Data](#tutorial-2--variable-dan-tipe-data)
  - [Daftar Isi](#daftar-isi)
  - [Identifiers](#identifiers)
      - [Naming Conventions](#naming-conventions)
      - [Reserved Words](#reserved-words)
    - [Variable](#variable)
      - [Assignment](#assignment)
      - [Simultaneous Assignment](#simultaneous-assignment)
    - [Tipe Data](#tipe-data)
      - [Konversi Tipe Data](#konversi-tipe-data)
      - [Operator untuk Integer & Float](#operator-untuk-integer--float)
        - [Presedensi operator](#presedensi-operator)
      - [Augmented Assignment](#augmented-assignment)
  - [Modules](#modules)
  - [Latihan : *Simple Calculator*](#latihan--simple-calculator)
  - [Tugas : *Parabola Result*](#tugas--parabola-result)
    - [Deskripsi Soal](#deskripsi-soal)
      - [Jadi, Ceritanya...](#jadi-ceritanya)
      - [Spesifikasi program](#spesifikasi-program)
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

#### Simultaneous Assignment

Di Python, assignment dapat dilakukan untuk banyak variable dalam satu baris

```py
>>> x, y = 7, 10
>>> print(x)
7
>>> print(y)
10
>>> 
```

### Tipe Data

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

Hasil input user adalah string sehingga harus dikonversi menjadi integer jika input adalah angka.

Cara mengkonversi tipe input:
```py
input_user_str = input(Masukkan angka:)
input_user_int = int(input_user_str)
```
atau
```py
input_user_str = int(input(Masukkan angka:))
```

Fungsi untuk konversi tipe:
- `int(sebuah_var)` mengembalikan integer
- `float(sebuah_var)` mengembalikan float
- `str(sebuah_var)` mengembalikan string

**contoh:**
`int("2")` mengembalikan 2
`int(2.1)` mengembalikan 2 (dibulatkan ke bawah)
`int("2.1")` *error*

`float(2)` mengembalikan 2.0
`float("2")` mengembalikan 2.0
`float("2.1")` mengembalikan 2.1

`str(2)` mengembalikan "2"
`str(2.0)` mengembalikan "2.0"
`str("abc")` mengembalikan "abc"

#### Operator untuk Integer & Float

`+` penjumlahan
`-` pengurangan
`*` perkalian
`**` perpangkatan
`/` pembagian
`//` pembagian ke bawah
`%` modulo (sisa)

**contoh:**
```py
a = 10
b = 3

print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a ** b) # Output: 100
print(a / b)  # Output: 3.333333333
print(a // b) # Output: 3
print(a % b)  # Output: 1
```

Jika ada integer dan float pada *expression* yang sama, maka hasilnya adalah float
`42 * 3` mengasilkan 126
`42.0 * 3` mengasilkan 126.0

##### Presedensi operator

Presedensi adalah urutan operator yang dikerjakan terlebih dahulu. Presedensi pada Python kurang lebih sama seperti presedensi pada matematika.


| Operator    | Deskripsi                |
| :---------: | ------------------------ |
| ()          | Tanda kurung             |
| **          | Perpangkatan             |
| +x, -x      | Positif, Negative        |
| *, /, %, // | Perkalian, Pembagian     |
| +, -        | Penjumlahan, Pengurangan |

> Selengkapnya lihat di [dokumentasi Python 3.7](https://docs.python.org/3/reference/expressions.html#operator-precedence)

#### Augmented Assignment

Augmented assignment adalah penggabungan dari operasi dan assignment. Shortcut ini biasa digunakan untuk penambahan/pengurangan nilai.

| Cara cepat    | Ekivalen              |
| ------------- | --------------------- |
| `my_int += 2` | `my_int = my_int + 2` |
| `my_int -= 2` | `my_int = my_int - 2` |
| `my_int *= 2` | `my_int = my_int * 2` |
| `my_int /= 2` | `my_int = my_int / 2` |

## Modules

Modules adalah file yang bisa di-*import* ke program Python kalian. Module berisi konten-konten yang dapat memudahkan dalam membuat program.
Contohnya adalah **math** module yang berisi hal-hal yang berhubungan dengan matematika.

contoh:
```py
>>> import math     # sebelum menggunakan sebuah module, import terlebih dahulu
>>> print(math.pi)  # sebuah constant pi di math module
3.141592653589793
>>> print(math.sqrt(49)) # sebuah fungsi akar di math module
7.0
>>> help(math)      # melihat info module math
...
>>> help(math.sin)  # melihat info tenteng fungsi sin
...
```

<!-- TODO: Complete this -->

## Tambahan

### Algoritma: Max of Three

*written soon*

---

## Latihan : *Simple Calculator*

Buatlah program yang meminta masukan dua angka kemudian memberikan keluaran hasil-hasil dari beberapa operasi matematika.

**contoh:**
```
Masukkan angka pertama : 14
Masukkan angka kedua   : 3

14 + 3 = 17
14 - 3 = 11
14 * 3 = 42
14 ** 3 = 2744
14 / 3 = 4.666666666666667
14 // 3 = 4
14 % 3 = 2

```
```
Masukkan angka pertama : 5
Masukkan angka kedua   : 21
5 + 21 = 26
5 - 21 = -16
5 * 21 = 105
5 ** 21 = 476837158203125
5 / 21 = 0.23809523809523808
5 // 21 = 0
5 % 21 = 5
```
```
Masukkan angka pertama : 10
Masukkan angka kedua   : -2
10 + -2 = 8
10 - -2 = 12
10 * -2 = -20
10 ** -2 = 0.01
10 / -2 = -5.0
10 // -2 = -5
10 % -2 = 0
```
**Hint:** Tidak ada

---

## Tugas : *Parabola Result*

### Deskripsi Soal

#### Jadi, Ceritanya...

< Cerita soal >

#### Spesifikasi program

Sebuah parabola mempunyai rumus umum **y = ax<sup>2</sup> + bx + c**. Program akan meminta input nilai a, b, c, dan x nya (a, b, c, x adalah integer). Kemudian program akan mengeluarkan nilai dari y.

```
Rumus umum parabola: y = ax^2 + bx + c

Masukkan nilai a : <nilai a>
Masukkan nilai b : <nilai b>
Masukkan nilai c : <nilai c>

Rumus parabola: y = <rumus parabola nya>

Masukkan nilai x : <nilai x>
Nilai y pada x = 7 adalah <nilai y>
```

#### Contoh

```
Rumus umum parabola: y = ax^2 + bx + c

Masukkan nilai a : 1
Masukkan nilai b : 3
Masukkan nilai c : 2

Rumus parabola: y = 1x^2 + 3x + 2

Masukkan nilai x : 7
Nilai y pada x = 7 adalah 72
```
```
Rumus umum parabola: y = ax^2 + bx + c

Masukkan nilai a : -2
Masukkan nilai b : -5
Masukkan nilai c : 144

Rumus parabola: y = -2x^2 + -5x + 144

Masukkan nilai x : 10
Nilai y pada x = 10 adalah -106
```
```
Rumus umum parabola: y = ax^2 + bx + c

Masukkan nilai a : 0
Masukkan nilai b : 5
Masukkan nilai c : 0

Rumus parabola: y = 0x^2 + 5x + 0

Masukkan nilai x : 23
Nilai y pada x = 23 adalah 115
```

#### Hint

Fungsi `print` memiliki atribut `sep` (separator) untuk menentukan pemisah antar nilai yang di-print. Jika tidak ditulis, maka default nya adalah spasi (`sep=" "`)

### Bonus

Tambahkan link search dari google untuk menampilkan gambar dari kurva tersebut. Google memiliki link search seperti berikut https://www.google.com/search?q=[keyword yang mau kamu cari].

Jika keyword mengandung spasi, maka ganti spasi tersebut dengan **%2B**. Contoh: https://www.google.com/search?q=isi%2Bkeyword%2Bdi%2Bsini.

Untuk menampilkan gambar kurva di google, isi keyword dengan rumus parabola yang sudah kalian dapatkan tadi.

Contoh:
```
Rumus umum parabola: y = ax^2 + bx + c

Masukkan nilai a : 2
Masukkan nilai b : 4
Masukkan nilai c : 7

Rumus parabola: y = 2x^2 + 4x + 7

Masukkan nilai x : -1
Nilai y pada x = -1 adalah 5

Lihat gambar kurva di : (untuk a = 0 atau b = 0, gambar mungkin tidak akan keluar)
https://www.google.com/search?q=2x^2+%2B+4x+%2B+7
```

### Komponen penilaian

[ ] Hasil output (90)
[ ] Kerapihan kode (10)
[ ] Bonus (10)

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