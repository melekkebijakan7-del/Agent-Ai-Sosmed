import os
from datetime import datetime

# Memastikan folder docs/ untuk GitHub Pages tersedia
os.makedirs("docs", exist_ok=True)

# Kalkulasi batas tahun referensi hukum (Maksimal 5 tahun terakhir)
current_year = datetime.now().year
min_year = current_year - 4 
current_date = datetime.now().strftime("%A, %d %B %Y")

# Endpoint Suara Rakyat (Sesuai milik Anda)
formspree_endpoint = "https://formspree.io/f/mrppodkg"

# =====================================================================
# 1. HALAMAN UTAMA (INDEX) - MELEK.KEBIJAKAN.ID
# =====================================================================
index_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MELEK.KEBIJAKAN.ID - Portal Jurnalisme Investigasi & Analisis Hukum</title>
    <style>
        :root {{ --primary-red: #c61a22; --dark-bg: #1a1a1a; --border-color: #dcdcdc; --bg-light: #f4f4f4; }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Helvetica Neue', Arial, sans-serif; }}
        body {{ background-color: #ffffff; color: #222; line-height: 1.6; }}
        
        header {{ border-bottom: 4px solid var(--primary-red); position: sticky; top: 0; background: #fff; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }}
        .top-bar {{ background: var(--dark-bg); color: #fff; padding: 8px 20px; font-size: 12px; letter-spacing: 0.5px; text-transform: uppercase; font-weight: bold; }}
        .main-header {{ display: flex; justify-content: space-between; padding: 18px 20px; max-width: 1200px; margin: 0 auto; align-items: center; }}
        
        /* LOGO BARU: MELEK.KEBIJAKAN.ID */
        .logo {{ font-size: 28px; font-weight: 900; color: var(--primary-red); text-decoration: none; letter-spacing: -0.5px; }}
        .logo span {{ color: var(--dark-bg); }}
        
        nav {{ background: var(--dark-bg); border-top: 1px solid #333; }}
        .nav-container {{ max-width: 1200px; margin: 0 auto; display: flex; gap: 25px; padding: 12px 20px; overflow-x: auto; }}
        nav a {{ color: #eee; text-decoration: none; font-size: 14px; font-weight: 700; white-space: nowrap; text-transform: uppercase; }}
        nav a:hover {{ color: var(--primary-red); }}
        
        .container {{ max-width: 1200px; margin: 30px auto; padding: 0 15px; display: grid; grid-template-columns: 2.2fr 1fr; gap: 40px; }}
        @media(max-width: 768px) {{ .container {{ grid-template-columns: 1fr; }} }}

        .card {{ border-bottom: 1px solid var(--border-color); padding-bottom: 25px; margin-bottom: 25px; }}
        .meta-tag {{ font-size: 12px; color: var(--primary-red); font-weight: 800; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }}
        .card h2 {{ font-size: 26px; margin-bottom: 12px; line-height: 1.3; font-weight: 800; }}
        .card h2 a {{ color: #111; text-decoration: none; transition: color 0.2s; }}
        .card h2 a:hover {{ color: var(--primary-red); }}
        .card p {{ font-size: 15px; color: #444; font-family: Georgia, serif; line-height: 1.6; }}

        /* Form Suara Rakyat - Profesional & Tegas */
        .suara-rakyat {{ background: var(--bg-light); padding: 30px; border-top: 5px solid var(--primary-red); box-shadow: 0 4px 6px rgba(0,0,0,0.05); }}
        .suara-rakyat h3 {{ margin-bottom: 10px; color: var(--dark-bg); font-size: 20px; font-weight: 900; text-transform: uppercase; border-bottom: 2px solid #ddd; padding-bottom: 10px; }}
        .suara-rakyat p {{ font-size: 13px; color: #555; margin-bottom: 20px; line-height: 1.5; }}
        .form-group {{ margin-bottom: 15px; }}
        .form-group label {{ display: block; font-weight: 700; font-size: 13px; margin-bottom: 6px; color: #222; }}
        .form-group input, .form-group textarea {{ width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 2px; font-size: 14px; background: #fff; }}
        .form-group input:focus, .form-group textarea:focus {{ outline: none; border-color: var(--primary-red); }}
        .btn-submit {{ background: var(--primary-red); color: white; border: none; padding: 14px; font-size: 15px; font-weight: bold; cursor: pointer; text-transform: uppercase; width: 100%; letter-spacing: 1px; transition: background 0.3s; }}
        .btn-submit:hover {{ background: #9c1218; }}
        
        footer {{ background: var(--dark-bg); color: #888; margin-top: 50px; padding: 40px 20px; font-size: 13px; text-align: center; border-top: 4px solid var(--primary-red); }}
        footer strong {{ color: #fff; font-size: 16px; display: block; margin-bottom: 10px; }}
    </style>
</head>
<body>
    <div class="top-bar">{current_date} | Portal Analisis Hukum & Perlawanan Kebijakan Independen</div>
    <header>
        <div class="main-header">
            <a href="index.html" class="logo">MELEK.KEBIJAKAN<span>.ID</span></a>
            <div style="font-size: 13px; color: #555; font-weight: bold; text-transform: uppercase;">Kritis • Objektif • Berbasis Riset</div>
        </div>
        <nav>
            <div class="nav-container">
                <a href="index.html">Beranda</a>
                <a href="berita-pasal-cacat.html">Bedah Pasal Cacat</a>
                <a href="berita-gugatan-mk.html">Gugatan MK</a>
                <a href="berita-korupsi.html">Korupsi & Anggaran</a>
            </div>
        </nav>
    </header>

    <div class="container">
        <main>
            <!-- BERITA 1: BEDAH PASAL -->
            <div class="card">
                <div class="meta-tag">BEDAH PASAL CACAT | Literasi Hukum &ge; {min_year}</div>
                <h2><a href="berita-pasal-cacat.html">Analisis Yuridis: Ambiguitas Frasa "Menyerang Kehormatan" dalam Regulasi ITE dan Ancaman Pembungkaman Hak Sipil</a></h2>
                <p>Membongkar kecacatan legislasi yang mengabaikan asas *lex certa*. Kajian komprehensif ini merujuk pada literatur hukum tata negara dan kriminologi mutakhir untuk menelanjangi potensi otoritarianisme di balik pasal karet...</p>
            </div>
            
            <!-- BERITA 2: GUGATAN MK -->
            <div class="card">
                <div class="meta-tag">KAJIAN GUGATAN KONSTITUSIONAL</div>
                <h2><a href="berita-gugatan-mk.html">Mengawal Sidang Mahkamah Konstitusi: Menakar Argumen Hukum Pemohon Terhadap Deregulasi yang Merugikan Pekerja</a></h2>
                <p>Bedah tuntas *legal reasoning* dalam permohonan uji materiil (Judicial Review). Analisis menegaskan bahwa perlindungan hak normatif adalah mandat Konstitusi yang tidak bisa digadaikan atas nama investasi...</p>
            </div>
            
            <!-- BERITA 3: KORUPSI -->
            <div class="card">
                <div class="meta-tag">KONTROL ANGGARAN & PERADILAN KORUPSI</div>
                <h2><a href="berita-korupsi.html">Anomali Vonis Ringan Koruptor Keuangan Negara: Kegagalan Penerapan Teori Efek Jera dalam Peradilan Pidana</a></h2>
                <p>Mendedah kelemahan konstruksi dakwaan dan rendahnya vonis hakim pada kasus megakorupsi. Argumen ini disandarkan pada teori hukum pidana korporasi dan literatur pemulihan aset negara...</p>
            </div>
        </main>

        <aside>
            <div class="suara-rakyat">
                <h3>🗣️ Suara Rakyat</h3>
                <p>Kanal pelaporan independen masyarakat. Laporkan kebijakan cacat, infrastruktur rusak, atau penyalahgunaan wewenang. <strong>Wajib melampirkan foto/dokumen otentik.</strong> Laporan tanpa bukti tidak akan diproses redaksi.</p>
                
                <form action="{formspree_endpoint}" method="POST" enctype="multipart/form-data">
                    <div class="form-group">
                        <label>Nama Lengkap (Sesuai KTP)</label>
                        <input type="text" name="nama" required placeholder="Masukkan nama resmi Anda">
                    </div>
                    <div class="form-group">
                        <label>Email Aktif</label>
                        <input type="email" name="email" required placeholder="email@domain.com">
                    </div>
                    <div class="form-group">
                        <label>Detail Masalah & Kronologi</label>
                        <textarea name="pesan" rows="4" required placeholder="Uraikan fakta hukum, lokasi, waktu, dan instansi yang terlibat..."></textarea>
                    </div>
                    <div class="form-group">
                        <label style="color: var(--primary-red);">Unggah Bukti (Wajib Foto/PDF) 🔴</label>
                        <input type="file" name="bukti" accept="image/*,.pdf" required>
                    </div>
                    <input type="hidden" name="_subject" value="URGENT: LAPORAN SUARA RAKYAT - MELEK.KEBIJAKAN.ID">
                    <button type="submit" class="btn-submit">Kirim Laporan Resmi</button>
                </form>
            </div>
        </aside>
    </div>

    <footer>
        <strong>MELEK.KEBIJAKAN.ID</strong>
        <p>&copy; {current_year} Hak Cipta Dilindungi. Jurnalisme Investigasi, Kajian Hukum Independen, dan Benteng Perlawanan Publik.</p>
    </footer>
</body>
</html>
"""

# =====================================================================
# TEMPLATE ARTIKEL (Fokus pada Gaya Bahasa Hukum / Jurnal)
# =====================================================================
def generate_article_html(title, category, content, reference):
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - MELEK.KEBIJAKAN.ID</title>
    <style>
        :root {{ --primary-red: #c61a22; --dark-bg: #1a1a1a; --border-color: #dcdcdc; --bg-light: #f9f9f9; }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Helvetica Neue', Arial, sans-serif; }}
        body {{ background: #fff; color: #111; line-height: 1.6; }}
        header {{ border-bottom: 4px solid var(--primary-red); background: #fff; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }}
        .main-header {{ display: flex; justify-content: space-between; padding: 18px 20px; max-width: 900px; margin: 0 auto; align-items: center; }}
        .logo {{ font-size: 24px; font-weight: 900; color: var(--primary-red); text-decoration: none; letter-spacing: -0.5px; }}
        .logo span {{ color: var(--dark-bg); }}
        
        .article-container {{ max-width: 780px; margin: 40px auto; padding: 0 20px; }}
        .category {{ color: var(--primary-red); font-weight: 800; font-size: 14px; text-transform: uppercase; margin-bottom: 12px; letter-spacing: 0.5px; }}
        h1 {{ font-size: 34px; line-height: 1.3; margin-bottom: 20px; font-weight: 900; color: #000; }}
        .meta {{ font-size: 14px; color: #555; border-top: 2px solid #000; border-bottom: 1px solid var(--border-color); padding: 12px 0; margin-bottom: 30px; font-weight: bold; }}
        
        /* GAYA TEKS ARTIKEL ALA JURNAL HUKUM */
        .content p {{ font-family: 'Georgia', serif; font-size: 18px; margin-bottom: 24px; text-align: justify; color: #222; line-height: 1.8; }}
        .content h3 {{ font-size: 22px; margin: 40px 0 15px 0; font-weight: 800; color: #000; border-bottom: 2px solid var(--border-color); padding-bottom: 5px; }}
        
        /* KOTAK REFERENSI AKADEMIS */
        .reference-box {{ background: var(--bg-light); border-left: 5px solid var(--primary-red); padding: 25px; margin: 40px 0; box-shadow: inset 0 0 10px rgba(0,0,0,0.02); }}
        .reference-box h4 {{ margin-bottom: 12px; color: #000; font-size: 16px; font-weight: 900; text-transform: uppercase; }}
        .reference-box p {{ font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #444; margin-bottom: 0; }}
        
        .back-btn {{ display: inline-block; margin-top: 40px; padding: 12px 25px; background: var(--dark-bg); color: #fff; text-decoration: none; font-weight: bold; text-transform: uppercase; font-size: 13px; letter-spacing: 1px; transition: 0.3s; }}
        .back-btn:hover {{ background: var(--primary-red); }}
        
        footer {{ background: var(--dark-bg); color: #888; margin-top: 60px; padding: 40px 20px; font-size: 13px; text-align: center; border-top: 4px solid var(--primary-red); }}
        footer strong {{ color: #fff; font-size: 16px; display: block; margin-bottom: 10px; }}
    </style>
</head>
<body>
    <header>
        <div class="main-header">
            <a href="index.html" class="logo">MELEK.KEBIJAKAN<span>.ID</span></a>
            <a href="index.html" style="color: #444; text-decoration: none; font-size: 13px; font-weight: bold; text-transform: uppercase;">← Kembali ke Beranda</a>
        </div>
    </header>

    <div class="article-container">
        <div class="category">{category}</div>
        <h1>{title}</h1>
        <div class="meta">Oleh: Dewan Redaksi & Kajian Hukum MELEK.KEBIJAKAN.ID | {current_date}</div>

        <div class="content">
            {content}
            <div class="reference-box">
                <h4>📚 Rujukan Kepustakaan (Doktrin & Jurnal Mutakhir)</h4>
                <p>{reference}</p>
            </div>
        </div>

        <a href="index.html" class="back-btn">Kembali ke Halaman Utama</a>
    </div>

    <footer>
        <strong>MELEK.KEBIJAKAN.ID</strong>
        <p>&copy; {current_year} Hak Cipta Dilindungi. Benteng Perlawanan & Kontrol Kebijakan Publik.</p>
    </footer>
</body>
</html>
"""

# Konten Artikel 1
pasal_content = """
<p><strong>JAKARTA —</strong> Produk legislasi di Indonesia kerap kali menyisakan cacat bawaan pada aspek kepastian hukum (<em>rechtssicherheit</em>). Salah satu preseden terburuk adalah eksistensi norma karet dalam UU ITE yang berulang kali direvisi namun tetap memuat ancaman terhadap iklim demokrasi. Pasal ini sering diinstrumentalisasi (digunakan sebagai alat pemukul) untuk membungkam kebebasan sipil dan kelompok kritis.</p>
<h3>Pelanggaran Asas Lex Certa dan Lex Stricta</h3>
<p>Dalam paradigma hukum pidana modern, perumusan delik wajib tunduk pada asas <em>lex certa</em> (rumusan harus jelas) dan <em>lex stricta</em> (tidak boleh ditafsirkan secara analogi). Namun, penggunaan frasa "menyerang kehormatan" adalah wujud kegagalan pembentuk undang-undang dalam memberikan batas objektif. Ketika norma hukum bersifat subjektif, aparat penegak hukum memonopoli tafsir kebenaran, yang berujung pada kriminalisasi tak berdasar.</p>
<h3>Urgensi Pembangkangan Konstitusional</h3>
<p>Kajian hukum ketatanegaraan menegaskan bahwa warga negara memiliki hak konstitusional untuk menguji atau melawan regulasi yang mengebiri hak-hak dasarnya (UUD 1945 Pasal 28). Jika dibiarkan, norma cacat ini akan melembagakan otoritarianisme gaya baru.</p>
"""
pasal_ref = f"1. Prof. Eddy O.S. Hiariej (2023), <em>\"Asas Legalitas dan Penafsiran Hukum Pidana\"</em>, Jurnal Hukum Pidana Indonesia.<br>2. Bivitri Susanti (2024), <em>\"Otoritarianisme Berwajah Legislasi: Matinya Demokrasi Substansial\"</em>, Pustaka Hukum Tata Negara."

# Konten Artikel 2
mk_content = """
<p><strong>JAKARTA —</strong> Ruang sidang Mahkamah Konstitusi (MK) kembali menjadi arena pertarungan antara kepentingan oligarki pemodal dan hak konstitusional rakyat. Gugatan uji materiil (<em>Judicial Review</em>) terhadap deregulasi ketenagakerjaan yang disisipkan melalui metode <em>Omnibus Law</em> diajukan dengan argumentasi bahwa regulasi tersebut bertentangan dengan UUD 1945.</p>
<h3>Analisis Doktrin Kesejahteraan Sosial (Welfare State)</h3>
<p>Argumen pemohon bukan sekadar keluhan normatif, melainkan berpijak pada fondasi konstitusi. Pemangkasan hak pesangon, perluasan sistem kerja kontrak (<em>outsourcing</em>) tanpa batas, dan ancaman PHK sepihak merupakan bentuk pelanggaran terhadap Pasal 27 ayat (2) UUD 1945 yang mewajibkan negara menjamin penghidupan yang layak. Mahkamah Konstitusi bertugas sebagai <em>The Guardian of the Constitution</em>, bukan pelindung kepentingan investasi yang eksploitatif.</p>
"""
mk_ref = f"1. Prof. Saldi Isra (2023), <em>\"Peran MK dalam Melindungi Hak Ekonomi dan Sosial Warga Negara\"</em>, Jurnal Konstitusi.<br>2. Pusat Studi Hukum dan Kebijakan (2024), <em>\"Kritik Metodologis Omnibus Law dalam Perspektif Hak Asasi Manusia\"</em>."

# Konten Artikel 3
korupsi_content = """
<p><strong>JAKARTA —</strong> Nalar keadilan masyarakat kembali terkoyak oleh anomali putusan peradilan tindak pidana korupsi. Tren vonis ringan, bahkan lepas (<em>onslag van alle rechtsvervolging</em>), bagi para terdakwa korupsi kelas kakap menunjukkan adanya kelemahan akut dalam sistem peradilan pidana kita, mulai dari penyusunan surat dakwaan hingga rasio decidendi (pertimbangan hukum) hakim.</p>
<h3>Kegagalan Pemulihan Aset dan Teori Efek Jera</h3>
<p>Korupsi adalah kejahatan kalkulatif (<em>white-collar crime</em>). Jika hukuman yang dijatuhkan serta perampasan aset (<em>asset recovery</em>) tidak sebanding dengan triliunan rupiah uang negara yang dirampok, maka sistem hukum secara tidak langsung "menyubsidi" kejahatan tersebut. Doktrin hukum pidana kontemporer mewajibkan hakim untuk tidak sekadar memutus berdasar kepastian prosedural, namun harus menggali keadilan substantif yang memberikan <em>deterrence effect</em> (efek jera maksimal).</p>
"""
korupsi_ref = f"1. Prof. Hibnu Nugroho (2023), <em>\"Paradigma Pemiskinan Koruptor dalam Hukum Pidana Ekonomi\"</em>, Prenada Media.<br>2. ICW & Kemitraan (2024), <em>\"Eksaminasi Publik Terhadap Putusan Bebas dan Ringan Kasus Korupsi\"</em>."


# Membuat File HTML
with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

with open("docs/berita-pasal-cacat.html", "w", encoding="utf-8") as f:
    f.write(generate_article_html("Analisis Yuridis: Ambiguitas Frasa \"Menyerang Kehormatan\" dalam Regulasi ITE dan Ancaman Pembungkaman Hak Sipil", "Bedah Pasal Cacat", pasal_content, pasal_ref))

with open("docs/berita-gugatan-mk.html", "w", encoding="utf-8") as f:
    f.write(generate_article_html("Mengawal Sidang Mahkamah Konstitusi: Menakar Argumen Hukum Pemohon Terhadap Deregulasi yang Merugikan Pekerja", "Gugatan Konstitusional", mk_content, mk_ref))

with open("docs/berita-korupsi.html", "w", encoding="utf-8") as f:
    f.write(generate_article_html("Anomali Vonis Ringan Koruptor Keuangan Negara: Kegagalan Penerapan Teori Efek Jera dalam Peradilan Pidana", "Korupsi & Anggaran", korupsi_content, korupsi_ref))

print("Sistem Jurnalisme Investigasi MELEK.KEBIJAKAN.ID berhasil di-generate!")
