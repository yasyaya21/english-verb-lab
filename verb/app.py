import streamlit as st
import pandas as pd
import random

# ==============================================================================
# 1. DATA VERBS
# ==============================================================================
full_verb_data = {
    "V1 (Base Form)": ["go", "eat", "write", "see", "take", "make", "sing", "drink", "break", "give", "speak", "do", "run"],
    "V2 (Past Simple)": ["went", "ate", "wrote", "saw", "took", "made", "sang", "drank", "broke", "gave", "spoke", "did", "ran"],
    "V3 (Past Participle)": ["gone", "eaten", "written", "seen", "taken", "made", "sung", "drunk", "broken", "given", "spoken", "done", "run"],
}

df_verbs = pd.DataFrame(full_verb_data)

# ==============================================================================
# 2. KONFIGURASI APLIKASI DAN SESSION STATE
# ==============================================================================

st.set_page_config(
    page_title="Virtual English Verb Lab - V1, V2, V3",
    layout="wide",
    initial_sidebar_state="collapsed" # Mengubah ini menjadi 'collapsed' atau 'auto'
)

# Inisialisasi Session State
if 'score' not in st.session_state:
    st.session_state['score'] = 0
if 'current_quiz' not in st.session_state:
    st.session_state['current_quiz'] = None
if 'current_verb_pair' not in st.session_state:
    st.session_state['current_verb_pair'] = random.choice(df_verbs.values.tolist())

# ==============================================================================
# 3. FUNGSI UTAMA UNTUK KUIS/LATIHAN BARU
# ==============================================================================

def generate_new_quiz():
    """Memilih soal kuis baru secara acak."""
    quiz_questions = [
        {"sentence": "She has never ___ a famous person before.", "answer": "seen", "options": ["see", "saw", "seen"], "correct_form": "V3 (Perfect Tense)"},
        {"sentence": "They ___ to the beach last summer.", "answer": "went", "options": ["go", "gone", "went"], "correct_form": "V2 (Simple Past)"},
        {"sentence": "I usually ___ coffee in the morning.", "answer": "drink", "options": ["drank", "drunk", "drink"], "correct_form": "V1 (Simple Present)"},
        {"sentence": "The glass was ___ by the careless waiter.", "answer": "broken", "options": ["break", "broke", "broken"], "correct_form": "V3 (Passive Voice)"},
        {"sentence": "Could you ___ me the salt, please?", "answer": "give", "options": ["gave", "given", "give"], "correct_form": "V1 (After Modal)"},
        {"sentence": "Have you ___ your homework yet?", "answer": "done", "options": ["do", "did", "done"], "correct_form": "V3 (Perfect Tense)"}
    ]
    st.session_state['current_quiz'] = random.choice(quiz_questions)

def generate_new_verb_pair():
    """Memilih pasangan kata kerja baru untuk latihan."""
    st.session_state['current_verb_pair'] = random.choice(df_verbs.values.tolist())

# ==============================================================================
# 4. TAMPILAN UTAMA DAN NAVIGASI MENGGUNAKAN TABS
# ==============================================================================

st.title("🧪 Virtual Lab: Three Forms of Verbs (V1, V2, V3)")
st.caption("Pelajari dan Latih Penggunaan Kata Kerja Bahasa Inggris Interaktif")

# --- MENGGANTI SIDEBAR DENGAN TABS DI BAGIAN ATAS ---
tab1, tab2, tab3 = st.tabs(["📚 Materi", "📝 Latihan Interaktif", "🏆 Kuis Konteks"])

# Menampilkan skor di bagian atas sebelum tabs
st.metric("Skor Kuis Anda Saat Ini", st.session_state['score'])
st.markdown("---")

# ==============================================================================
# 5. KONTEN TAB 1: MATERI
# ==============================================================================

with tab1:
    st.header("Materi: Penggunaan V1, V2, dan V3")
    st.markdown("---")
    
    st.info("Kata kerja (verb) dalam Bahasa Inggris memiliki tiga bentuk utama yang harus Anda kuasai, terutama untuk **Irregular Verbs**.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("1. V1 (Base Form) - Present")
        st.markdown("* **Fungsi:** Simple Present, Perintah (Imperative), setelah Modal (can, must, will, etc.).")
        st.markdown("> *Contoh: We **write** a letter. (Present)*")
    with col2:
        st.subheader("2. V2 (Past Simple) - Past")
        st.warning("Hanya digunakan untuk **Simple Past Tense**, menunjukkan aksi yang selesai di masa lalu.")
        st.markdown("> *Contoh: They **ate** lunch an hour ago. (Simple Past)*")
    with col3:
        st.subheader("3. V3 (Past Participle) - Perfect/Passive")
        st.error("Digunakan setelah **Have/Has/Had (Perfect Tenses)** atau sebagai **Passive Voice**.")
        st.markdown("> *Contoh: She has **taken** the bus. (Present Perfect)*")

    st.markdown("---")
    st.subheader("Tabel Irregular Verbs (Contoh)")
    st.dataframe(df_verbs, use_container_width=True)
    st.markdown("💡 **Tips:** Irregular verbs harus dihafalkan karena bentuk V2 dan V3-nya sering berubah total dari V1.")

# ==============================================================================
# 6. KONTEN TAB 2: LATIHAN INTERAKTIF
# ==============================================================================

with tab2:
    st.header("Latihan Interaktif: Tebak Bentuk Kata Kerja")
    st.markdown("---")
    
    v1, v2, v3 = st.session_state['current_verb_pair']
    
    st.subheader(f"Kata Kerja Dasar (V1): **{v1.upper()}**")
    st.markdown("Isi bentuk V2 dan V3 yang benar dari kata kerja di atas.")
    
    col_input1, col_input2 = st.columns(2)
    
    # Inisialisasi status cek
    if 'v2_status' not in st.session_state:
        st.session_state['v2_status'] = None
    if 'v3_status' not in st.session_state:
        st.session_state['v3_status'] = None
        
    with col_input1:
        st.subheader("V2 (Past Simple):")
        # Menggunakan key unik dengan V1 saat ini agar input reset saat soal baru
        jawaban_v2 = st.text_input("Ketik V2 di sini:", key=f"v2_input_{v1}", value="").strip().lower()
        
        if st.button("Cek V2", key="check_v2_tab2"):
            if jawaban_v2 == v2:
                st.success(f"🎉 **Benar!** V2 dari '{v1}' adalah **{v2}**.")
            else:
                st.error(f"❌ **Salah!** Coba lagi. Jawaban yang benar adalah **{v2}**.")

    with col_input2:
        st.subheader("V3 (Past Participle):")
        jawaban_v3 = st.text_input("Ketik V3 di sini:", key=f"v3_input_{v1}", value="").strip().lower()
        
        if st.button("Cek V3", key="check_v3_tab2"):
            if jawaban_v3 == v3:
                st.success(f"🎉 **Benar!** V3 dari '{v1}' adalah **{v3}**.")
            else:
                st.error(f"❌ **Salah!** Coba lagi. Jawaban yang benar adalah **{v3}**.")
                
    st.markdown("---")
    
    # Tombol Soal Baru
    if st.button("🔄 Soal Baru", key="new_verb_tab2"):
        generate_new_verb_pair()
        st.rerun() # Memuat ulang aplikasi untuk mendapatkan soal baru

# ==============================================================================
# 7. KONTEN TAB 3: KUIS KONTEKS
# ==============================================================================

with tab3:
    st.header("Kuis Konteks: Tentukan Bentuk Kata Kerja yang Tepat")
    st.markdown("Uji pemahaman Anda tentang kapan menggunakan V1, V2, atau V3 berdasarkan konteks kalimat.")
    st.markdown("---")
    
    if st.session_state['current_quiz'] is None:
        generate_new_quiz()

    question = st.session_state['current_quiz']
    
    st.markdown(f"**Soal:** Lengkapi kalimat berikut dengan bentuk kata kerja yang tepat:")
    st.subheader(f"\"{question['sentence'].replace('___', '**...**')}\"")
    
    # Input Pilihan Ganda
    user_choice = st.radio(
        "Pilih jawaban yang paling tepat:",
        question["options"],
        key=f"quiz_radio_options_{question['answer']}" # Key unik
    )
    
    if 'quiz_checked' not in st.session_state:
        st.session_state['quiz_checked'] = False
        
    # Memastikan tombol "Kirim Jawaban" hanya bisa diklik sekali per soal
    if st.button("Kirim Jawaban", key="submit_quiz_tab3"):
        if user_choice == question["answer"]:
            st.balloons()
            st.success(f"✅ **Jawaban Benar!** ({question['correct_form']}).")
            st.session_state['score'] += 1
        else:
            st.error(f"❌ **Jawaban Salah.** Jawaban yang benar adalah **{question['answer']}**.")
            
        st.info(f"**Penjelasan:** Kata kunci dalam kalimat ini menunjukkan penggunaan **{question['correct_form']}**, sehingga membutuhkan bentuk **{question['answer']}**.")
        st.session_state['quiz_checked'] = True # Menandai soal sudah dijawab
        
    st.markdown("---")
    
    if st.session_state.get('quiz_checked', False):
        if st.button("Lanjut Soal Berikutnya", key="next_quiz_tab3"):
            generate_new_quiz()
            st.session_state['quiz_checked'] = False
            st.rerun()
    else:
        st.button("Lanjut Soal Berikutnya", key="disabled_next_quiz", disabled=True)
        
    st.markdown(f"**Skor Kuis Total:** **{st.session_state['score']}**")
