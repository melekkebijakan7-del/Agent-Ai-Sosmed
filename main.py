import os
from datetime import datetime

# Memastikan folder docs tersedia
os.makedirs("docs", exist_ok=True)

current_date = datetime.now().strftime("%A, %d %B %Y")

# Data Berita Otomatis (Nantinya bisa dihubungkan ke AI API Anda untuk generate otomatis)
news_title = "Celah Konstitusional dan Muatan Politis: Mengapa Regulasi Baru Ini Wajib Dilawan Melalui Judicial Review?"
news_excerpt = "Aliansi masyarakat sipil dan pakar hukum menegaskan pentingnya perlawanan total terhadap produk hukum pemerintah yang cacat substansi. Regulasi ini dinilai mencederai rasa keadilan dan berpotensi memberangus hak-hak dasar warga negara."
news_category = "Investigasi Hukum & Regulasi"
news_image = "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=1000&q=80"
news_filename = "berita-1.html"

# 1. TEMPLATE HALAMAN UTAMA (INDEX.HTML)
index_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Melek Kebijakan - Suara Kritis & Perlawanan Publik</title>
    <style>
        :root {{
            --primary-red: #d9232d;
            --dark-bg: #111111;
            --border-color: #e0e0e0;
            --text-main: #222222;
            --text-muted: #666666;
            --bg-light: #f7f7f7;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: Arial, sans-serif; }}
        body {{ background-color: #ffffff; color: var(--text-main); line-height: 1.5; }}
        
        header {{ border-bottom: 3px solid var(--primary-red); background: #ffffff; position: sticky; top: 0; z-index: 1000; }}
        .top-bar {{ background: var(--dark-bg); color: #fff; padding: 6px 20px; font-size: 12px; display: flex; justify-content: space-between; }}
        .main-header {{ display: flex; align-items: center; justify-content: space-between; padding: 15px 20px; max-width: 1200px; margin: 0 auto; }}
        .logo {{ font-size: 26px; font-weight: bold; color: var(--primary-red); text-decoration: none; text-transform: uppercase; }}
        .logo span {{ color: var(--dark-bg); }}
        
        nav {{ background: var(--dark-bg); }}
        .nav-container {{ max-width: 1200px; margin: 0 auto; display: flex; overflow-x: auto; }}
        nav a {{ color: #ffffff; text-decoration: none; padding: 12px 15px; font-size: 14px; white-space: nowrap; font-weight: bold; }}
        nav a:hover, nav a.active {{ background: var(--primary-red); }}

        .container {{ max-width: 1200px; margin: 20px auto; padding: 0 15px; display: grid; grid-template-columns: 2fr 1fr; gap: 30px; }}
        @media(max-width: 768px) {{ .container {{ grid-template-columns: 1fr; }} }}

        .trending {{ background: var(--bg-light); padding: 10px 20px; margin-bottom: 20px; border-left: 4px solid var(--primary-red); font-size: 14px; display: flex; gap: 15px; align-items: center; max-width: 1200px; margin: 15px auto; }}
        .trending span {{ font-weight: bold; color: var(--primary-red); text-transform: uppercase; font-size: 12px; }}

        .headline-card {{ border-bottom: 1px solid var(--border-color); padding-bottom: 20px; margin-bottom: 20px; }}
        .headline-card img {{ width: 100%; height: auto; max-height: 400px; object-fit: cover; border-radius: 4px; margin-bottom: 15px; }}
        .headline-card h1 {{ font-size: 26px; margin-bottom: 10px; color: #111; }}
        .headline-card h1 a {{ color: inherit; text-decoration: none; }}
        .headline-card h1 a:hover {{ color: var(--primary-red); }}
        .meta {{ font-size: 12px; color: var(--primary-red); font-weight: bold; margin-bottom: 10px; }}
        .excerpt {{ font-size: 15px; color: #444; }}

        .sidebar {{ background: var(--bg-light); padding: 20px; border-radius: 4px; border-top: 3px solid var(--dark-bg); }}
        .sidebar h3 {{ font-size: 18px; margin-bottom: 15px; border-bottom: 2px solid #ddd; padding-bottom: 8px; color: var(--dark-bg); }}
        .pop-item {{ display: flex; gap: 12px; margin-bottom: 15px; align-items: flex-start; }}
        .pop-number {{ font-size: 24px; font-weight: bold; color: var(--primary-red); line-height: 1; }}
        .pop-text a {{ font-size: 14px; text-decoration: none; color: #333; font-weight: bold; }}
        .pop-text a:hover {{ color: var(--primary-red); }}
        .pop-meta {{ font-size: 11px; color: var(--text-muted); margin-top: 4px; }}

        footer {{ background: var(--dark-bg); color: #aaa; margin-top: 40px; padding: 30px 20px; font-size: 13px; text-align: center; }}
        footer p {{ margin-bottom: 8px; }}
    </style>
</head>
<body>

    <div class="top-bar">
        <div>{current_date}</div>
        <div>Suara Keras Perlawanan Publik & Kontrol Kebijakan</div>
    </div>

    <header>
        <div class="main-header">
            <a href="index.html" class="logo">Melek<span>Kebijakan</span></a>
            <div style="font-size: 14px; color: var(--text-muted);">Investigasi Regulasi & Perlawanan Publik</div>
        </div>
        <nav>
            <div class="nav-container">
                <a href="index.html" class="active">Kritik Utama</a>
                <a href="#">Bedah Pasal Cacat</a>
                <a href="#">Gugatan Konstitusional</a>
                <a href="#">Korupsi & Anggaran</a>
                <a href="#">Suara Rakyat</a>
            </div>
        </nav>
    </header>

    <div class="trending">
        <span>Fokus Perlawanan:</span>
        <a href="{news_filename}" style="color: #333; text-decoration: none; font-size: 14px;">Menolak Pasal Karet yang Membungkam Kebebasan</a>
    </div>

    <div class="container">
        <main>
            <div class="headline-card">
                <div class="meta">{news_category} | Melawan Arogansi Regulasi Pemerintah</div>
                <img src="{news_image}" alt="Ilustrasi Hukum dan Regulasi">
                <h1><a href="{news_filename}">{news_title}</a></h1>
                <p class="excerpt">{news_excerpt}</p>
            </div>
        </main>

        <aside class="sidebar">
            <h3>Sorotan Perlawanan</h3>
            <div class="pop-item">
                <div class="pop-number">1</div>
                <div class="pop-text">
                    <a href="{news_filename}">Daftar Pasal Karet dalam UU Terbaru yang Siap Digugat ke Mahkamah Konstitusi</a>
                    <div class="pop-meta">Hukum • 2 jam lalu</div>
                </div>
            </div>
        </aside>
    </div>

    <footer>
        <p>&copy; 2026 Melek Kebijakan Indonesia. Benteng Perlawanan & Kontrol Kebijakan Publik.</p>
        <p>Lawan Regulasi Cacat, Tegakkan Keadilan Hukum!</p>
    </footer>

</body>
</html>
"""

# 2. TEMPLATE HALAMAN DETAIL BERITA (BERITA-1.HTML)
article_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{news_title} - Melek Kebijakan</title>
    <style>
        :root {{
            --primary-red: #d9232d;
            --dark-bg: #111111;
            --border-color: #e0e0e0;
            --text-main: #222222;
            --text-muted: #666666;
            --bg-light: #f7f7f7;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: Arial, sans-serif; }}
        body {{ background-color: #ffffff; color: var(--text-main); line-height: 1.8; }}
        
        header {{ border-bottom: 3px solid var(--primary-red); background: #ffffff; position: sticky; top: 0; z-index: 1000; }}
        .top-bar {{ background: var(--dark-bg); color: #fff; padding: 6px 20px; font-size: 12px; display: flex; justify-content: space-between; }}
        .main-header {{ display: flex; align-items: center; justify-content: space-between; padding: 15px 20px; max-width: 900px; margin: 0 auto; }}
        .logo {{ font-size: 26px; font-weight: bold; color: var(--primary-red); text-decoration: none; text-transform: uppercase; }}
        .logo span {{ color: var(--dark-bg); }}
        
        .article-container {{ max-width: 800px; margin: 30px auto; padding: 0 20px; }}
        .category {{ color: var(--primary-red); font-weight: bold; font-size: 14px; text-transform: uppercase; margin-bottom: 10px; }}
        h1.article-title {{ font-size: 32px; line-height: 1.3; color: #111; margin-bottom: 15px; }}
        .article-meta {{ font-size: 13px; color: var(--text-muted); border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color); padding: 10px 0; margin-bottom: 25px; }}
        
        .featured-image {{ width: 100%; height: auto; border-radius: 4px; margin-bottom: 10px; }}
        .image-caption {{ font-size: 12px; color: var(--text-muted); text-align: center; margin-bottom: 30px; font-style: italic; }}

        .article-content p {{ font-size: 17px; margin-bottom: 20px; color: #333; text-align: justify; }}
        .article-content h3 {{ font-size: 20px; color: var(--dark-bg); margin: 30px 0 15px 0; border-left: 4px solid var(--primary-red); padding-left: 10px; }}
        
        .resistance-box {{ background: var(--bg-light); border-left: 4px solid var(--primary-red); padding: 20px; margin: 30px 0; font-size: 16px; font-style: italic; color: #111; }}

        .back-btn {{ display: inline-block; margin-top: 40px; padding: 10px 20px; background: var(--dark-bg); color: #fff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 14px; }}
        .back-btn:hover {{ background: var(--primary-red); }}

        footer {{ background: var(--dark-bg); color: #aaa; margin-top: 60px; padding: 30px 20px; font-size: 13px; text-align: center; }}
    </style>
</head>
<body>

    <div class="top-bar">
        <div>{current_date}</div>
        <div>Portal Berita Investigasi & Kontrol Kebijakan</div>
    </div>

    <header>
        <div class="main-header">
            <a href="index.html" class="logo">Melek<span>Kebijakan</span></a>
            <a href="index.html" style="color: #333; text-decoration: none; font-size: 14px; font-weight: bold;">← Kembali ke Beranda</a>
        </div>
    </header>

    <div class="article-container">
        <div class="category">{news_category}</div>
        <h1 class="article-title">{news_title}</h1>
        
        <div class="article-meta">
            Oleh: Tim Investigasi Melek Kebijakan | Editor: Redaksi Hukum Publik<br>
            {current_date}
        </div>

        <img src="{news_image}" alt="Ilustrasi Aksi Perlawanan Regulasi" class="featured-image">
        <div class="image-caption">Ilustrasi: Pembahasan regulasi pemerintah yang dinilai cacat prosedur dan memicu gelombang penolakan dari koalisi masyarakat sipil.</div>

        <div class="article-content">
            <p><strong>JAKARTA —</strong> Gelombang penolakan keras terhadap produk hukum dan regulasi terbaru yang diterbitkan oleh pemerintah terus bergulir. Sejumlah pakar hukum tata negara, aliansi akademisi, serta koalisi masyarakat sipil menyatakan mosi tidak percaya dan bersiap melayangkan gugatan uji materiil (judicial review) ke Mahkamah Konstitusi (MK).</p>

            <p>{news_excerpt}</p>

            <h3>Celah Hukum dan Ancaman Bagi Hak Sipil</h3>
            <p>Dalam kajian mendalam yang dilakukan oleh lembaga pemerhati kebijakan, ditemukan setidaknya lima pasal krusial yang bersifat ambigu (multitafsir). Pasal-pasal ini memberikan kewenangan berlebihan tanpa batasan pengawasan yang jelas kepada aparat, sehingga membuka ruang lebar bagi terjadinya kriminalisasi terhadap warga.</p>

            <div class="resistance-box">
                "Kita tidak boleh tinggal diam menghadapi arogansi legislasi yang mengabaikan partisipasi bermakna. Regulasi yang lahir tanpa mendengarkan aspirasi rakyat adalah bentuk pengkhianatan terhadap konstitusi, dan perlawanan hukum adalah harga mati."
            </div>

            <h3>Mengapa Perlawanan Melalui Jalur Konstitusional Wajib Dilakukan?</h3>
            <p>Perlawanan terhadap produk regulasi yang cacat substansi bukan sekadar opsi, melainkan kewajiban moral dan konstitusional. Jika dibiarkan, preseden buruk ini akan terus berulang di mana produk hukum dijadikan alat kekuasaan untuk menekan kelompok kritis.</p>
        </div>

        <a href="index.html" class="back-btn">&larr; Kembali ke Beranda Utama</a>
    </div>

    <footer>
        <p>&copy; 2026 Melek Kebijakan Indonesia. Benteng Perlawanan & Kontrol Kebijakan Publik.</p>
        <p>Lawan Regulasi Cacat, Tegakkan Keadilan Hukum!</p>
    </footer>

</body>
</html>
"""

# Menyimpan file otomatis ke dalam folder docs
with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

with open(f"docs/{news_filename}", "w", encoding="utf-8") as f:
    f.write(article_html)

print("Skrip berhasil: Halaman utama dan artikel perlawanan otomatis ter-generate!")
