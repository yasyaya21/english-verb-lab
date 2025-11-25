import streamlit as st
import pandas as pd
import random

# --- Data Verbs (Contoh Sederhana) ---
# Dalam aplikasi nyata, ini bisa diambil dari file CSV/Excel yang lebih besar
verb_data = {
    "V1 (Base Form)": ["go", "eat", "write", "see", "take", "make", "sing", "drink"],
    "V2 (Past Simple)": ["went", "ate", "wrote", "saw", "took", "made", "sang", "drank"],
    "V3 (Past Participle)": ["gone", "eaten", "written", "seen", "taken", "made", "sung", "drunk"],
}

df_verbs = pd.DataFrame(verb_data)

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Virtual English Verb Lab",
    layout="wide",
    initial_sidebar_state="expanded"
)
