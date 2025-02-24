# -*- coding: utf-8 -*-
"""House Price Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZxL47Ji_dYgDwcQ9Vf8hOntctc060M_f

#Tanggerang House Pricing Prediction

##import library
"""

import pandas as pd
from google.colab import drive
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import re

"""## **1 .read dataset**"""

data = pd.read_csv('https://github.com/Amerta1090/Tangerang-House-Pricing/raw/371c9ef4dfc248afc4a06f1e112f469cc2b85b55/rumahTangsel.csv', encoding='latin1')

data.head()

"""## **2. Detail dan tipe dataset**"""

data.info()

print("data columns : ", data.columns)

print("data shape : ", data.shape)

"""## **3. EDA (Expoloratory Data Analysis)**

###Handling Missing Value
"""

data.isnull().sum()

data = data.dropna()

data.isnull().sum()

"""###Handling Duplicated"""

duplikasi = data.duplicated().sum()
print("Jumlah Duplikasi Data :", duplikasi)

data = data.drop_duplicates()

##setelah di-handling duplikasi
duplikasi = data.duplicated().sum()
print("Jumlah Duplikasi Data :", duplikasi)

data.shape

"""

```
# This is formatted as code
```

###Handling Outlier"""

data.drop(columns=['nav-link href'], inplace=True)
data.sample(10)

data.info()

def convert_to_numeric(price_str):
    price_str = price_str.lower().replace(' ', '')
    if 'm' in price_str:
        return float(price_str.replace('m', '').replace(',', '.')) * 1_000_000_000
    elif 'jt' in price_str:
        return float(price_str.replace('jt', '').replace(',', '.')) * 1_000_000
    elif 'rb' in price_str:
        return float(price_str.replace('rb', '').replace(',', '.')) * 1_000
    else:
        return float(price_str.replace(',', '.'))

data['price'] = data['price'].apply(convert_to_numeric)

data.sample(10)

data.rename(columns={'listing-floorarea': 'listing-floorarea (m²)'}, inplace=True)
data.sample()

data['listing-floorarea (m²)'] = data['listing-floorarea (m²)'].str.replace(' m²', '').astype(float)

data.sample(10)

data.info()

# Definisi fungsi untuk membersihkan kolom
def hapus_karakter(text):
    return re.sub(r'\D', '', text)

# Terapkan fungsi ke setiap elemen dalam kolom 'listing-floorarea 2'
data['listing-floorarea 2'] = data['listing-floorarea 2'].apply(hapus_karakter)

# Tampilkan hasil
print(data)

data['listing-floorarea 2'] = data['listing-floorarea 2'].astype(float)

data.rename(columns={'listing-floorarea 2': 'harga listing-floorarea per m²'}, inplace=True)

data.sample(10)

data = data.drop(columns=['listing-location'])
data.info()

data.sample(10)

# Daftar kolom yang akan diolah
kolom_kolom = ['price', 'bed', 'bath', 'listing-floorarea (m²)', 'harga listing-floorarea per m²']

# Salinan data untuk difilter
data_filtered = data.copy()

for kolom in kolom_kolom:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=data[kolom], orient='h')
    plt.title('Penyebaran Data {}'.format(kolom))
    plt.xlabel(kolom)
    plt.show()

    # Handling outlier menggunakan metode IQR
    Q1 = data[kolom].quantile(0.25)
    Q3 = data[kolom].quantile(0.75)
    IQR = Q3 - Q1

    # Filtering data berdasarkan IQR
    data_filtered = data_filtered[(data_filtered[kolom] >= Q1 - 1.5 * IQR) & (data_filtered[kolom] <= Q3 + 1.5 * IQR)]

    # Menampilkan boxplot setelah handling outlier
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=data_filtered[kolom], orient='h')
    plt.title('Penyebaran Data {} (Setelah Handling Outlier)'.format(kolom))
    plt.xlabel(kolom)
    plt.show()

# Menampilkan data setelah handling outlier untuk semua kolom
print(data_filtered)

"""## **4. Descriptive Statistik**"""

# Menampilkan data_filtered
data_filtered.describe()

"""####Median

"""

# Menampilkan Data Median
price_median = data_filtered['price'].median()
bed_median = data_filtered['bed'].median()
bath_median = data_filtered['bath'].median()
listing_floorarea_median = data_filtered['listing-floorarea (m²)'].median()
harga_permeter_median = data_filtered['harga listing-floorarea per m²'].median()

print('price              :', price_median)
print('bed                :', bed_median)
print('bath               :', bath_median)
print('listing-floorarea  :', listing_floorarea_median)
print('harga permeter     :', harga_permeter_median)

"""#### Modus

"""

# Menampilkan data modus
price_modus = data_filtered['price'].mode()[0]
bed_modus = data_filtered['bed'].mode()[0]
bath_modus = data_filtered['bath'].mode()[0]
listing_floorarea_modus = data_filtered['listing-floorarea (m²)'].mode()[0]
harga_permeter_modus = data_filtered['harga listing-floorarea per m²'].mode()[0]

print('price              :', price_modus)
print('bed                :', bed_modus)
print('bath               :', bath_modus)
print('listing-floorarea  :', listing_floorarea_modus)
print('harga permeter     :', harga_permeter_modus)

"""## **5. Visualisasi Data**"""

# Membuat histogram dengan overlay
plt.figure(figsize=(10, 6))

# Histogram untuk jumlah kamar mandi
plt.hist(data_filtered['bath'], bins=5, alpha=0.5, label='Bathrooms', color='blue', edgecolor='black')

# Histogram untuk jumlah kamar tidur
plt.hist(data_filtered['bed'], bins=5, alpha=0.5, label='Bedrooms', color='green', edgecolor='black')

# Menambahkan label dan judul
plt.xlabel('Count')
plt.ylabel('Frequency')
plt.title('Histogram of Number of Bathrooms and Bedrooms')
plt.legend()

plt.show()

plt.figure(figsize=(12, 10))
for i, column in enumerate(data_filtered.columns, 1):
    plt.subplot(3, 2, i)
    sns.boxplot(data_filtered[column])
    plt.title(f'Boxplot of {column}')
plt.tight_layout()
plt.show()

# Menambahkan garis yang menunjukkan harga rata-rata untuk setiap luas tanah
average_prices = data_filtered.groupby('listing-floorarea (m²)')['price'].mean()
plt.figure(figsize=(10, 4))
plt.plot(average_prices.index, average_prices.values, color='blue', linestyle='-', linewidth=1.5)
plt.ylabel('Harga Rata-rata (miliar)')
plt.xlabel('Luas Tanah (m²)')
plt.title('Harga Rata-rata Berdasarkan Luas Tanah')

plt.show()

"""## **6. Korelasi**"""

data_filtered.sample(5)

data_filtered.info()

# Menghitung nilai korelasi
correlation_matrix = data_filtered.corr()
print("Nilai Korelasi:\n", correlation_matrix)

# Membuat visualisasi korelasi menggunakan heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap Korelasi Antar Variabel')
plt.show()

"""## **7. Modeling (Linear Regression)**"""

# Pisahkan fitur dan target
X = data_filtered[['bed', 'bath', 'listing-floorarea (m²)', 'harga listing-floorarea per m²']]
y = data_filtered['price']

# Split data menjadi training dan testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardisasi fitur
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Polynomial Features
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

# Menampilkan bentuk dari setiap subset data
print("Bentuk X_train:", X_train.shape)
print("Bentuk X_test:", X_test.shape)
print("Bentuk y_train:", y_train.shape)
print("Bentuk y_test:", y_test.shape)

# Inisialisasi model regresi linear
model = LinearRegression()

# Latih model dengan data training yang telah distandarisasi
model.fit(X_train_scaled, y_train)

# Nilai konstanta (intercept) dan koefisien regresi
a = model.intercept_
b = model.coef_

print("Constanta (a):", a)
print("Koefisien regresi (b):", b)

"""Nilai Konstanta(a) = 2601235003.8757515

Nilai koefisien (b1)= 5.24982678e+07, (b2) = 2.53100556e+07 , (b3) = 1.21519039e+09, (b4) = 5.96469527e+08

Sehingga model regresi yang didapat adalah

==> Y = 2601235003.8757515 +  5.24982678e+07.X1 + 2.53100556e+07.X2 + 1.21519039e+09.X3 + 5.96469527e+08.X4
"""

model.get_params()

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('poly', PolynomialFeatures()),
    ('regressor', LinearRegression())
])

# Define the hyperparameters and their values
param_grid = {
    'poly__degree': [5, 6, 7, 8, 9, 10],  # Polynomial degrees to test
    'regressor__copy_X': [True, False],
    'regressor__fit_intercept': [True, False],
    'regressor__n_jobs': [1, 5, 10, 15, None],
    'regressor__positive': [True, False]
}

# Initialize GridSearchCV
grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1)

# Fit the model
grid_search.fit(X_train, y_train)

# Best parameters
print("Best parameters found: ", grid_search.best_params_)

# Best estimator
best_model = grid_search.best_estimator_

# Evaluate the model
print("Test set score: ", best_model.score(X_test, y_test))

# prompt: check best_model r squared dan rmse

import numpy as np
from sklearn.metrics import r2_score, mean_squared_error

# Predict on test data
y_pred = best_model.predict(X_test)

# Calculate R^2 score
r2_score_model = r2_score(y_test, y_pred)

# Calculate RMSE
rmse_model = np.sqrt(mean_squared_error(y_test, y_pred))

# Print results
print("R^2 score:", r2_score_model)
print("RMSE:", rmse_model)

"""## **8. Visualisasi Grafik Linear**"""

# Prediksi nilai harga berdasarkan data testing yang telah distandarisasi
y_pred = model.predict(X_test_scaled)

# Visualisasi data actual vs prediksi
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, edgecolors=(0, 0, 0))
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=3)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted Prices')
plt.show()

"""## **9. Evaluasi (Nilai Data Actual dan Nilai Data Prediksi)**"""

# Tampilkan nilai data actual dan prediksi dalam bentuk tabel
result = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(result)

"""## **10.  Uji Akurasi Model Linear Regression**"""

importance = model.coef_
for i, feature in enumerate(X_train.columns):
    print(f"{feature}: {importance[i]}")

# Visualisasi feature importance
plt.figure(figsize=(10, 6))
sns.barplot(x=X_train.columns, y=importance)
plt.title('Feature Importance')
plt.show()

# Ranking feature importance
importance_ranking = pd.DataFrame({'Feature': X_train.columns, 'Importance': importance}).sort_values(by='Importance', ascending=False)
print(importance_ranking)

"""Berdasarkan analisis kepentingan fitur, luas area rumah (listing-floorarea) dan harga per meter persegi (harga listing-floorarea per m²) menonjol sebagai faktor terpenting yang mempengaruhi prediksi harga rumah, dengan nilai kepentingan masing-masing sekitar 1.215190e+09 dan 5.964695e+08. Fitur jumlah kamar tidur (bed) dan jumlah kamar mandi (bath) juga memberikan kontribusi yang signifikan, meskipun dalam tingkat kepentingan yang lebih rendah dengan nilai masing-masing sekitar 5.249827e+07 dan 2.531006e+07. Analisis ini menunjukkan bahwa luas area dan harga per meter persegi adalah faktor yang paling berpengaruh dalam variasi harga rumah, dengan jumlah kamar tidur dan kamar mandi juga berperan penting dalam penentuan harga rumah."""

# Hitung metrik evaluasi
r_squared = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("R-squared:", r_squared)
print("RMSE:", rmse)

"""Hasil analisis menunjukkan bahwa model yang digunakan memiliki tingkat kemampuan yang cukup baik dalam menjelaskan variasi harga rumah, dengan nilai R-squared sebesar 0.75, yang berarti sekitar 75.24% dari variabilitas harga rumah dapat dijelaskan oleh model. Namun, nilai RMSE yang cukup besar sebesar 890,850,537 menandakan bahwa terdapat nilai selisih yang signifikan dalam satuan harga rumah.

RMSE sebesar 890,850,536 dalam konteks harga rumah maksimum sebesar 8,800,000,000 menunjukkan bahwa kesalahan prediksi rata-rata sekitar 10% dari harga maksimum yang mungkin. Ini bisa dianggap sebagai kesalahan yang relatif kecil dalam konteks nilai yang sangat besar seperti ini.
"""

bedrooms = int(input("Enter the number of bedrooms: "))
bathrooms = int(input("Enter the number of bathrooms: "))
area = float(input("Enter the area in square meters: "))
price_per_meter = float(input("Enter the price per square meter: "))

# Create a list of features
features = [bedrooms, bathrooms, area, price_per_meter]

# Convert the list to a NumPy array
features_array = np.array(features).reshape(1, -1)

# Predict the price using the model
predicted_price = model.predict(features_array)[0]

# Print the predicted price
print(f"Predicted price: Rp. {predicted_price:.2f}")



"""## model alternatif (random forest)"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest Regressor": RandomForestRegressor(),
    "Gradient Boosting Regressor": GradientBoostingRegressor(),
    "Neural Networks": MLPRegressor(hidden_layer_sizes=(100,), activation='relu', solver='adam', max_iter=1000),
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Model: {name}")
    print(f"R-squared: {r2:.3f}")
    print(f"RMSE: {rmse:.3f}")
    print(f"MAE: {mae:.3f}")
    print()

from sklearn.ensemble import RandomForestRegressor

# Inisialisasi model RandomForestRegressor
model_rf = RandomForestRegressor()

# Latih model dengan data training
model_rf.fit(X_train, y_train)

# Prediksi nilai harga berdasarkan data testing
y_pred_rf = model_rf.predict(X_test)

# Hitung nilai R^2
r2_rf = r2_score(y_test, y_pred_rf)

# Print hasil
print("R^2 using RandomForestRegressor:", r2_rf)

# prompt: atur cari polynomial degrees pada model rf

import numpy as np
# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline
pipeline_rf = Pipeline([
    ('scaler', StandardScaler()),
    ('poly', PolynomialFeatures()),
    ('regressor', RandomForestRegressor())
])

# Define the hyperparameters and their values
param_grid_rf = {
    'poly__degree': [1,2,3,4,5,6,7,8,9,10],  # Polynomial degrees to test
    'regressor__n_estimators': [100, 200, 300],
    'regressor__max_depth': [None, 5, 10],
}

# Initialize GridSearchCV
grid_search_rf = GridSearchCV(pipeline_rf, param_grid_rf, cv=5, n_jobs=-1)

# Fit the model
grid_search_rf.fit(X_train, y_train)

# Best parameters
print("Best parameters found: ", grid_search_rf.best_params_)

# Best estimator
best_model_rf = grid_search_rf.best_estimator_

# Evaluate the model
print("Test set score: ", best_model_rf.score(X_test, y_test))

# Predict on test data
y_pred_rf = best_model_rf.predict(X_test)

# Calculate R^2 score
r2_score_model_rf = r2_score(y_test, y_pred_rf)

# Calculate RMSE
rmse_model_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))

# Print results
print("R^2 score:", r2_score_model_rf)
print("RMSE:", rmse_model_rf)

# Hitung nilai RMSE model_rf
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))

# Print hasil
print("RMSE model_rf:", rmse_rf)

# Prediksi nilai harga menggunakan model_rf
y_pred_rf = model_rf.predict(X_test)

# Visualisasi data actual vs prediksi menggunakan model_rf
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_rf, edgecolors=(0, 0, 0))
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=3)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted Prices (Random Forest)')
plt.show()

# prompt: uji prediksi model_rf user input

import numpy as np
bedrooms = int(input("Enter the number of bedrooms: "))
bathrooms = int(input("Enter the number of bathrooms: "))
area = float(input("Enter the area in square meters: "))
price_per_meter = float(input("Enter the price per square meter: "))

# Create a list of features
features = [bedrooms, bathrooms, area, price_per_meter]

# Convert the list to a NumPy array
features_array = np.array(features).reshape(1, -1)

# Predict the price using the model
predicted_price = model_rf.predict(features_array)[0]

# Print the predicted price
print(f"Predicted price: Rp. {predicted_price:.2f}")