# Tutorial 5 : String

## Daftar Isi

- [Tutorial 5 : String](#tutorial-5--string)
  - [Daftar Isi](#daftar-isi)
  - [String](#string)
    - [Multiline String](#multiline-string)
    - [Mengakses String](#mengakses-string)
    - [Slicing](#slicing)
    - [Operasi](#operasi)
  - [Tambahan](#tambahan)
    - [Escape Sequences/Character](#escape-sequencescharacter)
    - [String Representation](#string-representation)
  - [Latihan : *< Judul Latihan >*](#latihan---judul-latihan)
  - [Tugas : *< Judul Tugas >*](#tugas---judul-tugas)
    - [Deskripsi Soal](#deskripsi-soal)
      - [Jadi, ceritanya...](#jadi-ceritanya)
      - [Spesifikasi program](#spesifikasi-program)
      - [Contoh](#contoh)
      - [Hint](#hint)
    - [Bonus](#bonus)
    - [Komponen penilaian](#komponen-penilaian)


## String

**String** adalah barisan karakter. String dibentuk dari tulisan yang dikelilingi tanda kutip `'...'` atau `"..."`.
Contoh: `'Ini String!!1!'` 
`"Dalam b.indonesia artinya untaian"`

### Multiline String

**Triple quote** (kutip tiga) `"""`/`'''` dapat menampung string yang terdiri dari banyak baris.
Contoh:
```py
"""There was a time above...
a time before...
there were perfect things...

diamond absolutes.

But things fall... things on earth.
And what falls... is fallen.
In the dream, it took me to the light.

A beautiful lie.
"""
```

### Mengakses String

Karena String adalah barisan, maka setiap elemen string (setiap karakter) memiliki **index**.

Contoh: `"Hello World"`
|H|e|l|l|o| |W|o|r|l|d|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|0|1|2|3|4|5|6|7|8|9|10|
|-11|-10|-9|-8|-7|-6|-5|-4|-3|-2|-1|

Index **positif** dimulai dari 0 dan dihitung dari kiri.
Index **negatif** dimulai dari -1 dan dihitung dari kanan.

Elemen pada string dapat diakses dengan menulis indeks di dalam kurung siku. `nama_string[indeks]`

```py
>>> alert = "Halo, Polisi"
>>> alert[6]
'P'
>>> alert[-2]
's'
>>> alert[11]
'i'
>>> alert[12]
# IndexError
```

### Slicing

**Slicing** adalah proses memilih sub-barisan dari suatu barisan.
Slicing menggunakan sintaks berikut:
`nama_barisan[awal:akhir]`

> Index `akhir` tidak masuk ke sub-barisan

Jika awal dan/atau akhir tidak ditulis, berarti *default*-nya adalah 0 (awal barisan) untuk `awal` dan -1 (akhir barisan) untuk `akhir`.

<!-- TODO: Insert illustration of slicing -->

```py
>>> salam = "Hello World"
>>> salam[6:10]
'Worl'
>>> salam[6:]
'World'
>>> salam[:5]
'Hello'
>>> salam[4:-3]
'o Wo'
```

Slicing juga dapat menerima argumen ketiga, yaitu `selisih` antar karakter.

```py
>>> alert = "Halo, Polisi"
>>> alert[::2]
'Hl,Pls'
```

**Extended Slicing** ini juga berguna untuk membalikkan string.

```py
>>> mangkok = "Bakso"
>>> mangkok[::-1]
'oskaB'
```

> Hanya python yang bisa membalikkan string semudah ini.

### Operasi

```py
>>> s = "spam"
>>> len(s)        # Mencari panjang string
4

>>> s + "mer"     # Concatenation / Penggabungan string
'spammer' 
>>> "penge-" + s  # Concatenation tidak komutatif
'penge-spam'

>>> s * 3         # Repetisi string
'spamspamspam'
>>> 3 * s         # Repetisi string komutatif
'spamspamspam'
```

## Tambahan

### Escape Sequences/Character

**Escape Sequence** berfungsi untuk mencetak karakter yang tidak bisa diketik pada string.
Escape Sequence dapat ditulis dengan awalan *backslash* `\`.
Contoh escape sequence yang paling umum digunakan adalah tab `\t` dan new line `\n`

```py
>>> print("baris pertama \n baris kedua")
baris pertama 
 baris kedua
>>> len("\n\t")  # mencari panjang string
2
```

### String Representation


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