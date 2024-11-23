import streamlit as st
import numpy as np
import pandas as pd

# Simulasi model prediksi (contoh sederhana)
def predict_bike_usage(temp, hum, weathersit, workingday):
    # Model sederhana (contoh hanya untuk ilustrasi)
    # Korelasi logis: suhu dan kondisi cuaca memengaruhi penggunaan sepeda
    base_count = 200  # rata-rata penggunaan sepeda
    weather_effect = {1: 1.2, 2: 0.9, 3: 0.5, 4: 0.3}  # faktor cuaca
    workingday_effect = 1.1 if workingday == 1 else 0.8

    count = base_count * (1 + (temp - 0.5)) * (1 - hum) * weather_effect.get(weathersit, 0.5) * workingday_effect
    return max(int(count), 0)  # Hindari nilai negatif

# Layout aplikasi
st.title("Analisis dan Prediksi Penggunaan Sepeda")

# Sidebar input
st.sidebar.header("Masukkan Parameter")
temp = st.sidebar.slider("Suhu (temp, skala 0-1):", min_value=0.0, max_value=1.0, step=0.01, value=0.5)
hum = st.sidebar.slider("Kelembapan (hum, skala 0-1):", min_value=0.0, max_value=1.0, step=0.01, value=0.5)
weathersit = st.sidebar.selectbox("Kondisi Cuaca (1: Cerah, 2: Berawan, 3: Hujan, 4: Salju)", [1, 2, 3, 4])
workingday = st.sidebar.radio("Hari Kerja (1: Ya, 0: Tidak)", [1, 0])

# Prediksi penggunaan sepeda
predicted_count = predict_bike_usage(temp, hum, weathersit, workingday)

# Hasil output
st.header("Prediksi Penggunaan Sepeda")
st.metric("Jumlah Penggunaan Sepeda", f"{predicted_count} sepeda")

# Informasi tambahan
st.subheader("Parameter yang Dimasukkan:")
st.write(f"- **Suhu**: {temp}")
st.write(f"- **Kelembapan**: {hum}")
st.write(f"- **Kondisi Cuaca**: {weathersit} ({'Cerah' if weathersit == 1 else 'Berawan' if weathersit == 2 else 'Hujan' if weathersit == 3 else 'Salju'})")
st.write(f"- **Hari Kerja**: {'Ya' if workingday == 1 else 'Tidak'}")
