# Laporan Proyek Machine Learning - Abdul Majid

## Domain Proyek

Proyek ini bertujuan untuk membangun model prediksi harga rumah di Kota Tangerang Selatan, Indonesia, dengan menggunakan dataset yang berisi berbagai fitur rumah, seperti lokasi, jumlah kamar tidur, jumlah kamar mandi, dan ukuran lantai. Dataset ini dapat diunduh melalui [Kaggle: Housing Price in South Tangerang City, Indonesia](https://www.kaggle.com/datasets/gerryzani/housing-price-in-south-tangerang-city-indonesia).

Penyelesaian masalah ini penting untuk pasar properti karena prediksi harga yang lebih akurat dapat memberikan keputusan yang lebih tepat bagi pembeli, penjual, dan agen properti. Model ini akan memberikan nilai jual rumah yang lebih realistis dan membantu meminimalisir kesalahan estimasi harga yang sering terjadi di pasar.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Faktor-faktor yang mempengaruhi harga properti sangat beragam, dengan lokasi sebagai faktor dominan. Proyek ini akan membantu meningkatkan ketepatan harga jual berdasarkan analisis data historis.
- Referensi terkait dapat ditemukan di [Predicting House Prices using Machine Learning](https://www.mecs-press.org/ijieeb/ijieeb-v12-n2/IJIEEB-V12-N2-3.pdf).

## Business Understanding

### Problem Statements
- **Pernyataan Masalah 1**: Bagaimana memprediksi harga rumah di Kota Tangerang Selatan berdasarkan fitur-fitur dalam dataset, seperti lokasi, jumlah kamar tidur, dan ukuran lantai?
- **Pernyataan Masalah 2**: Bagaimana memberikan rekomendasi harga jual rumah yang lebih realistis kepada penjual dan pembeli dengan menggunakan model prediksi harga?

### Goals
- **Tujuan Masalah 1**: Membangun model machine learning untuk memprediksi harga rumah berdasarkan data fitur yang tersedia.
- **Tujuan Masalah 2**: Memberikan rekomendasi harga jual rumah yang akurat berdasarkan model prediksi harga yang dibangun.

### Solution Statements
- **Solusi 1**: Menggunakan model regresi linier untuk melihat hubungan antara variabel fitur dan harga rumah. Selain itu, akan digunakan teknik feature engineering untuk meningkatkan kualitas model.
- **Solusi 2**: Menggunakan model ensemble seperti Random Forest Regressor untuk mengatasi masalah non-linearitas dan meningkatkan akurasi prediksi.

## Data Understanding

Dataset yang digunakan mencakup informasi mengenai harga properti di Tangerang Selatan, dengan fitur-fitur berikut:

- **nav-link href**: URL yang mengarah ke halaman listing properti.
- **listing-location**: Lokasi properti (misalnya, kelurahan atau kecamatan).
- **price**: Harga rumah (target variabel, dalam format string yang akan diproses menjadi numerik).
- **bed**: Jumlah kamar tidur.
- **bath**: Jumlah kamar mandi.
- **listing-floorarea**: Ukuran luas lantai rumah (dalam satuan m², dalam format string).
- **listing-floorarea 2**: Luas lantai tambahan jika ada (dalam satuan m², dalam format string).

### Tahapan untuk memahami data:
1. **Exploratory Data Analysis (EDA)**: Melakukan analisis untuk memahami distribusi harga, hubungan antar fitur, dan mengecek korelasi antara fitur dan harga rumah.
![image](https://github.com/user-attachments/assets/6f9d9458-6e06-4089-a928-7f55c99f352b)
![image](https://github.com/user-attachments/assets/ea730b6f-85f6-4465-8627-935bc9ae1345)


3. **Visualisasi Data**: Membuat grafik untuk mengilustrasikan distribusi harga, jumlah kamar tidur, kamar mandi dan ukuran lantai terhadap harga rumah.
![image](https://github.com/user-attachments/assets/a0927979-dc6e-45af-9ffc-abf9c4ca609d)
![image](https://github.com/user-attachments/assets/691cf294-46f4-42ae-87e8-e4525bcafde1)

## Data Preparation

Data preparation mencakup beberapa tahapan berikut:
1. **Pembersihan Data**:
   - Menghapus nilai yang hilang pada kolom `bed`, `bath`, `listing-floorarea`, dan `listing-floorarea 2`.
   - Mengubah kolom `price`, `listing-floorarea`, dan `listing-floorarea 2` dari format string menjadi numerik.
2. **Feature Engineering**:
   - Membuat fitur tambahan seperti total luas lantai (menggabungkan `listing-floorarea` dan `listing-floorarea 2`).
3. **Normalisasi Data**: Menggunakan MinMaxScaler atau StandardScaler untuk menormalkan fitur numerik agar model dapat bekerja dengan baik.

Proses ini memastikan data yang digunakan dalam model sudah bersih dan dalam format yang tepat untuk analisis lebih lanjut.

## Modeling

Model yang diterapkan pada proyek ini adalah:
1. **Regresi Linier**: Digunakan untuk memodelkan hubungan linear antara fitur dan harga rumah.
2. **Random Forest Regressor**: Algoritma ensemble yang digunakan untuk menangani data yang lebih kompleks dan non-linear.
3. **Gradient Boosting Machine (GBM)**: Digunakan untuk meningkatkan performa model dengan cara menggabungkan beberapa pohon keputusan secara bertahap.

### Hyperparameter Tuning
Hyperparameter tuning dilakukan menggunakan teknik Grid Search untuk mencari parameter terbaik bagi Random Forest dan GBM, seperti jumlah pohon (`n_estimators`) dan kedalaman pohon (`max_depth`).

Model terbaik yang dipilih adalah **Random Forest Regressor** karena menghasilkan performa yang lebih stabil dan akurat dibandingkan dengan model regresi linier.

## Evaluation

Metrik evaluasi yang digunakan dalam proyek ini adalah:
- **Mean Absolute Error (MAE)**: Mengukur rata-rata perbedaan antara harga prediksi dan harga aktual.
- **Mean Squared Error (MSE)**: Mengukur rata-rata kuadrat perbedaan antara harga prediksi dan harga aktual.
- **Root Mean Squared Error (RMSE)**: Memberikan gambaran kesalahan dalam satuan yang sama dengan harga rumah.

### Penjelasan Metrik:
- **MAE**: Menunjukkan rata-rata perbedaan absolut antara harga rumah yang diprediksi dan harga rumah yang sebenarnya.
- **MSE**: Memberikan gambaran lebih mendalam tentang seberapa besar perbedaan antara harga prediksi dan harga sebenarnya dengan menghitung kuadrat perbedaan.
- **RMSE**: Menunjukkan kesalahan prediksi dengan memberikan gambaran yang lebih realistis karena hasilnya dalam satuan yang sama dengan harga rumah.

### Hasil Evaluasi:

**Model: Linear Regression**
- **R-squared**: 0.752
- **RMSE**: 890.85 juta IDR
- **MAE**: 619.97 juta IDR

**Model: Random Forest Regressor**
- **R-squared**: 0.864
- **RMSE**: 659.41 juta IDR
- **MAE**: 340.30 juta IDR

Berdasarkan hasil evaluasi, **Random Forest Regressor** menunjukkan performa yang lebih baik dibandingkan dengan **Linear Regression**, dengan nilai **R-squared** yang lebih tinggi (0.864 vs. 0.752) dan kesalahan prediksi yang lebih rendah (RMSE: 659.41 juta IDR vs. 890.85 juta IDR, MAE: 340.30 juta IDR vs. 619.97 juta IDR).

![image](https://github.com/user-attachments/assets/72869c76-814a-46d6-af0c-52c4d31c8254)
![image](https://github.com/user-attachments/assets/45dff225-56a2-451a-bebc-e1a6f8183c4c)
