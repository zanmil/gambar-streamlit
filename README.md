# 🌽 Deteksi Penyakit Daun Jagung Otomatis

Aplikasi web berbasis deep learning untuk mendeteksi penyakit pada daun jagung secara otomatis menggunakan CNN, dilengkapi rekomendasi pengobatan dari AI (Groq LLaMA).

---

## 📋 Deskripsi Proyek

Proyek ini mengembangkan model **Convolutional Neural Network (CNN)** yang dapat mendeteksi penyakit pada tanaman jagung berdasarkan gambar daun. Model diintegrasikan ke dalam aplikasi web interaktif menggunakan **Streamlit**, sehingga petani dapat dengan mudah mengupload foto daun jagung dan mendapatkan:

- ✅ Hasil deteksi penyakit secara otomatis
- 📊 Tingkat kepercayaan prediksi model
- 💊 Rekomendasi pengobatan dari AI (Groq LLaMA 3.3)

---

## 🦠 Kelas Penyakit yang Dideteksi

| Kelas | Keterangan |
|---|---|
| 🟡 Bercak Daun | Infeksi jamur yang menyebabkan bercak pada daun |
| 🔴 Busuk Daun | Pembusukan jaringan daun akibat patogen |
| 🟠 Karat Daun | Infeksi jamur *Puccinia* yang menimbulkan warna kecoklatan |
| 🟢 Sehat | Daun jagung dalam kondisi normal |

---

## 🗂️ Struktur Proyek

```
├── app.py                  # Aplikasi utama Streamlit
├── cnn_jgg_500.h5          # Model CNN (tidak di-commit, >100MB)
├── requirements.txt        # Dependensi Python
├── .env                    # API key (tidak di-commit)
├── .gitignore
└── README.md
```

---

## 🧠 Arsitektur Model

Model CNN dilatih dengan **500 epoch** menggunakan dataset gambar daun jagung berlabel. Arsitektur terdiri dari:

- **Lapisan Konvolusi** — mengekstraksi fitur visual dari gambar
- **Lapisan Pooling** — mereduksi dimensi dan meningkatkan efisiensi
- **Dropout** — mencegah overfitting
- **Fully Connected Layer** — menghasilkan output klasifikasi 4 kelas

Input gambar di-resize ke **224×224 piksel** dan dinormalisasi sebelum diprediksi.

---

## 📊 Dataset

- Format: gambar `.jpg` / `.png` daun jagung berlabel
- Pembagian: **80% training** / **20% testing**
- Kelas: Bercak Daun, Busuk Daun, Karat Daun, Sehat

---

## 🚀 Cara Menjalankan

**1. Clone repository:**
```bash
git clone https://github.com/zanmil/gambar-streamlit.git
cd gambar-streamlit
```

**2. Install dependensi:**
```bash
pip install -r requirements.txt
```

**3. Buat file `.env` dan isi API key Groq:**
```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxx
```
> Dapatkan API key gratis di https://console.groq.com

**4. Tambahkan model** `cnn_jgg_500.h5` ke folder project (download terpisah)

**5. Jalankan aplikasi:**
```bash
streamlit run app.py
```

---

## 🛠️ Teknologi yang Digunakan

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)](https://www.tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-latest-red)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3-purple)](https://console.groq.com/)
[![NumPy](https://img.shields.io/badge/NumPy-latest-green)](https://numpy.org/)
[![Pillow](https://img.shields.io/badge/Pillow-latest-yellow)](https://python-pillow.org/)

---

## ⚠️ Catatan
- API key Groq **gratis** dan bisa didapatkan di https://console.groq.com
