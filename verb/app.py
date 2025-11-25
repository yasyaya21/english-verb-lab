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
st.title("🧪 Virtual Lab: Three Forms of Verbs (V1, V2, V3)")
st.caption("Pelajari dan Latih Penggunaan Kata Kerja Bahasa Inggris")

# Sidebar untuk Navigasi
menu = st.sidebar.radio(
    "Pilih Menu",
    ("📚 Materi", "📝 Latihan Interaktif", "🏆 Kuis")
)
st.sidebar.markdown("---")
st.sidebar.markdown("**Dibuat dengan Python & Streamlit**")

# --- Konten Halaman Berdasarkan Pilihan Menu ---
if menu == "📚 Materi":
    st.header("Materi: Penggunaan V1, V2, dan V3")
    st.markdown("""
    Kata kerja (verb) dalam Bahasa Inggris sering berubah bentuk tergantung waktu (tenses) kalimat.
    """)

    # Penjelasan Ringkas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("V1 (Base Form) - Present")
        st.info("Digunakan untuk Simple Present Tense, perintah (imperative), dan setelah modal (will, can, must).")
        st.markdown("> *Contoh: I **go** to school every day.*")
    with col2:
        st.subheader("V2 (Past Simple) - Past")
        st.warning("Digunakan untuk Simple Past Tense, menunjukkan aksi yang selesai di masa lalu.")
        st.markdown("> *Contoh: She **ate** pizza last night.*")
    with col3:
        st.subheader("V3 (Past Participle) - Perfect/Passive")
        st.error("Digunakan untuk Perfect Tenses (Have/Has/Had + V3) dan kalimat pasif (Passive Voice).")
        st.markdown("> *Contoh: They have **written** a book.*")

    st.markdown("---")
    st.subheader("Tabel Irregular Verbs (Contoh)")
    st.dataframe(df_verbs, use_container_width=True)
    st.info("💡 **Tips:** Sebagian besar *regular verbs* hanya menambahkan -ed/-d untuk V2 dan V3 (e.g., *play-played-played*).")
