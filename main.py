import os
from datetime import datetime

# 1. SETUP DIREKTORI & VARIABEL REDAKSI
os.makedirs("docs", exist_ok=True)
current_year = str(datetime.now().year)
min_year = str(datetime.now().year - 4)
current_date = datetime.now().strftime("%A, %d %B %Y")
formspree_endpoint = "https://formspree.io/f/mrppodkg"

# =====================================================================
# 2. MODUL KONTEN INVESTIGASI (Dibuat selaras dengan standar Claude)
# =====================================================================

pasal_img = "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&w=1200&q=80"
pasal_title = "Analisis Yuridis: Ambiguitas Frasa 'Menyerang Kehormatan' dalam Regulasi ITE dan Ancaman Pembungkaman Hak Sipil"
pasal_content = """
<p><strong>JAKARTA —</strong> Ruang kebebasan berekspresi di Indonesia kembali menemui jalan terjal. Produk legislasi yang seharusnya menjadi instrumen ketertiban sosial, justru kerap kali menyisakan cacat bawaan pada aspek kepastian hukum (<em>rechtssicherheit</em>). Salah satu preseden terburuk dan paling banyak memakan korban dari kalangan aktivis, jurnalis, dan warga sipil adalah eksistensi norma karet dalam Undang-Undang Informasi dan Transaksi Elektronik (UU ITE), khususnya yang berkaitan dengan delik pencemaran nama baik.</p>
<h3>Pelanggaran Asas Lex Certa dan Lex Stricta</h3>
<p>Dalam paradigma hukum pidana modern, perumusan sebuah delik atau tindak pidana wajib tunduk secara mutlak pada asas <em>lex certa</em> (rumusan aturan harus jelas, tidak ambigu) dan <em>lex stricta</em> (aturan tidak boleh ditafsirkan secara analogi atau diperluas). Namun, fakta di lapangan menunjukkan hal sebaliknya. Penggunaan frasa "menyerang kehormatan" atau "pencemaran nama baik" tanpa parameter kerugian yang objektif adalah wujud kegagalan fundamental pembentuk undang-undang.</p>
<h3>Chilling Effect dan Matinya Ruang Demokrasi</h3>
<p>Dampak sosiologis dari pembiaran pasal cacat ini sangat merusak. Fenomena <em>chilling effect</em> (efek jera dan ketakutan) mulai menjalar di tengah masyarakat. Warga menjadi takut untuk mengkritik kebijakan publik, melaporkan korupsi, atau sekadar menyuarakan ketidakadilan di media sosial karena bayang-bayang ancaman pidana penjara.</p>
"""
pasal_ref = "1. Prof. Eddy O.S. Hiariej (2023), <em>\"Asas Legalitas dan Penafsiran Hukum Pidana\"</em>, Jurnal Hukum Pidana Indonesia.<br>2. Bivitri Susanti (2024), <em>\"Otoritarianisme Berwajah Legislasi\"</em>, Pustaka Hukum Tata Negara."

# =====================================================================
# 3. TEMPLATE UTAMA WEBSITE (melek.kebijakan.id)
# =====================================================================

index_template = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>melek.kebijakan.id - Portal Jurnalisme Investigasi & Analisis Hukum</title>
    <style>
        :root { --primary-red: #c61a22; --dark-navy: #1e293b; --light-bg: #f1f5f9; --card-bg: #ffffff; --text-main: #334155; }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }
        body { background-color: var(--light-bg); color: var(--text-main); line-height: 1.6; }
        header { background: var(--dark-navy); box-shadow: 0 4px 15px rgba(0,0,0,0.1); position: sticky; top: 0; z-index: 1000; }
        .top-bar { background: var(--primary-red); color: #fff; padding: 10px 20px; font-size: 12px; font-weight: 700; display: flex; justify-content: space-between; text-transform: uppercase; }
        .main-header { display: flex; justify-content: space-between; padding: 20px; max-width: 1200px; margin: 0 auto; align-items: center; }
        .logo { font-size: 30px; font-weight: 900; color: #fff; text-decoration: none; }
        .logo span { color: var(--primary-red); }
        nav { background: #0f172a; }
        .nav-container { max-width: 1200px; margin: 0 auto; display: flex; gap: 30px; padding: 15px 20px; overflow-x: auto; }
        nav a { color: #cbd5e1; text-decoration: none; font-size: 14px; font-weight: 700; text-transform: uppercase; }
        nav a:hover { color: var(--primary-red); }
        .container { max-width: 1200px; margin: 40px auto; padding: 0 20px; display: grid; grid-template-columns: 2fr 1fr; gap: 40px; }
        @media(max-width: 850px) { .container { grid-template-columns: 1fr; } }
        .card { background: var(--card-bg); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.06); margin-bottom: 35px; }
        .card-img-wrapper { width: 100%; height: 260px; overflow: hidden; }
        .card-img-wrapper img { width: 100%; height: 100%; object-fit: cover; }
        .card-content { padding: 25px; }
        .meta-tag { display: inline-block; background: var(--primary-red); color: #fff; font-size: 11px; font-weight: 800; padding: 5px 12px; border-radius: 20px; text-transform: uppercase; margin-bottom: 15px; }
        .card h2 { font-size: 24px; margin-bottom: 15px; font-weight: 900; }
        .card h2 a { color: var(--dark-navy); text-decoration: none; }
        .card p { font-size: 15px; color: #475569; font-family: 'Georgia', serif; }
        .suara-rakyat { background: #fff; padding: 35px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.06); border-top: 5px solid var(--primary-red); position: sticky; top: 100px; }
        .suara-rakyat h3 { color: var(--dark-navy); font-size: 20px; font-weight: 900; margin-bottom: 15px; }
        .form-group { margin-bottom: 15px; }
        .form-group label { display: block; font-weight: 700; font-size: 13px; margin-bottom: 5px; }
        .form-group input, .form-group textarea { width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; }
        .btn-submit { background: var(--primary-red); color: white; border: none; padding: 14px; font-weight: 800; width: 100%; border-radius: 6px; cursor: pointer; text-transform: uppercase; }
        footer { background: var(--dark-navy); color: #94a3b8; padding: 40px 20px; text-align: center; margin-top: 50px; border-top: 4px solid var(--primary-red); }
    </style>
</head>
<body>
    <div class="top-bar"><span>[CURRENT_DATE]</span><span>Jurnalisme Investigasi & Hukum</span></div>
    <header>
        <div class="main-header">
            <a href="index.html" class="logo">melek.kebijakan<span>.id</span></a>
            <div style="color: #94a3b8; font-size: 13px; font-weight: 600;">Kritis • Objektif • Berbasis Riset</div>
        </div>
        <nav>
            <div class="nav-container">
                <a href="index.html" style="color: var(--primary-red);">Beranda Utama</a>
                <a href="berita-pasal-cacat.html">Bedah Pasal Cacat</a>
            </div>
        </nav>
    </header>
    <div class="container">
        <main>
            <div class="card">
                <div class="card-img-wrapper"><img src="[PASAL_IMG]" alt="Ilustrasi"></div>
                <div class="card-content">
                    <span class="meta-tag">BEDAH PASAL CACAT</span>
                    <h2><a href="berita-pasal-cacat.html">[PASAL_TITLE]</a></h2>
                    <p>Membongkar kecacatan legislasi yang mengabaikan asas lex certa. Kajian komprehensif ini merujuk pada literatur hukum tata negara mutakhir...</p>
                </div>
            </div>
        </main>
        <aside>
            <div class="suara-rakyat">
                <h3>Kanal Suara Rakyat</h3>
                <p>Laporkan kebijakan publik yang merugikan. Wajib melampirkan bukti foto/dokumen.</p>
                <form action="[FORMSPREE_URL]" method="POST" enctype="multipart/form-data">
                    <div class="form-group"><label>Nama Lengkap</label><input type="text" name="nama" required></div>
                    <div class="form-group"><label>Email Aktif</label><input type="email" name="email" required></div>
                    <div class="form-group"><label>Detail Masalah</label><textarea name="pesan" rows="3" required></textarea></div>
                    <div class="form-group"><label>Unggah Bukti 🔴</label><input type="file" name="bukti" required></div>
                    <button type="submit" class="btn-submit">Kirim Laporan</button>
                </form>
            </div>
        </aside>
    </div>
    <footer><strong>melek.kebijakan.id</strong><p>&copy; [CURRENT_YEAR] Hak Cipta Dilindungi.</p></footer>
</body>
</html>
"""

article_template = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>[ARTICLE_TITLE] - melek.kebijakan.id</title>
    <style>
        :root { --primary-red: #c61a22; --dark-navy: #1e293b; }
        body { background: #f8fafc; color: #334155; font-family: 'Inter', sans-serif; line-height: 1.8; margin: 0; }
        header { background: var(--dark-navy); padding: 20px; text-align: center; border-bottom: 4px solid var(--primary-red); }
        .logo { font-size: 24px; font-weight: 900; color: #fff; text-decoration: none; }
        .logo span { color: var(--primary-red); }
        .container { max-width: 800px; margin: 40px auto; padding: 40px; background: #fff; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        h1 { font-size: 32px; font-weight: 900; color: #0f172a; margin-bottom: 20px; }
        .content p { font-family: 'Georgia', serif; font-size: 18px; margin-bottom: 20px; text-align: justify; }
        .back-btn { display: inline-block; margin-top: 30px; padding: 12px 25px; background: var(--dark-navy); color: #fff; text-decoration: none; font-weight: 800; border-radius: 6px; }
    </style>
</head>
<body>
    <header><a href="index.html" class="logo">melek.kebijakan<span>.id</span></a></header>
    <div class="container">
        <h1>[ARTICLE_TITLE]</h1>
        <div class="content">[ARTICLE_CONTENT]</div>
        <a href="index.html" class="back-btn">← Kembali ke Beranda</a>
    </div>
</body>
</html>
"""

# Render file HTML
final_index = index_template.replace("[CURRENT_DATE]", current_date).replace("[MIN_YEAR]", min_year).replace("[CURRENT_YEAR]", current_year).replace("[FORMSPREE_URL]", formspree_endpoint).replace("[PASAL_IMG]", pasal_img).replace("[PASAL_TITLE]", pasal_title)
final_article = article_template.replace("[ARTICLE_TITLE]", pasal_title).replace("[ARTICLE_CONTENT]", pasal_content)

with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(final_index)

with open("docs/berita-pasal-cacat.html", "w", encoding="utf-8") as f:
    f.write(final_article)

print("Pipeline website melek.kebijakan.id berhasil dirakit oleh agent!")
