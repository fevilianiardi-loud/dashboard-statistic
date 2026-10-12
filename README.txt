# Dashboard Statistik Deskriptif - Data Latihan 1

## 1. Instalasi
Buka terminal di folder project, lalu jalankan:

```bash
python -m pip install -r requirements.txt
```

Jika perintah `python` tidak dikenali di Windows, coba:
```bash
py -m pip install -r requirements.txt
```

## 2. Menjalankan
```bash
python app.py
```

atau:
```bash
py app.py
```

Setelah muncul alamat seperti `http://127.0.0.1:5000`, buka alamat tersebut di Chrome.

## 3. Isi project
- `app.py` = Flask + perhitungan statistik
- `data.csv` = data latihan 1
- `templates/index.html` = halaman dashboard
- `static/style.css` = desain
- `static/script.js` = grafik dan tombol mode gelap

## 4. Hasil utama data
X: mean 7.70, median 8.00, min 3, max 12, range 9, standar deviasi 2.98.
Y: mean 7.40, median 7.00, min 5, max 11, range 6, standar deviasi 2.22.
Korelasi Pearson X-Y sekitar 0.69, menunjukkan hubungan positif yang cukup kuat pada data ini.

Catatan: korelasi menunjukkan hubungan/pola, bukan bukti bahwa X menyebabkan Y.
