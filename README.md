# Deteksi Penyakit Tanaman Jagung Menggunakan CNN

## Deskripsi Proyek

Proyek ini bertujuan untuk mengembangkan model Convolutional Neural Network (CNN) yang dapat mendeteksi penyakit pada tanaman jagung berdasarkan gambar daun. Dengan menggunakan dataset gambar daun jagung yang telah diberi label, model ini akan dilatih untuk mengenali berbagai jenis penyakit yang umum terjadi pada tanaman jagung, seperti hawar daun, bercak daun, dan busuk batang. Hasil dari proyek ini diharapkan dapat membantu petani dalam mengidentifikasi penyakit pada tanaman jagung secara cepat dan akurat, sehingga dapat mengambil tindakan pencegahan yang tepat untuk meningkatkan hasil panen.

## Dataset

Dataset yang digunakan dalam proyek ini terdiri dari gambar daun jagung yang telah diberi label dengan jenis penyakit yang sesuai. Dataset ini mencakup berbagai kondisi daun, termasuk daun sehat dan daun yang terinfeksi oleh berbagai penyakit. Setiap gambar dalam dataset ini memiliki resolusi yang cukup tinggi untuk memastikan bahwa detail penting pada daun dapat dikenali oleh model CNN. Dataset ini dibagi menjadi dua bagian: data pelatihan (training set) dan data pengujian (testing set), dengan proporsi 80% untuk pelatihan dan 20% untuk pengujian.

## Arsitektur Model

Model CNN yang digunakan dalam proyek ini terdiri dari beberapa lapisan konvolusi, lapisan pooling, dan lapisan fully connected. Arsitektur model ini dirancang untuk mengekstraksi fitur penting dari gambar daun jagung dan mengklasifikasikan jenis penyakit yang ada. Lapisan konvolusi digunakan untuk mendeteksi pola dan fitur pada gambar, sementara lapisan pooling membantu mengurangi dimensi data dan meningkatkan efisiensi model. Lapisan fully connected digunakan untuk menggabungkan fitur yang diekstraksi dan menghasilkan output klasifikasi akhir. Model ini juga menggunakan teknik regularisasi seperti dropout untuk mencegah overfitting dan meningkatkan generalisasi model.

## Hasil dan Evaluasi

Setelah melatih model CNN dengan dataset gambar daun jagung, hasil evaluasi menunjukkan bahwa model ini memiliki akurasi yang tinggi dalam mendeteksi penyakit pada tanaman jagung. Evaluasi dilakukan menggunakan metrik seperti akurasi, precision, recall, dan F1-score untuk mengukur kinerja model dalam mengklasifikasikan jenis penyakit. Hasil evaluasi menunjukkan bahwa model ini mampu mengenali berbagai jenis penyakit dengan tingkat akurasi yang memuaskan, sehingga dapat digunakan sebagai alat bantu bagi petani dalam mengidentifikasi penyakit pada tanaman jagung secara efektif.

## Kesimpulan

Proyek ini berhasil mengembangkan model CNN yang efektif dalam mendeteksi penyakit pada tanaman jagung berdasarkan gambar daun. Dengan menggunakan dataset yang representatif dan arsitektur model yang tepat, model ini mampu mencapai akurasi yang tinggi dalam mengklasifikasikan berbagai jenis penyakit. Hasil dari proyek ini dapat memberikan manfaat besar bagi petani dalam mengidentifikasi penyakit pada tanaman jagung secara cepat dan akurat, sehingga dapat meningkatkan hasil panen dan mengurangi kerugian akibat penyakit. Proyek ini juga membuka peluang untuk pengembangan lebih lanjut, seperti penggunaan teknik augmentasi data atau arsitektur model yang lebih kompleks untuk meningkatkan kinerja deteksi penyakit pada tanaman jagung.

## Tool dan Teknologi

[!Python](https://img.shields.io/badge/Python-3.8-blue)] [![TensorFlow](https://img.shields.io/badge/TensorFlow-2.4-orange)](https://www.tensorflow.org/) [![Keras](https://img.shields.io/badge/Keras-2.4-red)](https://keras.io/) [![NumPy](https://img.shields.io/badge/NumPy-1.19-green)](https://numpy.org/) [![Matplotlib](https://img.shields.io/badge/Matplotlib-3.3-purple)](https://matplotlib.org/) [![Stramlit](https://img.shields.io/badge/Streamlit-0.80-yellow)](https://streamlit.io/)

