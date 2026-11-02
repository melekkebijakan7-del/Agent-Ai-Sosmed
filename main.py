import os
import json
import requests
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

# Nomor WA Owner
OWNER_WA_NUMBER = "6282361171427@c.us"

cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET")
)

genai.configure(api_key=GEMINI_API_KEY)


# ==========================================
# 1. RESEARCHER AGENT (Riset Dampak Lapangan)
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
        print(f"⚠️ [RESEARCHER] Error: {e}")
        return "Riset berdasarkan dampak riil penurunan pendapatan masyarakat & harga pasar."


# ==========================================
# 2. COPYWRITER AGENT (Kritis + Dampak Nyata)
# ==========================================
def copywriter_agent(topic, research_data):
    print("✍️ [COPYWRITER] Menyusun skrip argumen kontra berbasis dampak nyata...")
    
    prompt = f"""
    Kamu adalah Copywriter Utama akun Instagram @melek.kebijakan.id.
    Tugasmu menyusun skrip Reels (30-45 detik) yang KONTRA KEBIJAKAN PEMERINTAH, tetapi BERBASIS FAKTA & DAMPAK NYATA.

    TOPIK: {topic}
    HASIL RISET DAMPAK:
    {research_data}

    ATURAN KETAT SKRIP:
    1. DILARANG MENOLAK ASAL-ASALAN: Kritik harus rasional, argumentatif, dan berbasis data.
    2. WAJIB BERIKAN CONTOH DAMPAK NYATA: Sebutkan secara spesifik siapa yang dirugikan (contoh: harga gabah petani anjlok, beban pajak UMKM meningkat, daya beli buruh turun).
    3. STRUKTUR NARASI:
       - HOOK (Memancing rasa ingin tahu)
       - KONTEKS KEBIJAKAN (Penjelasan singkat aturan pemerintah)
       - CONTOH DAMPAK NYATA (Kerugian yang langsung dirasakan masyarakat)
       - ARGUMEN KONTRA KRITIS (Alasan kenapa kebijakan ini keliru)
       - ALTERNATIF SOLUSI (Langkah konkrit yang seharusnya diambil)
       - CTA: "Mari kritis bersama @melek.kebijakan.id"

    4. DESKRIPSI VISUAL ANIMASI 3D:
       Tuliskan 1 deskripsi prompt visual dalam Bahasa Inggris untuk membuat gambar adegan animasi 3D (Gaya Claymation/Toko Karakter 3D seperti anak sekolah di sawah).

    Format Output JSON:
    {{
      "script_narasi": "Teks narasi Reels yang akan dibacakan...",
      "caption_ig": "Teks caption Instagram + Hashtag...",
      "prompt_visual_3d": "Cute 3D claymation animation style of an Indonesian farmer standing in a dry rice field, highly detailed, vertical 9:16"
    }}
    """
    
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
            print(f"🔄 Memakai model: {model_name}...")
            model = genai.GenerativeModel(model_name)
            res = model.generate_content(prompt)
            if res and res.text:
                clean_text = res.text.replace("```json", "").replace("```", "").strip()
                return json.loads(clean_text)
        except Exception as e:
            print(f"⚠️ Model {model_name} gagal: {e}")
            continue
            
    raise RuntimeError("Gagal menghasilkan skrip.")


# ==========================================
# 3. EDITOR AGENT (Auto Render Visual 3D)
# ==========================================
def editor_animator_agent(prompt_visual):
    print("🎬 [EDITOR] Memproses gambar visual animasi 3D (Claymation Style)...")
    styled_prompt = f"{prompt_visual}, cute 3D claymation style, vibrant lighting, highly detailed, 9:16 vertical ratio"
    encoded_prompt = requests.utils.quote(styled_prompt)
    
    # URL Generator AI Visual 3D Cloud
    visual_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=720&height=1280&nologo=true"
    print(f"🖼️ Visual 3D Siap: {visual_url}")
    return visual_url


# ==========================================
# 4. MANAGER AGENT (Kirim Laporan WA)
# ==========================================
def manager_agent_send_whatsapp(chat_id, visual_url, content_data):
    print(f"📱 [MANAGER] Mengirimkan draft ke WhatsApp Owner...")
    url = f"https://api.green-api.com/waInstance{WA_INSTANCE_ID}/sendFileByUrl/{WA_API_TOKEN}"
    
    script_text = content_data.get("script_narasi", "")
    caption_ig = content_data.get("caption_ig", "")
    
    caption_wa = (
        f"🏛️ *KANTOR AI MELEK.KEBIJAKAN.ID - DRAFT KONTEN KRITIS*\n"
        f"--------------------------------------------------\n"
        f"📜 *SKRIP NARASI REELS:*\n{script_text}\n\n"
        f"📝 *CAPTION INSTAGRAM:*\n{caption_ig}\n"
        f"--------------------------------------------------\n"
        f"📌 Balas *ACC* untuk posting otomatis, atau tuliskan *REVISI: [catatan]*"
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
    print(f"Status WA: {res}")
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
    
    # 3. Buat Visual Animasi 3D Claymation
    prompt_3d = content_output.get("prompt_visual_3d", "Cute 3D claymation of Indonesian farmer")
    visual_ready_url = editor_animator_agent(prompt_3d)
    
    # 4. Laporan ke WhatsApp Owner
    manager_agent_send_whatsapp(OWNER_WA_NUMBER, visual_ready_url, content_output)
