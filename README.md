**README**

**Prediksi Penggunaan Daya Menggunakan LSTM**

Repository ini berisi kode Python untuk memprediksi penggunaan daya menggunakan jaringan saraf Long Short-Term Memory (LSTM).
deret waktu untuk memprediksi daya setelah setiap 60 hari konsumsi energi.

Dataset yang diperlukan dapat ditemukan di PowerAep2.csv yang akan di hasilkan,
Dataset ini telah dibuat dengan mengedit Kumpulan Data Global Tata Nasional.

 Kode terbagi menjadi dua bagian: satu diimplementasikan dalam skrip Python (`untitled.ipynb`) dan yang lainnya dalam sebuah Jupyter Notebook (`power_prediction.py`).

Berikut adalah panduan tentang cara menggunakan setiap bagian:

### Dependencies
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Keras (dengan backend TensorFlow)
- scikit-learn

### Instruksi untuk `untitled.ipynb`

1. **Import Library**: Impor pustaka yang diperlukan, termasuk Pandas, NumPy, Matplotlib, dan Keras.

2. **Memuat Data**: Muat dataset pelatihan dan pengujian (`PowerTrain.csv` dan `PowerTest.csv`, masing-masing) menggunakan Pandas.

3. **Pra-pemrosesan Data**:
   - Skala data pelatihan antara 0 dan 1 menggunakan MinMaxScaler dari scikit-learn.
   - Siapkan data pelatihan dengan membuat urutan input dan output untuk model LSTM.

4. **Membangun Model LSTM**:
   - Buat model Sequential menggunakan Keras.
   - Tambahkan lapisan LSTM dengan dropout untuk regularisasi.
   - Kompilasi model menggunakan optimizer Adam dan fungsi loss mean squared error.
   - Latih model pada data pelatihan untuk jumlah epoch yang ditentukan.

5. **Memprediksi Penggunaan Daya**:
   - Siapkan data pengujian dengan cara yang sama seperti data pelatihan.
   - Gunakan model yang dilatih untuk memprediksi penggunaan daya untuk data pengujian.
   - Balikkan transformasi nilai yang diprediksi untuk mendapatkan kembali skala aslinya.

6. **Visualisasi Hasil**:
   - Plot penggunaan daya aktual berbanding dengan penggunaan daya yang diprediksi menggunakan Matplotlib.

### Instruksi untuk `power_prediction.py`

1. **Import Library**: Impor pustaka yang diperlukan, termasuk Pandas, NumPy, Matplotlib, dan Keras.

2. **Memuat Data**: Muat dataset pelatihan dan pengujian (`PowerTrain.csv` dan `PowerTest.csv`, masing-masing) menggunakan Pandas.

3. **Pra-pemrosesan Data**:
   - Skala data pelatihan antara 0 dan 1 menggunakan MinMaxScaler dari scikit-learn.
   - Siapkan data pelatihan dengan membuat urutan input dan output untuk model LSTM.

4. **Membangun Model LSTM**:
   - Buat model Sequential menggunakan Keras.
   - Tambahkan lapisan LSTM dengan dropout untuk regularisasi.
   - Kompilasi model menggunakan optimizer Adam dan fungsi loss mean squared error.
   - Latih model pada data pelatihan untuk jumlah epoch yang ditentukan.

5. **Memprediksi Penggunaan Daya**:
   - Siapkan data pengujian dengan cara yang sama seperti data pelatihan.
   - Gunakan model yang dilatih untuk memprediksi penggunaan daya untuk data pengujian.
   - Balikkan transformasi nilai yang diprediksi untuk mendapatkan kembali skala aslinya.

6. **Visualisasi Hasil**:
   - Plot penggunaan daya aktual berbanding dengan penggunaan daya yang diprediksi menggunakan Matplotlib.

### Penggunaan

1. Klone repository:
   ```bash
   git clone <https://github.com/Yoga913/Prediksi-Konsumsi-Energi-berbasis-ML>
   ```
2. Instal dependensi menggunakan pip:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan Jupyter Notebook `untitled.ipynb` atau eksekusi skrip Python `power_prediction.py`.

### Catatan

Pastikan dataset pelatihan dan pengujian (`PowerTrain.csv` dan `PowerTest.csv`) berada dalam direktori yang sama dengan file kode.

### Lisensi

Proyek ini dilisensikan di bawah [Lisensi MIT](LICENSE).


