import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Statistik", layout="wide")

st.title("Dashboard Statistik Deskriptif")
st.write("Analisis data latihan menggunakan statistik deskriptif.")

df = pd.read_csv("data.csv")

st.subheader("Data Latihan")
st.dataframe(df, use_container_width=True)

st.subheader("Statistik Deskriptif")
st.dataframe(df.describe(), use_container_width=True)

st.subheader("Korelasi Antarvariabel")
st.dataframe(df.corr(numeric_only=True), use_container_width=True)