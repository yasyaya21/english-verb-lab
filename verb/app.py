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
elif menu == "📝 Latihan Interaktif":
    st.header("Latihan Interaktif: Isi Bentuk Kata Kerja yang Tepat")
    
    # 1. Pilih Verb secara acak untuk latihan
    selected_verb = random.choice(df_verbs.values.tolist())
    v1, v2, v3 = selected_verb
    
    # 2. Tentukan Jenis Latihan (Misalnya: Tebak V2 dan V3 dari V1)
    st.subheader(f"Kata Kerja Dasar (V1): **{v1.upper()}**")
    
    st.markdown("---")

    # Kolom untuk Input Jawaban
    col_input1, col_input2 = st.columns(2)

    with col_input1:
        # Latihan V2
        st.subheader("Apa bentuk V2-nya?")
        jawaban_v2 = st.text_input("V2 (Past Simple):", key="v2_input").strip().lower()
        if st.button("Cek V2"):
            if jawaban_v2 == v2:
                st.success(f"🎉 **Benar!** Bentuk V2 dari '{v1}' adalah **{v2}**.")
            elif jawaban_v2 == "":
                 st.warning("Silakan isi jawaban Anda.")
            else:
                st.error(f"❌ **Salah!** Coba lagi. Jawaban yang benar adalah **{v2}**.")
            st.session_state["v2_checked"] = True

    with col_input2:
        # Latihan V3
        st.subheader("Apa bentuk V3-nya?")
        jawaban_v3 = st.text_input("V3 (Past Participle):", key="v3_input").strip().lower()
        if st.button("Cek V3"):
            if jawaban_v3 == v3:
                st.success(f"🎉 **Benar!** Bentuk V3 dari '{v1}' adalah **{v3}**.")
            elif jawaban_v3 == "":
                 st.warning("Silakan isi jawaban Anda.")
            else:
                st.error(f"❌ **Salah!** Coba lagi. Jawaban yang benar adalah **{v3}**.")
            st.session_state["v3_checked"] = True

    st.markdown("---")
    
    # Tombol untuk Soal Baru
    if st.button("🔄 Soal Baru"):
        st.experimental_rerun() # Memuat ulang halaman untuk soal baru
elif menu == "🏆 Kuis":
    st.header("Kuis: Tentukan Verb yang Tepat dalam Kalimat")
    
    # Pastikan session state untuk skor ada
    if 'score' not in st.session_state:
        st.session_state['score'] = 0
    
    # Contoh Soal Kuis
    quiz_questions = [
        {"sentence": "She has never ___ a famous person before.", "answer": "seen", "options": ["see", "saw", "seen"], "correct_form": "V3"},
        {"sentence": "They ___ to the beach yesterday.", "answer": "went", "options": ["go", "gone", "went"], "correct_form": "V2"},
        {"sentence": "I usually ___ coffee in the morning.", "answer": "drink", "options": ["drank", "drunk", "drink"], "correct_form": "V1"}
    ]
    
    # Ambil 1 soal acak
    if 'current_quiz' not in st.session_state or st.session_state.current_quiz is None:
        st.session_state.current_quiz = random.choice(quiz_questions)

    question = st.session_state.current_quiz
    
    st.markdown(f"**Soal:** {question['sentence'].replace('___', '...')}")
    
    # Input Pilihan Ganda (Select Box)
    user_choice = st.radio(
        "Pilih jawaban yang paling tepat:",
        question["options"],
        key="quiz_radio"
    )
    
    if st.button("Kirim Jawaban"):
        if user_choice == question["answer"]:
            st.success(f"✅ **Jawaban Benar!** ({question['correct_form']}). Kalimat ini menggunakan **Perfect Tense** (has + V3).")
            st.session_state['score'] += 1
        else:
            st.error(f"❌ **Jawaban Salah.** Jawaban yang benar adalah **{question['answer']}**.")
        
        # Reset soal untuk pertanyaan berikutnya
        st.session_state.current_quiz = None
    
    st.markdown("---")
    st.subheader(f"Skor Anda: **{st.session_state['score']}**")
    
    if st.button("Lanjut Soal Berikutnya", disabled=st.session_state.current_quiz is not None):
        st.session_state.current_quiz = random.choice(quiz_questions)
        st.experimental_rerun()
