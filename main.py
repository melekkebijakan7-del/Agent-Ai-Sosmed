import os
from datetime import datetime

# Memastikan folder docs/ tersedia
os.makedirs("docs", exist_ok=True)

# Kalkulasi tahun
current_year = datetime.now().year
min_year = current_year - 4 
current_date = datetime.now().strftime("%A, %d %B %Y")
formspree_endpoint = "https://formspree.io/f/mrppodkg"

# =====================================================================
# DATA KONTEN BERITA (PANJANG & MENDALAM)
# =====================================================================

# --- BERITA 1: BEDAH PASAL CACAT ---
pasal_img = "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&w=1200&q=80"
pasal_title = "Analisis Yuridis: Ambiguitas Frasa 'Menyerang Kehormatan' dalam Regulasi ITE dan Ancaman Pembungkaman Hak Sipil"
pasal_content = """
<p><strong>JAKARTA —</strong> Ruang kebebasan berekspresi di Indonesia kembali menemui jalan terjal. Produk legislasi yang seharusnya menjadi instrumen ketertiban sosial, justru kerap kali menyisakan cacat bawaan pada aspek kepastian hukum (<em>rechtssicherheit</em>). Salah satu preseden terburuk dan paling banyak memakan korban dari kalangan aktivis, jurnalis, dan warga sipil adalah eksistensi norma karet dalam Undang-Undang Informasi dan Transaksi Elektronik (UU ITE), khususnya yang berkaitan dengan delik pencemaran nama baik.</p>

<h3>Pelanggaran Asas Lex Certa dan Lex Stricta</h3>
<p>Dalam paradigma hukum pidana modern, perumusan sebuah delik atau tindak pidana wajib tunduk secara mutlak pada asas <em>lex certa</em> (rumusan aturan harus jelas, tidak ambigu) dan <em>lex stricta</em> (aturan tidak boleh ditafsirkan secara analogi atau diperluas). Namun, fakta di lapangan menunjukkan hal sebaliknya. Penggunaan frasa "menyerang kehormatan" atau "pencemaran nama baik" tanpa parameter kerugian yang objektif adalah wujud kegagalan fundamental pembentuk undang-undang.</p>
<p>Kecacatan ini memberikan cek kosong kepada aparat penegak hukum. Ketika norma hukum bersifat sangat subjektif, maka pihak yang memiliki kekuasaan atau modal dapat dengan mudah memonopoli tafsir kebenaran. Aparat penegak hukum seringkali terjebak pada tafsir sepihak dari pelapor (yang mayoritas adalah pejabat atau tokoh berkuasa), yang pada akhirnya berujung pada kriminalisasi tak berdasar terhadap kelompok kritis. Ini bukan lagi soal penegakan hukum, melainkan instrumentalisasi hukum sebagai alat pemukul (<em>penal populism</em>).</p>

<h3>Chilling Effect dan Matinya Ruang Demokrasi</h3>
<p>Dampak sosiologis dari pembiaran pasal cacat ini sangat merusak. Fenomena <em>chilling effect</em> (efek jera dan ketakutan) mulai menjalar di tengah masyarakat. Warga menjadi takut untuk mengkritik kebijakan publik, melaporkan korupsi, atau sekadar menyuarakan ketidakadilan di media sosial karena bayang-bayang ancaman pidana penjara. Padahal, Mahkamah Agung dalam berbagai putusan landmark-nya telah menegaskan bahwa kritik terhadap kinerja pejabat publik tidak boleh diklasifikasikan sebagai penghinaan pribadi.</p>

<h3>Urgensi Pembangkangan Konstitusional Terukur</h3>
<p>Kajian hukum ketatanegaraan menegaskan bahwa warga negara memiliki hak konstitusional untuk menguji, memprotes, atau bahkan melawan regulasi yang secara nyata mengebiri hak-hak dasarnya sebagaimana dijamin dalam Pasal 28E UUD 1945. Pembangkangan sipil dan perlawanan litigasi (melalui <em>Judicial Review</em> ke Mahkamah Konstitusi) harus terus digelorakan. Jika dibiarkan tanpa perlawanan, norma cacat ini akan melembagakan otoritarianisme gaya baru yang berlindung di balik topeng supremasi hukum.</p>
"""
pasal_ref = f"1. Prof. Eddy O.S. Hiariej (2023), <em>\"Asas Legalitas dan Penafsiran Hukum Pidana dalam Konteks Cyber Law\"</em>, Jurnal Hukum Pidana Indonesia.<br>2. Bivitri Susanti (2024), <em>\"Otoritarianisme Berwajah Legislasi: Matinya Demokrasi Substansial\"</em>, Pustaka Hukum Tata Negara."

# --- BERITA 2: GUGATAN MK ---
mk_img = "https://images.unsplash.com/photo-1529101091764-c3526daf38fe?auto=format&fit=crop&w=1200&q=80"
mk_title = "Mengawal Sidang Mahkamah Konstitusi: Menakar Argumen Hukum Pemohon Terhadap Deregulasi yang Merugikan Pekerja"
mk_content = """
<p><strong>JAKARTA —</strong> Gedung Mahkamah Konstitusi (MK) kembali memanas. Ruang sidang yang mulia tersebut kini menjadi arena pertarungan eksistensial antara kepentingan oligarki pemodal dan hak konstitusional kelas pekerja. Gugatan uji materiil (<em>Judicial Review</em>) terhadap klaster ketenagakerjaan dalam regulasi <em>Omnibus Law</em> kembali diajukan oleh konfederasi serikat buruh bersama koalisi masyarakat sipil. Gugatan ini mengusung satu narasi besar: menolak perbudakan modern yang dilegalkan oleh negara.</p>

<h3>Cacat Formil: Pengabaian Meaningful Participation</h3>
<p>Sebelum membedah materi, kuasa hukum pemohon dengan sangat tajam menyoroti cacat formil (prosedural) dalam pembentukan undang-undang ini. Konsep <em>meaningful participation</em> (partisipasi publik yang bermakna)—yang mewajibkan pembentuk undang-undang tidak hanya mendengar, tetapi mempertimbangkan dan memberi penjelasan atas masukan publik—telah diabaikan secara brutal. Proses legislasi yang kejar tayang dan elitis ini mencerminkan watak kekuasaan yang alergi terhadap suara rakyatnya sendiri.</p>

<h3>Analisis Doktrin Kesejahteraan Sosial (Welfare State)</h3>
<p>Memasuki cacat materiil, argumen pemohon sangat solid dan berpijak kuat pada fondasi konstitusi. Kebijakan pemangkasan rasio hak pesangon, perluasan sistem kerja kontrak (<em>outsourcing</em>) yang nyaris tanpa batas jenis pekerjaan, dan kemudahan mekanisme Pemutusan Hubungan Kerja (PHK) sepihak, adalah bentuk pengingkaran negara terhadap Pasal 27 ayat (2) UUD 1945 yang mewajibkan negara menjamin penghidupan yang layak bagi kemanusiaan.</p>
<p>Dalam doktrin negara hukum kesejahteraan (<em>welfare state</em>), negara tidak boleh menjadi agen pasar bebas yang melepas kelas pekerja untuk bertarung bebas dengan korporasi raksasa tanpa perlindungan jaring pengaman (<em>safety net</em>). Deregulasi ini menempatkan buruh semata-mata sebagai komoditas atau faktor produksi murah demi memikat investor asing.</p>

<h3>Ujian Integritas bagi Hakim Konstitusi</h3>
<p>Mahkamah Konstitusi saat ini sedang diuji integritasnya. Sebagai <em>The Guardian of the Constitution</em> (Penjaga Konstitusi), kesembilan hakim konstitusi harus berani mengambil sikap progresif. Hukum tidak boleh hanya mengabdi pada pragmatisme ekonomi dan pertumbuhan investasi jangka pendek yang eksploitatif. Putusan MK nanti akan menjadi catatan sejarah: apakah Mahkamah berpihak pada konstitusi kerakyatan, atau tunduk pada dikte oligarki.</p>
"""
mk_ref = f"1. Prof. Saldi Isra (2023), <em>\"Peran MK dalam Melindungi Hak Ekonomi dan Sosial Warga Negara dari Invasi Regulasi Neoliberal\"</em>, Jurnal Konstitusi.<br>2. Pusat Studi Hukum dan Kebijakan (2024), <em>\"Kritik Metodologis Omnibus Law dalam Perspektif Hak Asasi Manusia dan Perlindungan Pekerja\"</em>."

# --- BERITA 3: KORUPSI ---
korupsi_img = "https://images.unsplash.com/photo-1593115057322-e94b77572f20?auto=format&fit=crop&w=1200&q=80"
korupsi_title = "Anomali Vonis Ringan Koruptor Keuangan Negara: Kegagalan Penerapan Teori Efek Jera dalam Peradilan Pidana"
korupsi_content = """
<p><strong>JAKARTA —</strong> Nalar keadilan masyarakat Indonesia kembali terkoyak, diinjak-injak oleh anomali putusan peradilan tindak pidana korupsi. Tren vonis ringan, pemotongan masa hukuman di tingkat banding, hingga putusan lepas (<em>onslag van alle rechtsvervolging</em>) bagi para terdakwa korupsi kelas kakap menunjukkan adanya penyakit struktural yang akut dalam sistem peradilan pidana kita. Triliunan rupiah uang rakyat dirampok, namun hukuman yang dijatuhkan bak dagelan yang tidak memiliki taring.</p>

<h3>Disparitas Tuntutan dan Rasio Decidendi Hakim</h3>
<p>Berdasarkan investigasi mendalam terhadap jalannya persidangan kasus megakorupsi terbaru, kelemahan sudah terlihat sejak penyusunan surat dakwaan oleh Jaksa Penuntut Umum. Kegagalan membuktikan unsur <em>mens rea</em> (niat jahat) dalam kejahatan korporasi seringkali dimanfaatkan secara cerdik oleh penasihat hukum terdakwa untuk menggeser tindak pidana murni menjadi sekadar kelalaian administratif bisnis (<em>business judgment rule</em>).</p>
<p>Tragisnya, majelis hakim kerap kali mengadopsi argumen pembelaan ini secara mentah-mentah. <em>Ratio decidendi</em> (pertimbangan hukum) hakim dalam memutus perkara seringkali mengabaikan konteks kerugian negara yang massif. Hakim cenderung berlindung di balik kepastian prosedural formal tekstual, namun gagal menggali keadilan substantif yang dituntut oleh masyarakat luas.</p>

<h3>Kegagalan Pemulihan Aset dan Matinya Efek Jera</h3>
<p>Korupsi pada dasarnya adalah kejahatan kalkulatif dan rasional (<em>white-collar crime</em>). Para koruptor sudah berhitung untung rugi. Jika hukuman penjara yang dijatuhkan sangat rendah, dan upaya perampasan aset (<em>asset recovery</em>) serta pengenaan pasal Tindak Pidana Pencucian Uang (TPPU) gagal mengembalikan kerugian negara secara proporsional, maka sistem hukum kita secara tidak langsung sedang "menyubsidi" kejahatan korupsi tersebut.</p>
<p>Doktrin hukum pidana kontemporer sejatinya mewajibkan penegak hukum untuk menerapkan teori <em>deterrence effect</em> (efek jera maksimal). Tanpa pemiskinan koruptor secara sistematis dan penghukuman yang sangat berat (termasuk pencabutan hak politik seumur hidup), peradilan korupsi di Indonesia hanya akan menjadi panggung teater yang menghabiskan anggaran negara tanpa pernah menyelesaikan akar masalah korupsi itu sendiri.</p>
"""
korupsi_ref = f"1. Prof. Hibnu Nugroho (2023), <em>\"Paradigma Pemiskinan Koruptor dalam Hukum Pidana Ekonomi dan Pemulihan Aset\"</em>, Prenada Media.<br>2. ICW & Kemitraan (2024), <em>\"Eksaminasi Publik Terhadap Putusan Bebas dan Ringan Kasus Megakorupsi: Matinya Nalar Keadilan\"</em>."


# =====================================================================
# TEMPLATE HTML (DENGAN CSS MODERN, WARNA & ANIMASI)
# =====================================================================

index_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>melek.kebijakan.id - Portal Jurnalisme Investigasi & Analisis Hukum</title>
    <style>
        /* CSS MODERN: Palet Warna & Animasi */
        :root {{ 
            --primary-red: #c61a22; 
            --dark-navy: #1e293b; 
            --light-bg: #f1f5f9; 
            --card-bg: #ffffff;
            --text-main: #334155;
            --border-color: #e2e8f0;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
        body {{ background-color: var(--light-bg); color: var(--text-main); line-height: 1.6; overflow-x: hidden; }}
        
        /* Animasi Fade In */
        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .animate-fade {{ animation: fadeInUp 0.8s ease-out forwards; opacity: 0; }}
        .delay-1 {{ animation-delay: 0.2s; }}
        .delay-2 {{ animation-delay: 0.4s; }}
        
        header {{ background: var(--dark-navy); box-shadow: 0 4px 15px rgba(0,0,0,0.1); position: sticky; top: 0; z-index: 1000; }}
        .top-bar {{ background: var(--primary-red); color: #fff; padding: 10px 20px; font-size: 12px; letter-spacing: 1px; text-transform: uppercase; font-weight: 700; display: flex; justify-content: space-between; }}
        .main-header {{ display: flex; justify-content: space-between; padding: 20px; max-width: 1200px; margin: 0 auto; align-items: center; }}
        
        .logo {{ font-size: 30px; font-weight: 900; color: #ffffff; text-decoration: none; letter-spacing: -1px; display: flex; align-items: center; gap: 5px; }}
        .logo span {{ color: var(--primary-red); }}
        .header-tagline {{ color: #94a3b8; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; border-left: 2px solid var(--primary-red); padding-left: 15px; }}
        
        nav {{ background: #0f172a; border-top: 1px solid rgba(255,255,255,0.1); }}
        .nav-container {{ max-width: 1200px; margin: 0 auto; display: flex; gap: 30px; padding: 15px 20px; overflow-x: auto; }}
        nav a {{ color: #cbd5e1; text-decoration: none; font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; transition: color 0.3s; }}
        nav a:hover {{ color: var(--primary-red); }}
        
        .container {{ max-width: 1200px; margin: 40px auto; padding: 0 20px; display: grid; grid-template-columns: 2fr 1fr; gap: 40px; }}
        @media(max-width: 850px) {{ .container {{ grid-template-columns: 1fr; }} .header-tagline {{ display: none; }} }}

        /* Desain Card Berita Modern */
        .card {{ background: var(--card-bg); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.06); margin-bottom: 35px; transition: transform 0.3s, box-shadow 0.3s; }}
        .card:hover {{ transform: translateY(-5px); box-shadow: 0 15px 40px rgba(0,0,0,0.1); }}
        
        /* Gambar Card & Efek Zoom */
        .card-img-wrapper {{ width: 100%; height: 250px; overflow: hidden; }}
        .card-img-wrapper img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.8s ease; }}
        .card:hover .card-img-wrapper img {{ transform: scale(1.08); }} /* Efek foto bergerak/zoom pelan */
        
        .card-content {{ padding: 25px; }}
        .meta-tag {{ display: inline-block; background: var(--primary-red); color: #fff; font-size: 11px; font-weight: 800; padding: 5px 12px; border-radius: 20px; text-transform: uppercase; margin-bottom: 15px; letter-spacing: 1px; }}
        .card h2 {{ font-size: 24px; margin-bottom: 15px; line-height: 1.4; font-weight: 900; }}
        .card h2 a {{ color: var(--dark-navy); text-decoration: none; transition: color 0.2s; }}
        .card h2 a:hover {{ color: var(--primary-red); }}
        .card p {{ font-size: 15px; color: #475569; font-family: 'Georgia', serif; line-height: 1.7; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }}

        /* Form Suara Rakyat - Desain Modern Berwarna */
        .suara-rakyat {{ background: linear-gradient(145deg, #ffffff, #f8fafc); padding: 35px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.06); position: sticky; top: 120px; border-top: 5px solid var(--primary-red); }}
        .suara-rakyat h3 {{ color: var(--dark-navy); font-size: 22px; font-weight: 900; text-transform: uppercase; margin-bottom: 10px; display: flex; align-items: center; gap: 10px; }}
        .suara-rakyat p {{ font-size: 13px; color: #64748b; margin-bottom: 25px; line-height: 1.6; padding-bottom: 15px; border-bottom: 1px solid var(--border-color); }}
        
        .form-group {{ margin-bottom: 18px; }}
        .form-group label {{ display: block; font-weight: 700; font-size: 13px; margin-bottom: 8px; color: var(--dark-navy); }}
        .form-group input, .form-group textarea {{ width: 100%; padding: 12px; border: 2px solid var(--border-color); border-radius: 8px; font-size: 14px; background: #fff; transition: all 0.3s; }}
        .form-group input:focus, .form-group textarea:focus {{ outline: none; border-color: var(--primary-red); box-shadow: 0 0 0 3px rgba(198,26,34,0.1); }}
        .btn-submit {{ background: linear-gradient(90deg, #c61a22, #9c1218); color: white; border: none; padding: 16px; font-size: 15px; font-weight: 800; cursor: pointer; border-radius: 8px; text-transform: uppercase; width: 100%; letter-spacing: 1px; transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 4px 15px rgba(198,26,34,0.3); }}
        .btn-submit:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(198,26,34,0.4); }}
        
        footer {{ background: var(--dark-navy); color: #94a3b8; margin-top: 60px; padding: 50px 20px; font-size: 14px; text-align: center; border-top: 4px solid var(--primary-red); }}
        footer strong {{ color: #fff; font-size: 18px; display: block; margin-bottom: 15px; letter-spacing: 1px; }}
    </style>
</head>
<body>
    <div class="top-bar">
        <span>{current_date}</span>
        <span>Jurnalisme Investigasi & Hukum</span>
    </div>
    <header>
        <div class="main-header">
            <a href="index.html" class="logo">melek.kebijakan<span>.id</span></a>
            <div class="header-tagline">Kritis • Objektif • Berbasis Riset &ge; {min_year}</div>
        </div>
        <nav>
            <div class="nav-container">
                <a href="index.html" style="color: var(--primary-red);">Beranda Utama</a>
                <a href="berita-pasal-cacat.html">Bedah Pasal Cacat</a>
                <a href="berita-gugatan-mk.html">Gugatan Konstitusi</a>
                <a href="berita-korupsi.html">Investigasi Korupsi</a>
            </div>
        </nav>
    </header>

    <div class="container">
        <main>
            <!-- BERITA 1 -->
            <div class="card animate-fade">
                <div class="card-img-wrapper">
                    <img src="{pasal_img}" alt="Ilustrasi Hukum dan Keadilan">
                </div>
                <div class="card-content">
                    <span class="meta-tag">BEDAH PASAL CACAT</span>
                    <h2><a href="berita-pasal-cacat.html">{pasal_title}</a></h2>
                    <p>Membongkar kecacatan legislasi yang mengabaikan asas lex certa. Kajian komprehensif ini merujuk pada literatur hukum tata negara dan kriminologi mutakhir untuk menelanjangi potensi otoritarianisme di balik pasal karet...</p>
                </div>
            </div>
            
            <!-- BERITA 2 -->
            <div class="card animate-fade delay-1">
                <div class="card-img-wrapper">
                    <img src="{mk_img}" alt="Gedung Mahkamah Konstitusi">
                </div>
                <div class="card-content">
                    <span class="meta-tag">GUGATAN MAHKAMAH KONSTITUSI</span>
                    <h2><a href="berita-gugatan-mk.html">{mk_title}</a></h2>
                    <p>Bedah tuntas legal reasoning dalam permohonan uji materiil (Judicial Review). Analisis menegaskan bahwa perlindungan hak normatif kelas pekerja adalah mandat Konstitusi yang tidak bisa digadaikan atas nama investasi...</p>
                </div>
            </div>
            
            <!-- BERITA 3 -->
            <div class="card animate-fade delay-2">
                <div class="card-img-wrapper">
                    <img src="{korupsi_img}" alt="Ilustrasi Korupsi dan Keuangan">
                </div>
                <div class="card-content">
                    <span class="meta-tag">KONTROL ANGGARAN NEGARA</span>
                    <h2><a href="berita-korupsi.html">{korupsi_title}</a></h2>
                    <p>Mendedah kelemahan konstruksi dakwaan dan rendahnya vonis hakim pada kasus megakorupsi. Argumen ini disandarkan pada teori hukum pidana korporasi dan literatur pemulihan aset negara untuk menciptakan efek jera...</p>
                </div>
            </div>
        </main>

        <aside class="animate-fade delay-1">
            <div class="suara-rakyat">
                <h3>Kanal Suara Rakyat</h3>
                <p>Laporkan kebijakan cacat, infrastruktur publik yang hancur, atau penyalahgunaan wewenang di daerah Anda. <strong>Wajib melampirkan foto/dokumen otentik.</strong> Laporan tanpa bukti akan ditolak otomatis oleh sistem redaksi.</p>
                
                <form action="{formspree_endpoint}" method="POST" enctype="multipart/form-data">
                    <div class="form-group">
                        <label>Nama Lengkap (Sesuai KTP)</label>
                        <input type="text" name="nama" required placeholder="Masukkan nama resmi Anda">
                    </d
