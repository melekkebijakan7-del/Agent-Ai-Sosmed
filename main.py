import os
from datetime import datetime

os.makedirs("docs", exist_ok=True)
current_year = datetime.now().year
min_year = current_year - 4 # Standar referensi jurnal maksimal 5 tahun terakhir
current_date = datetime.now().strftime("%A, %d %B %Y")

# Endpoint Formspree Anda yang asli
formspree_endpoint = "https://formspree.io/f/mrppodkg"

# Template HTML Halaman Utama dengan Form Suara Rakyat
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
        .suara-rakyat {{ background: var(--bg-light); padding: 25px; border-top: 4px solid var(--primary-red); margin-top: 20px; border-radius: 4px; }}
        .suara-rakyat h3 {{ margin-bottom: 15px; color: var(--dark-bg); font-size: 20px; }}
        .suara-rakyat p {{ font-size: 13px; color: #555; margin-bottom: 15px; }}
        .form-group {{ margin-bottom: 12px; }}
        .form-group label {{ display: block; font-weight: bold; font-size: 13px; margin-bottom: 4px; }}
        .form-group input[type="text"], .form-group input[type="email"], .form-group textarea {{ width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; font-size: 13px; }}
        .form-group input[type="file"] {{ padding: 5px 0; font-size: 12px; }}
        .btn-submit {{ background: var(--primary-red); color: white; border: none; padding: 10px; font-size: 15px; font-weight: bold; cursor: pointer; border-radius: 4px; width: 100%; }}
        .btn-submit:hover {{ background: #b01c24; }}
    </style>
</head>
<body>
    <div class="top-bar">{current_date} | Portal Jurnalisme Investigasi & Kontrol Kebijakan</div>
    <header>
        <div class="main-header">
            <a href="index.html" class="logo">Melek<span>Kebijakan</span></a>
        </div>
        <nav>
            <div class="nav-container">
                <a href="index.html">Kritik Utama</a>
                <a href="#">Bedah Pasal</a>
                <a href="#">Gugatan MK</a>
                <a href="#">Korupsi & Anggaran</a>
            </div>
        </nav>
    </header>

    <div class="container">
        <main>
            <div class="card">
                <div class="meta-tag">BEDAH PASAL CACAT (Rujukan Min. Tahun {min_year})</div>
                <h2><a href="#">Analisis Yuridis: Sengkarut Pasal Karet UU ITE Terbaru dan Ancaman Demokrasi</a></h2>
                <p>Mengupas tuntas kecacatan regulasi berdasarkan Jurnal Hukum Tata Negara terkait ambiguitas frasa pencemaran nama baik...</p>
            </div>
            
            <div class="card">
                <div class="meta-tag">GUGATAN KONSTITUSIONAL</div>
                <h2><a href="#">Sidang MK Perkara No. 45/PUU-2026: Mengawal Gugatan Rakyat Atas Monopoli SDA</a></h2>
                <p>Tuntutan pemohon memiliki pijakan rasional yang kuat didukung oleh literatur hukum agraria mutakhir...</p>
            </div>
            
            <div class="card">
                <div class="meta-tag">KORUPSI & ANGGARAN</div>
                <h2><a href="#">Vonis Ringan Koruptor: Mencederai Nalar Keadilan Publik</a></h2>
                <p>Analisis persidangan menunjukkan ketimpangan antara kerugian negara triliunan rupiah dengan putusan hakim...</p>
            </div>
        </main>

        <aside>
            <!-- FORMULIR SUARA RAKYAT -->
            <div class="suara-rakyat">
                <h3>🗣️ Suara Rakyat (Laporan Publik)</h3>
                <p>Laporkan masalah publik, jalan rusak, atau kebijakan cacat. <strong>Wajib melampirkan foto/dokumen bukti nyata.</strong> Laporan tanpa bukti tidak akan diproses.</p>
                
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
                        <textarea name="pesan" rows="3" required placeholder="Jelaskan masalah secara detail (lokasi, kronologi, dll)"></textarea>
                    </div>
                    <div class="form-group">
                        <label>Lampirkan Bukti (Wajib Foto/Dokumen) 🔴</label>
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

print("Skrip utama berhasil dijalankan dengan Formspree Endpoint.")
