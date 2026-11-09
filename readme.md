# 🛡️ Blockchain Transaction Scam Detector

Sistem deteksi risiko penipuan (*scam/fraud*) pada transaksi Web3 dan cryptocurrency secara *real-time* berbasis **Machine Learning** (Random Forest Classifier) dan kerangka kerja **CRISP-DM**.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688)
![Vue.js](https://img.shields.io/badge/Vue.js-3.0-4FC08D)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Fitur Utama
* **Real-time Inference:** Memprediksi status transaksi (**Aman** atau **Berisiko Scam**) dalam hitungan milidetik.
* **High Accuracy:** Dilatih menggunakan 20.000 data transaksi blockchain dengan akurasi model **92.53%** (Random Forest Classifier).
* **Decoupled Architecture:** Backend REST API berbasis **FastAPI** dan antarmuka web interaktif berbasis **Vue.js 3 (CDN)**.

---

## 🏗️ Struktur Repositori

```text
blockchain-scam-detector/
│
├── model_scam.pkl           # Artifact model Random Forest terlatih
├── main.py                  # Server Backend REST API (FastAPI)
├── index.html               # Antarmuka Frontend (Vue.js 3 CDN + Axios)
├── requirements.txt         # Dependency Python
└── README.md                # Dokumentasi proyek
```

---

## ⚙️ Spesifikasi Fitur Data (Input Features)

Model menerima 10 parameter numerik transaksi sebagai input:
1. `sender_wallet_age_days`: Usia dompet pengirim (hari).
2. `receiver_wallet_age_days`: Usia dompet penerima (hari).
3. `transaction_amount_usd`: Nilai nominal transaksi (USD).
4. `gas_fee_usd`: Biaya gas transaksi (USD).
5. `num_prev_transactions_sender`: Histori transaksi pengirim.
6. `num_prev_transactions_receiver`: Histori transaksi penerima.
7. `avg_txn_interval_sender_min`: Rata-rata jeda waktu antar-transaksi pengirim (menit).
8. `failed_txn_ratio_sender`: Rasio kegagalan transaksi pengirim (0.0 - 1.0).
9. `velocity_score`: Skor kecepatan frekuensi transaksi.
10. `anomaly_score`: Skor indikator kejanggalan perilaku transaksi (0.0 - 1.0).

---

## 🚀 Cara Menjalankan Aplikasi Lokal

### 1. Prasyarat
Pastikan Python 3.9+ telah terinstall di komputer kamu.

### 2. Clone Repositori & Install Dependencies
```bash
# Clone repositori ini
git clone https://github.com/USERNAME_KAMU/blockchain-scam-detector.git

# Masuk ke direktori proyek
cd blockchain-scam-detector

# Install dependencies yang dibutuhkan
pip install -r requirements.txt
```

### 3. Jalankan Backend Server (FastAPI)
```bash
uvicorn main:app --reload
```
Server backend akan berjalan di `http://127.0.0.1:8000`. Dokumentasi Swagger API interaktif dapat diakses di `http://127.0.0.1:8000/docs`.

### 4. Jalankan Antarmuka Web (Frontend)
Buka file `index.html` langsung di browser favorit kamu (Chrome/Firefox/Edge), atau gunakan ekstensi *Live Server* di VS Code.

---

## 📊 Performa Model (CRISP-DM Evaluation)

| Algoritma | Accuracy | Precision (Scam) | Recall (Scam) | Status |
| :--- | :---: | :---: | :---: | :---: |
| **Random Forest (Model Utama)** | **92.53%** | **0.45** | **0.14** | **Selected Model (`model_scam.pkl`)** |
| **Decision Tree (Pembanding)** | 88.39% | 0.23 | 0.25 | Baseline |

---

## 📝 Lisensi
Proyek ini dibuat untuk pemenuhan Tugas Besar Mata Kuliah Machine Learning dan dilisensikan di bawah [MIT License](LICENSE).