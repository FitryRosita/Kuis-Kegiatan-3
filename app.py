import streamlit as st
import joblib

# ====== Tampilan Latar Belakang dan Pengaturan ======
st.set_page_config(page_title="Kuis Kegiatan 3", page_icon="📊")
st.markdown("""
    <style>
        .stApp {
            background-color: #fff0f5;
            padding: 2rem;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Kuis Interaktif - Kegiatan 3")
st.caption("Topik: Frekuensi Harapan (Etnomatematika — Cublak‑Cublak Suweng)")

# ====== Data Soal ======
soal_pilgan = [
    {
        "soal": "1. Pak Budi mengorganisir ...  Hitung frekuensi harapan pergantian penebak!",
        "opsi": ["A. 8", "B. 7", "C. 3", "D. 4"],
        "jawaban": "B"
    },
    {
        "soal": "2. Berdasarkan soal nomor 1, hitunglah frekuensi harapan penebak tetap!",
        "opsi": ["A. 35", "B. 42", "C. 63", "D. 49"],
        "jawaban": "D"
    },
    {
        "soal": "3. ... Tentukan frekuensi harapan pergantian pak empo!",
        "opsi": ["A. 18", "B. 19", "C. 20", "D. 21"],
        "jawaban": "A"
    },
    {
        "soal": "4. Dadu khusus: 2,2,3,4,5,6. Jika dilempar 120 kali, berapa kali muncul angka genap?",
        "opsi": ["A. 80", "B. 60", "C. 90", "D. 75"],
        "jawaban": "A"
    },
    {
        "soal": "5. Kantong 12 permen: 5 jeruk, 4 stroberi, 3 anggur. Di 60 percobaan, berapa anggur?",
        "opsi": ["A. 5", "B. 10", "C. 15", "D. 20"],
        "jawaban": "C"
    },
    {
        "soal": "6. Melempar 2 koin 40 kali. Frekuensi harapan satu angka dan satu gambar adalah ... kali.",
        "opsi": ["A. 5", "B. 10", "C. 15", "D. 20"],
        "jawaban": "D"
    }
]

# ====== Input Nama dan Form Kuis ======
nama = st.text_input("Masukkan nama kamu (opsional):")

with st.form("quiz"):
    jawaban_siswa = [
        st.radio(soal["soal"], soal["opsi"], key=f"q{i}")
        for i, soal in enumerate(soal_pilgan)
    ]
    submit = st.form_submit_button("✅ Kirim Jawaban")

if submit:
    benar = sum(
        1 for i, soal in enumerate(soal_pilgan)
        if jawaban_siswa[i][0] == soal["jawaban"]
    )
    total = len(soal_pilgan)
    nilai = int((benar / total) * 100)

    # 🎈 Uji animasi berdasarkan nilai
    if nilai == 100:
        st.balloons()
    elif nilai >= 80:
        st.snow()

    st.success(f"✅ Kamu benar {benar} dari {total} soal.")
    st.info(f"📊 Nilai kamu: {nilai}/100")

    # 📝 Pembahasan per soal
    st.subheader("🔍 Pembahasan Soal")
    for i, soal in enumerate(soal_pilgan):
        jaw = jawaban_siswa[i][0]
        benar_ = soal["jawaban"]
        if jaw == benar_:
            st.write(f"✅ Soal {i+1}: Jawaban kamu *{jaw}* — **Benar**")
        else:
            st.write(f"❌ Soal {i+1}: Jawaban kamu *{jaw}* — ❗ **Salah**. Jawaban benar: *{benar_}*")

    # 💾 Simpan hasil lokal (opsional .pkl), tapi tidak dipakai/upload
    hasil = {
        "nama": nama,
        "benar": benar,
        "total": total,
        "nilai": nilai,
        "jawaban": jawaban_siswa
    }
    joblib.dump(hasil, "hasil_kuis_fitry.pkl")
