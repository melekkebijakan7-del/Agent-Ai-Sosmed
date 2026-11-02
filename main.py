import os
import json
import requests
import datetime
import google.generativeai as genai
import cloudinary
import cloudinary.uploader

# ==========================================
# 0. KONFIGURASI API & ENVIRONMENT
# ==========================================
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
SERPER_API_KEY = os.environ.get("SERPER_API_KEY")
WA_INSTANCE_ID = os.environ.get("WA_INSTANCE_ID")
WA_API_TOKEN = os.environ.get("WA_API_TOKEN")

# Social Media Meta Graph API Keys
IG_ACCOUNT_ID = os.environ.get("INSTAGRAM_ACCOUNT_ID")
IG_ACCESS_TOKEN = os.environ.get("INSTAGRAM_ACCESS_TOKEN")

# Nomor WhatsApp Penerima sesuai Dashboard Green API Anda
OWNER_WA_NUMBER = "6282361171427@c.us"

cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET")
)

genai.configure(api_key=GEMINI_API_KEY)


# ==========================================
# 1. RESEARCHER AGENT (Fakta & Dampak Lapangan)
# ==========================================
def researcher_agent(topic_query):
    print(f"🔍 [RESEARCHER] Riset fakta & dampak lapangan: '{topic_query}'...")
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": f"dampak kerugian kebijakan {topic_query} masyarakat petani ekonomi bps"})
    headers = {'X-API-KEY': SERPER_API_KEY, 'Content-Type': 'application/json'}
    try:
        response = requests.post(url, headers=headers, data=payload, timeout=10)
        results = response.json()
        snippets = [f"• {item.get('title')}: {item.get('snippet')}" for item in results.get("organic", [])[:4]]
        return "\n".join(snippets) if snippets else "Data dampak ekonomi & sosial masyarakat."
    except Exception as e:
        print(f"⚠️ [RESEARCHER] Error riset: {e}")
        return "Riset berdasarkan dampak riil penurunan pendapatan masyarakat & harga pasar."


# ==========================================
# 2. COPYWRITER AGENT (Kritis + Dampak Nyata)
# ==========================================
def copywriter_agent(topic, research_data, revision_notes=None):
    print("✍️ [COPYWRITER] Menyusun skrip argumen kontra berbasis dampak nyata...")
    
    prompt = f"""
    Kamu adalah Copywriter Utama akun Instagram & Portal Berita @melek.kebijakan.id.
    Tugasmu menyusun skrip Reels & Narasi Artikel Berita yang KONTRA KEBIJAKAN PEMERINTAH berbasis fakta & dampak nyata.

    TOPIK: {topic}
    HASIL RISET DAMPAK:
    {research_data}

    ATURAN KETAT SKRIP:
    1. DILARANG MENOLAK ASAL-ASALAN: Kritik harus rasional, argumentatif, dan berbasis data.
    2. WAJIB BERIKAN CONTOH DAMPAK NYATA: Sebutkan secara spesifik siapa yang dirugikan (contoh: harga gabah petani anjlok, beban pajak UMKM meningkat).
    3. STRUKTUR NARASI: Hook, Konteks Kebijakan, Contoh Dampak Nyata, Argumen Kontra Kritis, Alternatif Solusi, CTA.

    Format Output JSON:
    {{
      "script_narasi": "Teks narasi lengkap artikel & Reels...",
      "caption_ig_fb": "Teks caption Instagram & Facebook + Hashtag...",
      "prompt_visual_3d": "Cute 3D claymation animation style of an Indonesian farmer standing in a dry rice field, vertical 9:16"
    }}
    """
    
    if revision_notes:
        prompt += f"\n\nCATATAN REVISI DARI OWNER: {revision_notes}. Sesuaikan skrip dan narasi dengan revisi ini."

    available_models = []
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                available_models.append(m.name)
    except Exception as e:
        print(f"⚠️ Deteksi model gagal: {e}")
        
    if not available_models:
        available_models = ['models/gemini-1.5-flash', 'models/gemini-2.5-flash']

    for model_name in available_models:
        try:
            model = genai.GenerativeModel(model_name)
            res = model.generate_content(prompt)
            if res and res.text:
                clean_text = res.text.replace("```json", "").replace("```", "").strip()
                return json.loads(clean_text)
        except Exception:
            continue
            
    raise RuntimeError("Gagal menghasilkan skrip.")


# ==========================================
# 3. SEO SPECIALIST AGENT (Optimasi Google Search)
# ==========================================
def seo_specialist_agent(topic, script_text):
    print("🚀 [SEO AGENT] Mengoptimasi SEO & Metadata Google News...")
    
    prompt = f"""
    Kamu adalah SEO Specialist untuk Portal Berita Kebijakan Publik @melek.kebijakan.id.
    Tugasmu membuat metadata SEO agar artikel berita ini menduduki peringkat #1 di Google Search.

    TOPIK KEBIJAKAN: {topic}
    ISI NARASI BERITA: {script_text}

    Buatkan output JSON valid berisi:
    1. "seo_title": Judul berita yang menarik & SEO-friendly (Gaya portal berita Kompas/Detik).
    2. "meta_description": Ringkasan berita untuk Google Search (Maksimal 155 karakter).
    3. "slug": URL slug pendek yang ramah SEO (contoh: evaluasi-kebijakan-impor-beras-2026).
    4. "keywords": 5 kata kunci terpisah koma.

    Format Output JSON:
    {{
      "seo_title": "...",
      "meta_description": "...",
      "slug": "...",
      "keywords": "..."
    }}
    """
    
    available_models = ['models/gemini-1.5-flash', 'models/gemini-2.5-flash']
    for model_name in available_models:
        try:
            model = genai.GenerativeModel(model_name)
            res = model.generate_content(prompt)
            if res and res.text:
                clean_text = res.text.replace("```json", "").replace("```", "").strip()
                return json.loads(clean_text)
        except Exception:
            continue
            
    return {
        "seo_title": f"Dampak Kebijakan {topic} Bagi Masyarakat",
        "meta_description": f"Analisis kritis dampak kebijakan {topic} berbasis fakta dan data resmi.",
        "slug": "analisis-kebijakan-publik",
        "keywords": "kebijakan publik, impor pangan, dampak ekonomi, pemerintah"
    }


# ==========================================
# 4. EDITOR AGENT (Render Visual 3D Claymation)
# ==========================================
def editor_animator_agent(prompt_visual):
    print("🎬 [EDITOR] Memproses gambar visual animasi 3D (Claymation Style)...")
    styled_prompt = f"{prompt_visual}, cute 3D claymation style, vibrant lighting, highly detailed, 9:16 vertical ratio"
    encoded_prompt = requests.utils.quote(styled_prompt)
    return f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=720&height=1280&nologo=true"


# ==========================================
# 5. PUBLISHER AGENT (Posting Website Portal)
# ==========================================
def publish_to_website_portal(content_data, visual_url, seo_data):
    print("📰 [WEB PUBLISHER] Menerbitkan berita ke situs portal melek.kebijakan.id...")
    
    docs_dir = "docs"
    berita_dir = os.path.join(docs_dir, "berita")
    os.makedirs(berita_dir, exist_ok=True)
    
    cname_filepath = os.path.join(docs_dir, "CNAME")
    with open(cname_filepath, "w", encoding="utf-8") as f:
        f.write("melek.kebijakan.id")
        
    today = datetime.datetime.now().strftime("%d %B %Y")
    today_iso = datetime.datetime.now().strftime("%Y-%m-%d")
    
    slug = seo_data.get('slug', 'berita-kebijakan')
    detail_filename = f"{slug}.html"
    detail_filepath = os.path.join(berita_dir, detail_filename)
    relative_link = f"berita/{detail_filename}"
    
    article_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{seo_data['seo_title']} - Melek Kebijakan News</title>
    <meta name="description" content="{seo_data['meta_description']}">
    <meta name="keywords" content="{seo_data['keywords']}">
    <meta property="og:title" content="{seo_data['seo_title']}">
    <meta property="og:description" content="{seo_data['meta_description']}">
    <meta property="og:image" content="{visual_url}">
    
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "NewsArticle",
      "headline": "{seo_data['seo_title']}",
      "image": ["{visual_url}"],
      "datePublished": "{today_iso}",
      "author": {{ "@type": "Organization", "name": "Melek Kebijakan ID" }}
    }}
    </script>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; background: #f4f6f9; color: #222; }}
        header {{ background: #d32f2f; color: white; padding: 15px 20px; font-size: 24px; font-weight: bold; display: flex; justify-content: space-between; align-items: center; }}
        header a {{ color: white; text-decoration: none; font-size: 16px; background: rgba(255,255,255,0.2); padding: 6px 12px; border-radius: 4px; }}
        .container {{ max-width: 800px; margin: 30px auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }}
        h1 {{ color: #111; line-height: 1.3; font-size: 28px; margin-top: 0; }}
        .meta {{ font-size: 14px; color: #777; border-bottom: 1px solid #eee; padding-bottom: 15px; margin-bottom: 20px; }}
        img {{ width: 100%; height: auto; border-radius: 8px; margin-bottom: 25px; }}
        .content {{ font-size: 18px; line-height: 1.8; white-space: pre-line; color: #333; }}
        footer {{ text-align: center; padding: 20px; font-size: 14px; color: #666; margin-top: 40px; border-top: 1px solid #ddd; }}
    </style>
</head>
<body>
    <header>
        <span>🏛️ MelekKebijakan.id</span>
        <a href="../index.html">← Beranda Berita</a>
    </header>
    <div class="container">
        <h1>{seo_data['seo_title']}</h1>
        <div class="meta">Dipublikasikan oleh <strong>Tim Melek Kebijakan</strong> | {today}</div>
        <img src="{visual_url}" alt="{seo_data['seo_title']}">
        <div class="content">
{content_data['script_narasi']}
        </div>
    </div>
    <footer>
        © 2026 melek.kebijakan.id - Portal Berita & Analisis Kebijakan Publik Independen
    </footer>
</body>
</html>
"""
    with open(detail_filepath, "w", encoding="utf-8") as f:
        f.write(article_html)

    json_db_path = os.path.join(docs_dir, "articles.json")
    articles = []
    if os.path.exists(json_db_path):
        try:
            with open(json_db_path, "r", encoding="utf-8") as f:
                articles = json.load(f)
        except Exception:
            articles = []
            
    new_article_entry = {
        "title": seo_data['seo_title'],
        "description": seo_data['meta_description'],
        "link": relative_link,
        "image": visual_url,
        "date": today
    }
    
    articles.insert(0, new_article_entry)
    with open(json_db_path, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

    cards_html = ""
    for item in articles:
        cards_html += f"""
        <div class="news-card">
            <img src="{item['image']}" alt="{item['title']}">
            <div class="news-body">
                <div class="news-date">{item['date']}</div>
                <h2 class="news-title"><a href="{item['link']}">{item['title']}</a></h2>
                <p class="news-desc">{item['description']}</p>
                <a href="{item['link']}" class="read-btn">Baca Selengkapnya →</a>
            </div>
        </div>
        """
        
    homepage_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Melek Kebijakan - Portal Berita & Analisis Kebijakan Publik</title>
    <meta name="description" content="Portal berita independen menyajikan analisis kritis berbasis fakta mengenai kebijakan pemerintah Indonesia.">
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; background: #f4f6f9; color: #222; }}
        header {{ background: #d32f2f; color: white; padding: 20px; text-align: center; }}
        header h1 {{ margin: 0; font-size: 32px; font-weight: bold; }}
        header p {{ margin: 5px 0 0 0; opacity: 0.9; font-size: 16px; }}
        .main-container {{ max-width: 1100px; margin: 30px auto; padding: 0 20px; }}
        .portal-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 25px; }}
        .news-card {{ background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.06); transition: transform 0.2s; display: flex; flex-direction: column; }}
        .news-card:hover {{ transform: translateY(-5px); }}
        .news-card img {{ width: 100%; height: 200px; object-fit: cover; }}
        .news-body {{ padding: 20px; flex-grow: 1; display: flex; flex-direction: column; }}
        .news-date {{ font-size: 12px; color: #d32f2f; font-weight: bold; margin-bottom: 8px; text-transform: uppercase; }}
        .news-title {{ font-size: 20px; margin: 0 0 10px 0; line-height: 1.4; }}
        .news-title a {{ color: #111; text-decoration: none; }}
        .news-title a:hover {{ color: #d32f2f; }}
        .news-desc {{ font-size: 14px; color: #666; line-height: 1.6; margin-bottom: 15px; flex-grow: 1; }}
        .read-btn {{ color: #d32f2f; text-decoration: none; font-weight: bold; font-size: 14px; }}
        footer {{ text-align: center; padding: 25px; background: #222; color: #fff; margin-top: 50px; font-size: 14px; }}
    </style>
</head>
<body>
    <header>
        <h1>🏛️ MELEK KEBIJAKAN NEWS</h1>
        <p>Media Analisis Kritis & Independen Kebijakan Publik Indonesia</p>
    </header>
    <div class="main-container">
        <h2 style="border-bottom: 3px solid #d32f2f; display: inline-block; padding-bottom: 5px; margin-bottom: 25px;">Berita & Analisis Terbaru</h2>
        <div class="portal-grid">
{cards_html}
        </div>
    </div>
    <footer>
        © 2026 melek.kebijakan.id - Diperbarui Otomatis oleh Kantor AI Agent
    </footer>
</body>
</html>
"""
    index_filepath = os.path.join(docs_dir, "index.html")
    with open(index_filepath, "w", encoding="utf-8") as f:
        f.write(homepage_html)
        
    print(f"✅ Artikel Berita Berhasil Diterbitkan ke Website melek.kebijakan.id!")
    return detail_filepath


# ==========================================
# 6. MANAGER AGENT (Kirim WhatsApp & Deteksi Error)
# ==========================================
def manager_agent_send_draft_to_wa(chat_id, visual_url, content_data, seo_data):
    print(f"📱 [MANAGER] Mengirimkan DRAFT LENGKAP ke WhatsApp Owner untuk Peninjauan...")
    url = f"https://api.green-api.com/waInstance{WA_INSTANCE_ID}/sendFileByUrl/{WA_API_TOKEN}"
    
    script_text = content_data.get("script_narasi", "")
    caption_ig = content_data.get("caption_ig_fb", "")
    seo_title = seo_data.get("seo_title", "")
    
    caption_wa = (
        f"🏛️ *KANTOR AI MELEK.KEBIJAKAN.ID - DRAFT KONTEN & BERITA*\n"
        f"--------------------------------------------------\n"
        f"📰 *JUDUL BERITA WEB:* {seo_title}\n\n"
        f"📜 *SKRIP NARASI REELS:*\n{script_text}\n\n"
        f"📝 *CAPTION SOSMED (IG & FB):*\n{caption_ig}\n"
        f"--------------------------------------------------\n"
        f"📌 *PERINTAH OWNER (BALAS CHAT INI):*\n"
        f"1. Balas *ACC* -> Otomatis diposting ke IG & FB dulu, lalu diterbitkan ke Website Portal Berita.\n"
        f"2. Balas *REVISI: [catatan]* -> Tim AI akan merubah isi skrip & editan visual secara otomatis."
    )
    
    if len(caption_wa) > 980:
        caption_wa = caption_wa[:975] + "\n\n...[teks dipotong untuk WA]"

    payload = {
        "chatId": chat_id,
        "urlFile": visual_url,
        "fileName": "draft_visual_3d.jpg",
        "caption": caption_wa
    }
    headers = {'Content-Type': 'application/json'}
    
    res = requests.post(url, json=payload, headers=headers).json()
    print(f"Status WA API Response: {res}")
    
    if "idMessage" not in res:
        raise RuntimeError(f"❌ GAGAL KIRIM WHATSAPP! Balasan API: {res}")
        
    print("✅ Notifikasi WhatsApp Berhasil Terkirim ke HP Owner!")
    return res


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    print("==================================================")
    print("🏢 KANTOR AI @melek.kebijakan.id ACTIVE & ONLINE")
    print("==================================================")
    
    topik = "Kebijakan Impor Beras Saat Musim Panen Raya"
    
    # 1. Riset Dampak Kerugian
    data_riset = researcher_agent(topik)
    
    # 2. Buat Skrip Kritis Berbasis Dampak Nyata
    content_output = copywriter_agent(topik, data_riset)
    
    # 3. SEO Specialist Optimization
    seo_output = seo_specialist_agent(topik, content_output.get("script_narasi", ""))
    
    # 4. Render Visual 3D Claymation
    prompt_3d = content_output.get("prompt_visual_3d", "Cute 3D claymation of Indonesian farmer")
    visual_ready_url = editor_animator_agent(prompt_3d)
    
    # 5. Menerbitkan ke Website Portal Berita
    publish_to_website_portal(content_output, visual_ready_url, seo_output)
    
    # 6. Kirim Laporan Draft & Visual ke WA Owner
    manager_agent_send_draft_to_wa(OWNER_WA_NUMBER, visual_ready_url, content_output, seo_output)
