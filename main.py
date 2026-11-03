import os
from datetime import datetime

os.makedirs("docs", exist_ok=True)
current_year = datetime.now().year
min_year = current_year - 4 # Batas minimal tahun referensi (maksimal 5 tahun terakhir)
current_date = datetime.now().strftime("%A, %d %B %Y")

# =====================================================================
# BAGIAN 1: SISTEM PROMPT UNTUK AGEN AI (PANDUAN KETAT)
# (Jika Anda menghubungkan skrip ini ke API AI seperti Gemini/OpenAI, 
# gunakan prompt di bawah ini untuk men-generate artikelnya).
# =====================================================================

prompt_bedah_pasal = f"""
Buat 1 artikel jurnalistik investigatif tentang BEDAH PASAL CACAT di Indonesia hari ini.
Syarat mutlak:
1. Pasal harus NYATA dan sedang berlaku (misal UU ITE, UU Cipta Kerja, KUHP Baru).
2. Argumen perlawanan harus berbobot dan rasional.
3. WAJIB cantumkan kutipan dari sumber hukum kuat (Jurnal Hukum atau Buku) dengan tahun terbit minimal {min_year}.
4. Gaya bahasa profesional, kritis, ala Hukumonline.
"""

prompt_gugatan_mk = f"""
Buat 1 artikel tentang GUGATAN KONSTITUSIONAL di Mahkamah Konstitusi (MK) yang sedang hangat.
Syarat mutlak:
1. Kasus dan nomor perkara harus NYATA.
2. Bahas tuntutan pemohon. Jika baik, berikan dukungan argumentasi hukum yang kuat.
3. WAJIB gunakan referensi jurnal/buku hukum terbitan {min_year}-{current_year} sebagai pondasi argumen.
"""

prompt_korupsi = f"""
Buat 1 artikel tentang KASUS KORUPSI DAN ANGGARAN yang sedang disidangkan.
Syarat mutlak:
1. Kasus nyata (misal korupsi timah, BTS, dll).
2. Bahas jalan persidangan, dakwaan, dan kerugian negara secara detail.
3. Berikan analisis kritis: Apakah tuntutan/putusan hakim sudah pas? Jika belum, berikan alasan hukumnya secara mendetail berdasarkan doktrin hukum pidana terbaru (referensi minimal {min_year}).
"""

# =====================================================================
# BAGIAN 2: TEMPLATE HTML HALAMAN UTAMA (Dengan Form Suara Rakyat)
# =====================================================================

# PENTING: Ganti "YOUR_FORMSPREE_ID" dengan ID dari formspree.io Anda nanti.
formspree_endpoint = "https://formspree.io/f/YOUR_FORMSPREE_ID"

index_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Melek Kebijakan - Suara Kritis & Perlawanan Publik</title>
    <style>
        :root {{ --primary-red: #d9232d; --dark-bg: #111111; --border-color: #e0e0e0; --bg-light: #f7f7f7; }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: Arial, sans-serif; }}
        body {{ background-color: #ffffff; color: #222; line-height: 1.5; }}
        header {{ border-bottom: 3px solid var(--primary-red); position: sticky; top: 0; background: #fff; z-index: 1000; }}
        .top-bar {{ background: var(--dark-bg); color: #fff; padding: 6px 20px; font-size: 12px; }}
        .main-header {{ display: flex; justify-content: space-between; padding: 15px 20px; max-width: 1200px; margin: 0 auto; }}
        .logo {{ font-size: 26px; font-weight: bold; color: var(--primary-red); text-decoration: none; }}
        .logo span {{ color: var(--dark-bg); }}
        nav {{ background: var(--dark-bg); }}
        .nav-container {{ max-width: 1200px; margin: 0 auto; display: flex; gap: 15px; padding: 10px 20px; }}
        nav a {{ color: #fff; text-decoration: none; font-size: 14px; font-weight: bold; }}
        nav a:hover {{ color: var(--primary-red); }}
        
        .container {{ max-width: 1200px; margin: 20px auto; padding: 0 15px; display: grid; grid-template-columns: 2fr 1fr; gap: 30px; }}
        .card {{ border-bottom: 1px solid var(--border-color); padding-bottom: 20px; margin-bottom: 20px; }}
        .meta-tag {{ font-size: 12px; color: var(--primary-red); font-weight: bold; margin-bottom: 5px; }}
        .card h2 {{ font-size: 24px; margin-bottom: 10px; }}
        .card h2 a {{ color: #111; text-decoration: none; }}
        .card h2 a:hover {{ color: var(--primary-red); }}
        
        /* Form Suara Rakyat */
        .suara-rakyat {{ background: var(--bg-light); padding: 25px; border-top: 4px solid var(--primary-red); margin-top: 40px; }}
        .suara-rakyat h3 {{ margin-bottom: 15px; color: var(--dark-bg); font-size: 22px; }}
        .suara-rakyat p {{ font-size: 14px; color: #555; margin-bottom: 20px; }}
        .form-group {{ margin-bottom: 15px; }}
        .form-group label {{ display: block; font-weight: bold; font-size: 14px; margin-bottom: 5px; }}
        .form-group input[type="text"], .form-group input[type="email"], .form-group textarea {{ width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; }}
        .form-group input[type="file"] {{ padding: 10px 0; }}
        .btn-submit {{ background: var(--primary-red); color: white; border: none; padding: 12px 20px; font-size: 16px; font-weight: bold; cursor: pointer; border-radius: 4px; width: 100%; }}
        .btn-submit:hover {{ background: #b01c24; }}
    </style>
</head>
<body>
    <div class="top-bar">{current_date} | Portal Jurnalisme Investigasi Hukum</div>
    <header>
        <div class="main-header">
            <a href="#" class="logo">Melek<span>Kebijakan</span></a>
        </div>
        <nav>
            <div class="nav-container">
                <a href="#">Bedah Pasal</a>
                <a href="#">Gugatan MK</a>
                <a href="#">Korupsi & Anggaran</a>
            </div>
        </nav>
    </header>

    <div class="container">
        <main>
            <div class="card">
                <div class="meta-tag">BEDAH PASAL CACAT</div>
                <h2><a href="#">Analisis Yuridis: Sengkarut Pasal Karet UU ITE Terbaru dan Ancaman Demokrasi</a></h2>
                <p>Mengupas tuntas kecacatan regulasi berdasarkan Jurnal Hukum Tata Negara (2025) terkait ambiguitas frasa pencemaran nama baik...</p>
            </div>
            
            <div class="card">
                <div class="meta-tag">GUGATAN KONSTITUSIONAL</div>
                <h2><a href="#">Sidang MK Perkara No. 45/PUU-2026: Mengawal Gugatan Rakyat Atas Monopoli SDA</a></h2>
                <p>Tuntutan pemohon memiliki pijakan rasional yang kuat didukung oleh literatur hukum agraria mutakhir...</p>
            </div>
            
            <div class="card">
                <div class="meta-tag">KORUPSI & ANGGARAN</div>
                <h2><a href="#">Vonis Ringan Koruptor Bansos: Mencederai Nalar Keadilan Publik</a></h2>
                <p>Analisis persidangan hari ini menunjukkan ketimpangan antara kerugian negara triliunan rupiah dengan putusan hakim...</p>
            </div>
        </main>

        <aside>
            <!-- FORMULIR SUARA RAKYAT -->
            <div class="suara-rakyat">
                <h3>🗣️ Suara Rakyat (Lapor Regulasi/Masalah Publik)</h3>
                <p>Laporkan masalah publik, jalan rusak, atau kebijakan cacat di daerah Anda. <strong>Wajib melampirkan foto/dokumen bukti nyata.</strong> Jika valid, akan kami jadikan berita utama.</p>
                
                <!-- Action form mengarah ke Formspree untuk menyembunyikan Email & menghubungkan ke WA -->
                <form action="{formspree_endpoint}" method="POST" enctype="multipart/form-data">
                    <div class="form-group">
                        <label>Nama Lengkap (Sesuai KTP)</label>
                        <input type="text" name="nama" required placeholder="Masukkan nama Anda">
                    </div>
                    <div class="form-group">
                        <label>Email Aktif</label>
                        <input type="email" name="email" required placeholder="emailanda@gmail.com">
                    </div>
                    <div class="form-group">
                        <label>Pesan / Detail Masalah Publik</label>
                        <textarea name="pesan" rows="4" required placeholder="Jelaskan masalah secara detail (lokasi, kronologi, dll)"></textarea>
                    </div>
                    <div class="form-group">
                        <label>Lampirkan Bukti (Wajib foto/dokumen nyata) 🔴</label>
                        <input type="file" name="bukti" accept="image/*,.pdf" required>
                    </div>
                    <input type="hidden" name="_subject" value="LAPORAN BARU SUARA RAKYAT - Melek Kebijakan">
                    <button type="submit" class="btn-submit">Kirim Laporan & Bukti</button>
                </form>
            </div>
        </aside>
    </div>
</body>
</html>
"""

with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print(f"Sistem Melek Kebijakan berhasil di-generate. Standar referensi minimal tahun: {min_year}.")
