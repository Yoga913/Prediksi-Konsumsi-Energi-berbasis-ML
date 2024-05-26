import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

# Membaca data pelatihan dari file CSV
dataset_train = pd.read_csv('PowerAep2.csv')

# Memilih kolom 'MW' sebagai data pelatihan
training_set = dataset_train.iloc[:, 1:2].values

# Menampilkan dataset pelatihan
print(dataset_train)

# Penskalaan data menggunakan MinMaxScaler agar nilainya berada dalam rentang 0-1
sc = MinMaxScaler(feature_range=(0, 1))
training_set_scaled = sc.fit_transform(training_set)

# Menampilkan nilai setelah penskalaan
print(training_set_scaled[1974])

# Membuat input dan output untuk pelatihan model LSTM
x_train = []
y_train = []
for i in range(60, 2035):
    x_train.append(training_set_scaled[i - 60:i, 0])
    y_train.append(training_set_scaled[i, 0])
x_train, y_train = np.array(x_train), np.array(y_train)

# Menampilkan contoh input pertama
print(x_train[0])

# Reshape input untuk kompatibilitas dengan model LSTM (jumlah data, timestep, fitur)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Menampilkan jumlah timestep (60)
print(x_train.shape[1])

# Membangun model LSTM
model = Sequential()
model.add(LSTM(units=128, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=64, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=32, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=32))
model.add(Dropout(0.2))
model.add(Dense(units=1))

# Mengompilasi model dengan optimizer 'adam' dan loss function 'mean_squared_error'
model.compile(optimizer='adam', loss='mean_squared_error')

# Melatih model dengan data pelatihan, menggunakan 350 epochs dan batch_size 32
model.fit(x_train, y_train, epochs=350, batch_size=32)

# Membaca data uji dari file CSV
dataset_test = pd.read_csv('PowerTest.csv')

# Mengambil kolom 'MW' sebagai data uji
real_power_price = dataset_test.iloc[:, 1:2].values

# Menggabungkan dataset pelatihan dan dataset uji untuk memprediksi nilai uji
dataset_total = pd.concat((dataset_train['AEP_MW'], dataset_test['AEP_MW']), axis=0)

# Mengambil 60 data terakhir dari dataset total sebagai input untuk prediksi
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
inputs = inputs.reshape(-1, 1)
inputs = sc.transform(inputs)

# Membuat input untuk prediksi model LSTM
x_test = []
for i in range(60, 76):
    x_test.append(inputs[i - 60:i, 0])
x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# Melakukan prediksi menggunakan model
predicted_power = model.predict(x_test)

# Mengembalikan data hasil prediksi ke skala aslinya
predicted_power = sc.inverse_transform(predicted_power)

# Menampilkan plot hasil aktual dan prediksi
plt.plot(real_power_price, color='black', label='Actual')
plt.plot(predicted_power, color='green', label='Predicted')


# dalam setiap Komentar ini memberikan penjelasan mengenai setiap baris kode dalam program, dari pembacaan data, penskalaan, pembuatan model LSTM, hingga prediksi dan visualisasi hasil prediksi.
