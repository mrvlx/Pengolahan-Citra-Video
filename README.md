# Tugas MK Pengolahan Citra dan Video 1

Repository ini berisi dua program Python sederhana menggunakan **OpenCV** dan **NumPy** untuk mendemonstrasikan konsep dasar manipulasi channel warna pada citra digital. Kedua program menerapkan filter warna dengan cara mengisolasi atau mengombinasikan channel warna dari gambar grayscale ke dalam beberapa versi tinted (bertona warna).

## Daftar Isi
- [RGB.py](#rgbpy)
- [HikubiMePi.py](#hikubimepipy)
- [Konsep Dasar](#konsep-dasar)
- [Cara Menjalankan](#cara-menjalankan)

---

## RGB.py

Program ini menampilkan filter 3 warna dasar (RGB) dari sebuah gambar (`rektorat.png`).

**Langkah proses:**
1. Membaca gambar dan mengecilkan ukurannya (`scale = 0.2`) agar lebih ringan diproses.
2. Mengonversi gambar ke grayscale menggunakan `cv2.cvtColor`.
3. Membuat 3 versi tinted dari citra grayscale tersebut:
   - **Biru** — hanya mengisi channel B
   - **Hijau** — hanya mengisi channel G
   - **Merah** — hanya mengisi channel R
4. Menggabungkan ketiga hasil secara horizontal (`cv2.hconcat`) dan menampilkannya dalam satu window.

**Catatan teknis:** OpenCV menyimpan gambar dengan urutan channel **BGR**, bukan RGB. Jadi urutan parameter pada `cv2.merge([...])` mengikuti urutan Blue, Green, Red.

---

## HikubiMePi.py

Program ini adalah pengembangan dari `RGB.py`, menambahkan 2 warna campuran (kuning dan pink) sehingga total menjadi **5 filter warna** dari gambar (`image.png`).

**Langkah proses:**
1. Membaca gambar dan mengecilkan ukurannya (`scale = 0.5`).
2. Mengonversi ke grayscale, lalu membuat channel kosong (`zeros`) sebagai basis.
3. Membuat 5 versi tinted:
   - **Hijau** — channel G saja
   - **Kuning** — campuran channel G + R (kuning = hijau + merah)
   - **Biru** — channel B saja
   - **Merah** — channel R saja
   - **Pink** — campuran channel B + R (pink/magenta = biru + merah)
4. Menggabungkan kelima hasil secara horizontal dan menampilkan dalam satu window.

**Perbedaan dengan RGB.py:** selain 3 warna dasar, program ini menunjukkan bagaimana warna sekunder (kuning, pink) terbentuk dari kombinasi dua channel warna dasar sekaligus — bukan hanya satu channel seperti warna primer.

---

## Konsep Dasar

Kedua program menggunakan pendekatan yang sama:

1. **Grayscale sebagai basis intensitas** — nilai grayscale pada setiap pixel dianggap sebagai "seberapa terang/gelap" titik tersebut, lalu nilai ini disalin ke satu atau lebih channel warna target.
2. **`cv2.merge()`** — menggabungkan beberapa channel (masing-masing berupa array 2D) menjadi satu gambar berwarna (array 3D).
3. **Channel kosong (`zeros`)** — dipakai untuk channel warna yang tidak diaktifkan, sehingga hasil akhirnya benar-benar hanya menonjolkan warna yang diinginkan.
4. **Warna sekunder** dibentuk dengan mengisi *dua* channel sekaligus dengan nilai grayscale yang sama:
   - Kuning = Hijau + Merah
   - Pink/Magenta = Biru + Merah
   - Cyan = Biru + Hijau (tidak dipakai di kedua program ini, tapi mengikuti prinsip yang sama)

Filter-filter ini adalah simulasi visual sederhana, **bukan** konversi warna yang presisi secara ilmiah (berbeda dengan konversi CMYK yang sesungguhnya, yang memerlukan rumus konversi dari nilai R, G, B asli). Tujuannya lebih untuk memahami bagaimana channel warna bekerja dan bagaimana kombinasi channel dapat membentuk kesan warna yang berbeda.

---

## Cara Menjalankan

**Requirement:**
```bash
pip install opencv-python numpy
```

**Menjalankan program:**
```bash
python RGB.py
python HikubiMePi.py
```

Pastikan file gambar (`rektorat.png` untuk `RGB.py` dan `image.png` untuk `HikubiMePi.py`) berada di folder yang sama dengan script, atau sesuaikan path pada `cv2.imread(...)`.

Setiap program akan membuka window OpenCV yang menampilkan gambar hasil filter secara berdampingan. Tekan tombol apa saja pada keyboard untuk menutup window.