# Tutorial 4 : Perulangan / Repetisi

## Daftar Isi

- [Tutorial 4 : Perulangan / Repetisi](#tutorial-4--perulangan--repetisi)
  - [Daftar Isi](#daftar-isi)
  - [Repetisi](#repetisi)
    - [While loop (undefinite loop)](#while-loop-undefinite-loop)
    - [For loop (Definite Loop)](#for-loop-definite-loop)
  - [Iterable](#iterable)
    - [Range](#range)
    - [List](#list)
      - [Mengakses konten list](#mengakses-konten-list)
      - [Nested List (List Bertingkat)](#nested-list-list-bertingkat)
      - [Range to List](#range-to-list)
  - [Tambahan](#tambahan)
    - [Advanced Loop](#advanced-loop)
      - [Break](#break)
      - [Continue](#continue)
      - [Pass](#pass)
    - [Algoritma: Loop for Correct Input](#algoritma-loop-for-correct-input)
  - [Latihan : *< Judul Latihan >*](#latihan---judul-latihan)
  - [Tugas : *< Judul Tugas >*](#tugas---judul-tugas)
    - [Deskripsi Soal](#deskripsi-soal)
      - [Jadi, ceritanya...](#jadi-ceritanya)
      - [Spesifikasi program](#spesifikasi-program)
      - [Contoh](#contoh)
      - [Hint](#hint)
    - [Bonus](#bonus)
    - [Komponen penilaian](#komponen-penilaian)

## Repetisi

Selain seleksi, hal paling penting pada sebuah program adalah repetisi (perulangan) yang berguna untuk mengulangi serangkaian statement dalam sebuah kondisi.

### While loop (undefinite loop)

```py
while <condition>:
    <body>
```

`while` loop menjalankan statement pada `body` secara berulang-ulang selama `condition` bernilai True.

<!-- TODO: Flowchart of while loop here -->

```py
# di luar loop, inisiasi kondisi nya
x = 5

while x > 0:
    print(x, end=” ”)
    # di dalam loop, ubah nilai variable nya
    # agar menuju ke kondisi False
    x -= 1  
print(x)
```
```
5 4 3 2 1
0
```

Sama seperti if statement, blok kode yang dijalankan jika kondisi bernilai True adalah blok program yang diberi indentasi relatif terhadap baris while.

```py
# Apa output program ini?
x = 5

while x > 0:
    print(x, end=” ”)
    x += 1  
print(x)
```

Jika variable kondisi tidak mengalami perubahan atau perubahannya tidak akan pernah membuat kondisi bernilai False, maka akan terjadi ***infinite loop***.

```py
# Apa output program ini?
x = 5

while x > 5:
    print(x, end=” ”)
    x -= 1
```

Statement di bawah while tidak dijalankan karena kondisi pada while loop bernilai False.

### For loop (Definite Loop)

```py
for <var> in <sequence>:
    <body>
```

`for` loop adalah perulangan yang bergerak sesuai *sequence* yang ada. *Sequence* dapat berupa list, string, atau range. Tipe-tipe data tersebut dapat disebut sebagai ***iterable***.

Loop dengan range:
```py
for i in range(5):
    print(i, end = " ")
```
```
0 1 2 3 4
```

Loop dengan list:
```py
a_list = [1, 2, 2, 50]

for i in a_list:
    print(i, end = " | ")
```
```
1 | 2 | 2 | 50 |
```

Loop dengan string:
```py
a_string = "Vaporwave"

for i in a_string:
    print(i, end = " ")

# Apa outputnya?
```

> Bagaimana bentuk for loop dari while loop [ini](#while-loop-undefinite-loop)?

## Iterable

### Range

`range` adalah fungsi Python yang menghasilkan barisan angka, (secara default) mulai dari nol.

Fungsi range dapat diisi parameter *integer* yang menyatakan angka mana yang ingin dihasilkan.

`range(angka)`
```py
for i in range(10):
    print(i, end = " ")

# 0 1 2 3 4 5 6 7 8 9
```

Fungsi range juga menerima parameter untuk mementukan awal dan akhir dari barisan yang dihasilkan.

`range(awal, akhir)`
```py
for i in range(5, 10):
    print(i, end = ", ")

# 5, 6, 7, 8, 9
```

Fungsi range dapat mengatur selisih antar angka pada barisan.

`range(awal, akhir, selisih)`
```py
for i in range(0, 10, 2):
    print(i, end = " ")

# 0 2 4 6 8
```

> Bisakah range membuat barisan angka yang menurun?

> Apa yang terjadi jika kita mencetak range tanpa for loop?

### List

`list` adalah tipe data yang menampung barisan tipe data lainnya, salah satunya adalah barisan angka.
Contoh: `[1, 2, 3, 4, 5]`
`["tulisan", True, 42, 0.69]`
`[]` (list kosong)

#### Mengakses konten list

Konten di dalam list dapat diakses menggunakan nomor index nya yang dikelilingi kurung siku.
`nama_list[index]`

```py
>>> useful = ["Barry", "Iris", "Cisco", "Caitlin"]
>>> useful[1]           # Mengakses konten list
'Iris'
>>> useful[1] = "Patty" # Mengganti konten list
>>> useful
['Barry', 'Patty', 'Cisco', 'Caitlin']
```

Selain mengakses satu item pada list, kita dapat mengakses beberapa item sekaligus. Caranya sama seperti String Slicing yang akan dipelajari pada [lab selanjutnya](..\lab_5\README.md).

#### Nested List (List Bertingkat)

*Nested List* adalah list yang berisi list.

```py
>>> shape = ["Circle", "Triangle", ["R1", "R2"], "Square", "Cross"]
>>> shape[1]
'Triangle'
>>> shape[2]
['R1', 'R2']
>>> shape[2][0]
'R1'
>>> len(shape)  # Mencari panjang dari list
5
```

#### Range to List

Range dapat diubah menjadi list dengan menggunakan fungsi `list(...)`

```py
>>> a_range = range(10)
>>> a_range
range(0, 10)
>>> a_list = list(a_range)
>>> a_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

> Apa bedanya range dan list? Range *immutable* sedangkan list *mutable*. Artinya isi range pada tidak dapat diubah sedangkan list bisa.

<!-- TODO: Complete this -->

## Tambahan

### Advanced Loop

#### Break
#### Continue
#### Pass


### Algoritma: Loop for Correct Input

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