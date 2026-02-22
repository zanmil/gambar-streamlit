import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

# Config
st.set_page_config(page_title="Deteksi Penyakit Daun Jagung", layout="centered")

# Load model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("cnn_jgg_500.h5")

model = load_model()

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Label kelas
class_names = ['Bercak Daun', 'Busuk Daun', 'Karat Daun', 'Sehat']

# Tampilan
st.title("🌽 Deteksi Penyakit Daun Jagung Otomatis")
st.write("📷 Upload gambar daun jagung, dan sistem akan memprediksi jenis penyakit serta memberikan saran pengobatan.")

# Upload gambar
uploaded_file = st.file_uploader("Upload gambar daun jagung (.jpg, .jpeg, .png)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    st.image(image, caption="🖼️ Gambar yang Anda upload", use_container_width=True)

    # Preprocessing
    img = image.resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Prediksi
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = np.max(predictions) * 100

    # Hasil prediksi
    st.markdown("### 🧪 Hasil Deteksi:")
    st.success(f"📌 Penyakit Terdeteksi: **{predicted_class}**")
    st.info(f"🎯 Tingkat Kepercayaan: **{confidence:.2f}%**")

    # Rekomendasi obat
    if predicted_class != "Sehat":
        st.markdown("### 💊 Rekomendasi Pengobatan:")
        with st.spinner("Mencari rekomendasi dari AI..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "system",
                            "content": "Kamu adalah ahli pertanian dan penyakit tanaman jagung. Berikan rekomendasi yang praktis dan mudah dipahami petani."
                        },
                        {
                            "role": "user",
                            "content": f"Tanaman jagung saya terkena penyakit '{predicted_class}'. Berikan rekomendasi pengobatan, obat yang digunakan, dan cara pencegahannya. Maksimal 4 kalimat."
                        }
                    ],
                    max_tokens=200,
                    temperature=0.7
                )
                rekomendasi = response.choices[0].message.content
                st.success(rekomendasi)
            except Exception as e:
                st.error(f"❌ Gagal mengambil rekomendasi: {str(e)}")
    else:
        st.success("🌿 Tanaman Anda sehat. Tidak perlu pengobatan!")
