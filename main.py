import os
from datetime import datetime

# 1. PERSIAPAN FOLDER & VARIABEL
os.makedirs("docs", exist_ok=True)
current_year = str(datetime.now().year)
min_year = str(datetime.now().year - 4)
current_date = datetime.now().strftime("%A, %d %B %Y")
formspree_endpoint = "https://formspree.io/f/mrppodkg"

# =====================================================================
# 2. DATA KONTEN BERITA (PANJANG & MENDALAM)
# =====================================================================

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
pasal_ref = "1. Prof. Eddy O.S. Hiariej (2023), <em>\"Asas Legalitas dan Penafsiran Hukum Pidana dalam Konteks Cyber Law\"</em>, Jurnal Hukum Pidana Indonesia.<br>2. Bivitri Susanti (2024), <em>\"Otoritarianisme Berwajah Legislasi: Matinya Demokrasi Substansial\"</em>, Pustaka Hukum Tata Negara."

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
mk_ref = "1. Prof. Saldi Isra (2023), <em>\"Peran MK dalam Melindungi Hak Ekonomi dan Sosial Warga Negara dari Invasi Regulasi Neoliberal\"</em>, Jurnal Konstitusi.<br>2. Pusat Studi Hukum dan Kebijakan (2024), <em>\"Kritik Metodologis Omnibus Law dalam Perspektif Hak Asasi Manusia dan Perlindungan Pekerja\"</em>."

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
korupsi_ref = "1. Prof. Hibnu Nugroho (2023), <em>\"Paradigma Pemiskinan Koruptor dalam Hukum Pidana Ekonomi dan Pemulihan Aset\"</em>, Prenada Media.<br>2. ICW & Kemitraan (2024), <em>\"Eksaminasi Publik Terhadap Putusan Bebas dan Ringan Kasus Megakorupsi: Matinya Nalar Keadilan\"</em>."


# =====================================================================
# 3. TEMPLATE HTML MENGGUNAKAN STRING BIASA (BEBAS ERROR)
# =====================================================================

index_template = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>melek.kebijakan.id - Portal Jurnalisme Investigasi & Analisis Hukum</title>
    <style>
        /* CSS Modern: Palet Warna & Animasi */
        :root { 
            --primary-red: #c61a22; 
            --dark-navy: #1e293b; 
            --light-bg: #f1f5f9; 
            --card-bg: #ffffff;
            --text-main: #334155;
            --border-color: #e2e8f0;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        body { background-color
