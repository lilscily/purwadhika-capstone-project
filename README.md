# Transjakarta Transaction Analytics

## 📌 Deskripsi Proyek
Proyek ini merupakan bagian dari capstone project untuk menganalisis data transaksi pengguna Transjakarta. Analisis dilakukan dengan pendekatan *Exploratory Data Analysis (EDA)* untuk memahami pola dan karakteristik pengguna, distribusi transaksi berdasarkan waktu, serta volume transaksi per koridor. Hasil analisis divisualisasikan dalam bentuk grafik dan dashboard interaktif menggunakan Tableau.

## 🎯 Tujuan
- Memahami profil pengguna Transjakarta berdasarkan usia dan gender.
- Menganalisis pola transaksi berdasarkan periode waktu (harian, mingguan, dan jam tertentu).
- Mengidentifikasi koridor dengan volume transaksi tertinggi dan terendah.
- Memberikan insight yang dapat membantu pemerintah dalam pengambilan kebijakan transportasi publik yang lebih efektif.

## 📊 Analisis
1. **Profil Pengguna**
   - Distribusi usia pengguna menunjukkan dominasi kelompok usia produktif (20–40 tahun).
   - Gender pengguna didominasi oleh **Perempuan (53,4%)** dibandingkan **Laki-laki (46,6%)**.

2. **Pola Transaksi Berdasarkan Waktu**
   - Aktivitas tertinggi terjadi pada jam sibuk (**06.00 & 17.00**) di hari kerja.
   - Pada akhir pekan, jumlah transaksi menurun signifikan, terutama di jam kerja.

3. **Analisis Koridor**
   - Koridor dengan volume tertinggi: **Cibubur – Balai Kota**, **Ciputat – CSW**, dan **Harmoni – Jakarta International Stadium**.
   - Koridor dengan volume terendah: **Kampung Rambutan – Blok M**, **Tanah Abang – Kebayoran Lama via Pos Pengumben**, dan **Pulo Gadung – Lampiri**.

## 📈 Dashboard
Visualisasi dibuat menggunakan **Tableau Public** dengan menampilkan:
- Total pengguna, transaksi, koridor, dan total tap.
- Distribusi usia & gender pengguna.
- Pola transaksi per hari dan per jam.
- Volume transaksi per koridor.

## 💡 Insight
- Mayoritas pengguna adalah kelompok usia produktif, dengan kontribusi signifikan dari pelajar.
- Perempuan sedikit lebih banyak menggunakan Transjakarta dibanding laki-laki.
- Pola penggunaan sangat dipengaruhi oleh jam sibuk kerja.
- Beberapa koridor memiliki beban transaksi tinggi sehingga perlu penguatan armada.

## ✅ Rekomendasi
- Menambah armada pada koridor dengan volume tinggi.
- Mengatur jadwal keberangkatan lebih padat pada jam sibuk.
- Menyediakan fasilitas ramah perempuan untuk meningkatkan kenyamanan.
- Optimalisasi pemanfaatan koridor dengan volume rendah.

## 🛠 Tools yang Digunakan
- **Python (Pandas, Matplotlib, Seaborn)** → Data Cleaning & EDA
- **Jupyter Notebook** → Dokumentasi Analisis
- **Tableau Public** → Dashboard Visualisasi

---
✍️ Disusun sebagai bagian dari Capstone Project Data Analytics
