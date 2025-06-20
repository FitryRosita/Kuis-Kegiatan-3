import streamlit as st
import joblib

# Konfigurasi halaman
st.set_page_config(page_title="🎮 Kuis Interaktif - Kegiatan 3", page_icon="🎮")

# Judul dan Caption
st.title("🎮 Kuis Interaktif - Kegiatan 3")
st.caption("Topik: Frekuensi Harapan (Etnomatematika — Cublak‑Cublak Suweng)")

# Input Nama
nama = st.text_input("Masukkan nama kamu terlebih dahulu:")

if nama:
    st.success(f"Halo, {nama}!")
    st.markdown("### 📌 Petunjuk Pengerjaan")
    st.write("- Bacalah soal dengan saksama.")
    st.write("- Pilih jawaban yang menurutmu benar.")
    st.write("- Setelah selesai, klik tombol **Kirim Jawaban**.")
    
    if st.button("✅ Saya Sudah Siap"):
        # Soal dan Jawaban
        soal_pilgan = [
            {
                "soal": "1. Pak Budi mengorganisir permainan cublak-cublak suweng untuk 9 anak (8 pemain + 1 pak empo) pada acara 17 Agustus di kampungnya. Permainan akan dilakukan sebanyak 56 ronde. Hitung frekuensi harapan terjadinya pergantian penebak!",
                "opsi": ["A. 8", "B. 7", "C. 3", "D. 4"],
                "jawaban": "B"
            },
            {
                "soal": "2. Berdasarkan soal nomor 1, hitunglah frekuensi harapan penebak tetap dalam posisinya!",
                "opsi": ["A. 35", "B. 42", "C. 63", "D. 49"],
                "jawaban": "D"
            },
            {
                "soal": "3. Dalam tradisi Jawa, permainan cublak-cublak suweng sering dimainkan saat bulan purnama. Sebuah grup yang terdiri dari 6 orang (5 pemain + 1 pak empo) bermain selama 3 jam dengan rata-rata 1 ronde per 2 menit. Tentukan frekuensi harapan pergantian pak empo!",
                "opsi": ["A. 18", "B. 19", "C. 20", "D. 21"],
                "jawaban": "A"
            },
            {
                "soal": "4. Sebuah dadu khusus memiliki sisi-sisi bernomor: 2, 2, 3, 4, 5, dan 6. Jika dadu dilempar 120 kali, berapa kali diperkirakan akan muncul angka genap?",
                "opsi": ["A. 80", "B. 60", "C. 90", "D. 75"],
                "jawaban": "A"
            },
            {
                "soal": "5. Sebuah kantong berisi 12 permen: 5 rasa jeruk, 4 rasa stroberi, dan 3 rasa anggur. Jika satu permen diambil acak dalam 60 percobaan, berapa kali diperkirakan permen rasa anggur yang akan terambil?",
                "opsi": ["A. 5", "B. 10", "C. 15", "D. 20"],
                "jawaban": "C"
            },
            {
                "soal": "6. Seseorang melempar dua koin sebanyak 40 kali. Frekuensi harapan munculnya satu angka dan satu gambar adalah ⋯ kali.",
                "opsi": ["A. 5", "B. 10", "C. 15", "D. 20"],
                "jawaban": "D"
            }
        ]

        jawaban_pengguna = []
        st.markdown("### 📝 Soal Kuis")
        for idx, soal in enumerate(soal_pilgan):
            st.markdown(soal["soal"])
            pilihan = st.radio(
                f"Jawaban soal {idx + 1}",
                soal["opsi"],
                key=idx
            )
            jawaban_pengguna.append(pilihan[0])  # Ambil huruf A/B/C/D saja

        if st.button("📨 Kirim Jawaban"):
            skor = 0
            st.markdown("### 📊 Hasil Kuis")
            for i, jawaban in enumerate(jawaban_pengguna):
                benar = soal_pilgan[i]["jawaban"]
                soal_teks = soal_pilgan[i]["soal"]
                if jawaban == benar:
                    skor += 1
                    st.success(f"Soal {i+1}: ✅ Benar! (Jawaban: {benar})")
                else:
                    st.error(f"Soal {i+1}: ❌ Salah. Jawaban yang benar adalah {benar}.")

            nilai = int((skor / len(soal_pilgan)) * 100)
            st.markdown("---")
            st.markdown(f"**Nama:** {nama}")
            st.markdown(f"**Jawaban Benar:** {skor} dari {len(soal_pilgan)} soal")
            st.markdown(f"🎉 **Nilai Akhir: {nilai}/100**")
