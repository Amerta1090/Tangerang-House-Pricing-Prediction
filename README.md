# Laporan Proyek Machine Learning - Abdul Majid

## Domain Proyek

Proyek ini bertujuan untuk membangun model prediksi harga rumah di Kota Tangerang Selatan, Indonesia, dengan menggunakan dataset yang berisi berbagai fitur rumah, seperti lokasi, jumlah kamar tidur, jumlah kamar mandi, dan ukuran lantai. Dataset ini dapat diunduh melalui [Kaggle: Housing Price in South Tangerang City, Indonesia](https://www.kaggle.com/datasets/gerryzani/housing-price-in-south-tangerang-city-indonesia).

Penyelesaian masalah ini penting untuk pasar properti karena prediksi harga yang lebih akurat dapat memberikan keputusan yang lebih tepat bagi pembeli, penjual, dan agen properti. Model ini akan memberikan nilai jual rumah yang lebih realistis dan membantu meminimalisir kesalahan estimasi harga yang sering terjadi di pasar.

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

### 1. URL/Tautan Sumber Data

[Kaggle: Housing Price in South Tangerang City, Indonesia](https://www.kaggle.com/datasets/gerryzani/housing-price-in-south-tangerang-city-indonesia)

### 2. Jumlah Baris dan Kolom

Dataset ini memiliki 29,420 entri dengan 7 kolom. Berikut adalah informasi lebih lanjut tentang struktur data:

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 29420 entries, 0 to 29419
Data columns (total 7 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   nav-link href        29420 non-null  object 
 1   listing-location     29420 non-null  object 
 2   price                29420 non-null  object 
 3   bed                  29282 non-null  float64
 4   bath                 29215 non-null  float64
 5   listing-floorarea    29420 non-null  object 
 6   listing-floorarea 2  29383 non-null  object 
dtypes: float64(2), object(5)
memory usage: 1.6+ MB
```

### 3. Kondisi Data

- **Missing Values**:  
  Kolom-kolom berikut mengandung nilai yang hilang (missing values):
  - **bed**: 138 missing values
  - **bath**: 205 missing values
  - **listing-floorarea 2**: 37 missing values

- **Duplikasi**:  
  Dataset ini memiliki **5,196 duplikasi** yang perlu ditangani agar model tidak terpengaruh oleh data yang tidak unik.
- **Outlier**:

![image](https://github.com/user-attachments/assets/002fcf2e-7b36-4974-95cc-895491287b1a)

![image](https://github.com/user-attachments/assets/1b209ec4-f836-40f3-b299-584f80bdc84a)

![image](https://github.com/user-attachments/assets/c041c10b-2723-441b-a143-c1d14863e93f)

![image](https://github.com/user-attachments/assets/d217f0d7-c898-4e35-ac8e-e0fa2d6ef805)

![image](https://github.com/user-attachments/assets/5a4d196b-7a18-436a-a39e-3fa6c77a87b3)



### 4. Uraian Seluruh Fitur pada Data

- **nav-link href**:  
  URL atau tautan yang mengarah ke halaman listing properti.

- **listing-location**:  
  Lokasi properti, yang menggambarkan tempat dimana properti tersebut berada.

- **price**:  
  Harga properti dalam satuan IDR, yang perlu dikonversi menjadi tipe numerik untuk analisis lebih lanjut.

- **bed**:  
  Jumlah kamar tidur yang terdapat dalam properti. Tipe data ini adalah numerik (float).

- **bath**:  
  Jumlah kamar mandi dalam properti. Tipe data ini juga numerik (float).

- **listing-floorarea**:  
  Luas bangunan properti dalam satuan meter persegi. Kolom ini berisi teks yang perlu diubah ke tipe numerik untuk analisis.

- **listing-floorarea 2**:  
  Alternatif luas bangunan properti dalam satuan meter persegi yang berbeda. Kolom ini juga berisi teks dan perlu dikonversi ke tipe numerik.

### Tahapan untuk memahami data:
1. **Exploratory Data Analysis (EDA)**: Melakukan analisis untuk memahami distribusi harga, hubungan antar fitur, dan mengecek korelasi antara fitur dan harga rumah.


![image](https://github.com/user-attachments/assets/8318a937-b324-4e39-8024-87cd763eb50f)
menggunakan bloxplot, dapat dilihat distribusi data data pada tiap tiap kolom.



![image](https://github.com/user-attachments/assets/ea730b6f-85f6-4465-8627-935bc9ae1345)
dapat terlihat bahwa 'listing-floorarea(m2) dan bath adalah top 2 fitur dengan korelasi paling tinggi dengan price. dapat dilihat juga bahwa fitur fitur yang lain juga memiliki nilai korelasi yang cukup tinggi (>0.5)

3. **Visualisasi Data**: Membuat grafik untuk mengilustrasikan distribusi harga, jumlah kamar tidur, kamar mandi dan ukuran lantai terhadap harga rumah.
![image](https://github.com/user-attachments/assets/a0927979-dc6e-45af-9ffc-abf9c4ca609d)
menampilkann histogram dari perbandingan jumlah kamar mandi dan kamar tidur pada dataset. terlihat bahwa kamartidur memiliki penyebaran di angka 2-5. dan memiliki nilai paling tinggi di jumlah kamar tidur 3. sedangkan penyebaran kamar mandi memiliki penyebaran di rentang 1-7. dengan jumlah kamar mandi terbanyak di angka 1-2.



![image](https://github.com/user-attachments/assets/691cf294-46f4-42ae-87e8-e4525bcafde1)
visualisasi tersebut menampilkan perbandingan antara luas tanah dan harga rumah. grafik tersebut menunjukan bahwa semakin luas tanah, semakin tinggi harga rumah
## Data Preparation

Data preparation adalah tahapan penting yang memastikan bahwa data yang digunakan dalam model machine learning sudah bersih, konsisten, dan dalam format yang tepat. Pada proyek ini, tahapan data preparation mencakup beberapa langkah berikut:

### 1. **Pembersihan Data (Data Cleaning)**:
   - **Menghapus Nilai yang Hilang (Missing Values)**:
     Dataset ini mengandung beberapa nilai yang hilang pada kolom `bed`, `bath`, dan `listing-floorarea 2`. Untuk mengatasi hal ini, terdapat beberapa pendekatan yang dapat diterapkan:
     - **Imputasi dengan Rata-rata/Median**: Nilai yang hilang pada kolom numerik (seperti `bed` dan `bath`) dapat diisi dengan rata-rata atau median dari nilai yang ada. Pada kolom `bed` dan `bath`, imputasi dengan median lebih disarankan karena median lebih tahan terhadap pencilan.
     - **Penghapusan Baris (Row Dropping)**: Baris yang mengandung banyak nilai hilang dapat dihapus jika dianggap tidak terlalu signifikan bagi keseluruhan dataset.
   
   - **Menghapus Duplikasi (Duplicate Removal)**: Dataset ini mengandung 5,196 baris duplikat. Duplikasi ini dapat mempengaruhi hasil model dan perlu dihapus untuk memastikan bahwa data yang digunakan adalah unik.

   - **Mengonversi Kolom `price`, `listing-floorarea`, dan `listing-floorarea 2` ke Format Numerik**:
     Kolom-kolom ini awalnya berada dalam format string dan perlu diubah menjadi tipe data numerik untuk melakukan analisis lebih lanjut. Proses ini melibatkan:
     - Menghapus karakter yang tidak relevan seperti tanda mata uang atau unit yang tertera pada kolom `price`.
     - Mengubah satuan pada kolom `listing-floorarea` dan `listing-floorarea 2` agar sesuai dalam satuan yang sama (misalnya, semuanya dalam meter persegi).

### 2. **Feature Engineering**:
   - **Membuat Fitur Tambahan**:
     Salah satu tahapan penting dalam data preparation adalah membuat fitur tambahan yang dapat memberikan informasi lebih bagi model. Dalam kasus ini, fitur tambahan yang relevan dapat dibuat dengan menggabungkan kolom `listing-floorarea` dan `listing-floorarea 2` untuk menghasilkan **total luas lantai** (total floor area). Dengan mengkombinasikan kedua kolom tersebut, model dapat memiliki informasi yang lebih lengkap mengenai luas properti yang ditawarkan.
     - Kolom `listing-floorarea` dan `listing-floorarea 2` memiliki satuan yang berbeda, oleh karena itu konversi satuan perlu dilakukan terlebih dahulu untuk memastikan keselarasan.
   
   - **Fitur Kategorikal**:
     Kolom `listing-location` adalah fitur kategorikal yang menunjukkan lokasi properti. Fitur kategorikal seperti ini perlu diproses dengan teknik encoding (seperti One-Hot Encoding atau Label Encoding) untuk mengubahnya menjadi format numerik yang dapat dipahami oleh model machine learning.

### 3. **Normalisasi Data**:
   - **Skalasi atau Normalisasi Fitur Numerik**:
     Sebagian besar algoritma machine learning (terutama yang berbasis jarak seperti KNN atau gradient descent-based seperti linear regression) memerlukan fitur numerik yang memiliki skala yang sama agar dapat bekerja secara optimal. Oleh karena itu, normalisasi atau skalasi fitur numerik perlu dilakukan.
     - **MinMax Scaling**: MinMaxScaler mengubah fitur numerik agar berada dalam rentang [0, 1]. Ini berguna jika model machine learning Anda sensitif terhadap skala data.
     - **Standardization (Z-score Normalization)**: Teknik ini mengubah fitur menjadi distribusi dengan rata-rata 0 dan deviasi standar 1. Hal ini bermanfaat ketika data memiliki distribusi yang tidak teratur atau pencilan.
   
   - **Penerapan Skalasi**: 
     Fitur numerik seperti `bed`, `bath`, dan `listing-floorarea` akan distandarisasi menggunakan salah satu metode di atas. Proses ini juga memastikan bahwa perbedaan besar dalam skala antara fitur tidak mempengaruhi performa model.

### 4. **Pemisahan Data untuk Pelatihan dan Pengujian**:
   Setelah data dipersiapkan, langkah selanjutnya adalah membagi dataset menjadi dua bagian utama:
   - **Training Set**: Digunakan untuk melatih model.
   - **Test Set**: Digunakan untuk menguji performa model setelah proses pelatihan selesai.
   
   Pemisahan ini penting untuk menghindari overfitting dan untuk mengukur kemampuan model dalam generalisasi terhadap data yang tidak terlihat sebelumnya. Proporsi umum untuk pemisahan ini adalah 70%-80% untuk training set dan 20%-30% untuk test set.

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

![image](https://github.com/user-attachments/assets/018cc107-4c9f-42c5-9b28-b71fa63996ab)


**Model: Linear Regression**
- **R-squared**: 0.752
- **RMSE**: 890.85 juta IDR
- **MAE**: 619.97 juta IDR

**Model: Random Forest Regressor**
- **R-squared**: 0.864
- **RMSE**: 659.41 juta IDR
- **MAE**: 340.30 juta IDR

Berdasarkan hasil evaluasi, **Random Forest Regressor** menunjukkan performa yang lebih baik dibandingkan dengan **Linear Regression**, dengan nilai **R-squared** yang lebih tinggi (0.864 vs. 0.752) dan kesalahan prediksi yang lebih rendah (RMSE: 659.41 juta IDR vs. 890.85 juta IDR, MAE: 340.30 juta IDR vs. 619.97 juta IDR).

#### Linear Regression
![image](https://github.com/user-attachments/assets/72869c76-814a-46d6-af0c-52c4d31c8254)
![image](https://github.com/user-attachments/assets/c9dc5202-0b48-436d-ac14-c6bde0f7e802)


#### Random Forest
![image](https://github.com/user-attachments/assets/45dff225-56a2-451a-bebc-e1a6f8183c4c)
![image](https://github.com/user-attachments/assets/f14a52df-b021-4942-9353-c47e477c64ea)



### Hubungan dengan Business Understanding

Dalam konteks proyek ini, tujuan utamanya adalah untuk memprediksi harga rumah di Kota Tangerang Selatan, Indonesia, dengan menggunakan dataset yang mencakup informasi tentang lokasi, jumlah kamar tidur, jumlah kamar mandi, dan ukuran lantai properti. **Business Understanding** di sini merujuk pada pemahaman mengenai tantangan dan tujuan yang ingin dicapai dalam konteks bisnis real estate, serta dampak yang diharapkan dari penggunaan model prediksi harga rumah.

#### Apakah model ini sudah menjawab setiap problem statement?

Proyek ini bertujuan untuk memberikan prediksi harga rumah berdasarkan fitur-fitur yang relevan dari dataset, seperti lokasi, jumlah kamar tidur, dan luas properti. Dengan menggunakan dua model utama, **Linear Regression** dan **Random Forest Regressor**, model-model ini telah berhasil memberikan prediksi harga rumah yang cukup akurat. Berdasarkan hasil evaluasi yang menunjukkan **R-squared** yang cukup tinggi untuk kedua model (0.752 untuk Linear Regression dan 0.864 untuk Random Forest Regressor), ini menunjukkan bahwa model-model ini berhasil menangkap pola dalam data dan memberikan prediksi harga rumah yang mendekati harga aktual.

Oleh karena itu, model yang dikembangkan telah berhasil menjawab **problem statement** yang diajukan, yaitu prediksi harga rumah dengan memperhatikan beberapa faktor yang relevan.

#### Apakah model ini berhasil mencapai setiap goal yang diharapkan?

Tujuan dari proyek ini adalah untuk mengembangkan model yang dapat memberikan prediksi harga rumah dengan akurasi yang baik dan dapat digunakan untuk membantu pembeli rumah dan agen real estate dalam membuat keputusan. Berdasarkan hasil evaluasi model:
- **Random Forest Regressor** memiliki **R-squared** yang lebih tinggi dan kesalahan prediksi yang lebih rendah dibandingkan dengan **Linear Regression**, yang menunjukkan bahwa model ini lebih baik dalam menangkap kompleksitas data dan memberikan prediksi yang lebih tepat.
- **RMSE** dan **MAE** yang lebih rendah pada **Random Forest Regressor** menunjukkan bahwa model ini memberikan prediksi yang lebih akurat, dengan kesalahan yang lebih kecil.

Dengan demikian, tujuan untuk memberikan model yang memiliki akurasi tinggi dalam memprediksi harga rumah telah tercapai, dengan **Random Forest Regressor** sebagai model yang paling efektif.

#### Apakah solusi yang direncanakan memberikan dampak yang signifikan?

Solusi yang direncanakan dalam proyek ini memberikan dampak signifikan terhadap sektor bisnis real estate, terutama dalam membantu para pembeli dan agen real estate untuk memperkirakan harga rumah secara lebih tepat. Dengan menggunakan model prediksi harga rumah yang lebih akurat, para pengguna dapat membuat keputusan yang lebih informasi dan efisien terkait dengan pembelian atau penjualan properti. Sebagai contoh:
- **Agen real estate** dapat menggunakan model ini untuk memberikan estimasi harga yang lebih realistis kepada klien mereka, yang dapat meningkatkan kepercayaan dan efisiensi dalam proses transaksi.
- **Pembeli rumah** dapat menggunakan prediksi harga untuk menentukan anggaran yang lebih sesuai dan menghindari keputusan yang tidak menguntungkan berdasarkan harga yang tidak realistis.

Secara keseluruhan, model yang dikembangkan membantu dalam meningkatkan akurasi prediksi harga rumah, yang memiliki dampak positif terhadap pengalaman dan keputusan bisnis dalam sektor real estate.

### Kesimpulan

Model yang dikembangkan dalam proyek ini telah berhasil menjawab problem statement, mencapai goal yang diharapkan, dan memberikan dampak signifikan bagi sektor real estate. **Random Forest Regressor** terbukti sebagai model yang lebih baik dalam hal akurasi dan keakuratan prediksi harga rumah dibandingkan dengan **Linear Regression**, yang menunjukkan bahwa pendekatan machine learning dapat membawa perubahan positif dalam industri ini dengan memberikan solusi prediksi yang lebih tepat.
