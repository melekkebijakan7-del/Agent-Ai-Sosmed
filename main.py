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
# 1. RESEARCHER AGENT
# ==========================================
def researcher_agent(topic_query):
    print(f"🔍 [RESEARCHER] Riset fakta: '{topic_query}'...")
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": f"kebijakan pemerintah {topic_query} site:go.id OR site:bps.go.id OR site:dpr.go.id"})
    headers = {'X-API-KEY': SERPER_API_KEY, 'Content-Type': 'application/json'}
    try:
        response = requests.post(url, headers=headers, data=payload, timeout=10)
        results = response.json()
        snippets = [f"• {item.get('title')}: {item.get('snippet')}" for item in results.get("organic", [])[:4]]
        return "\n".join(snippets) if snippets else "Data publik & peraturan perundang-undangan relevan."
    except Exception as e:
        print(f"⚠️ [RESEARCHER] Error riset: {e}")
        return "Riset berdasarkan Laporan Resmi BPS, Putusan MK, dan Naskah Akademik."


# ==========================================
# 2. COPYWRITER AGENT (OTOMATIS DETEKSI MODEL)
# ==========================================
def copywriter_agent(topic, research_data):
    print("✍️ [COPYWRITER] Menyusun skrip argumen kritis...")
    
    prompt = f"""
    Buatkan skrip Reels kritis ringkas (maksimal 150 kata) untuk Instagram @melek.kebijakan.id.
    TOPIK: {topic}
    FAKTA DATA: {research_data}
    ATURAN:
    1. Harus berbasis fakta data, TANPA HOAKS.
    2. Struktur: Hook menarik, Konteks, Fakta Data, Argumen Kontra Kritis, Alternatif Solusi, CTA.
    3. Sertakan caption dan hashtag ringkas di akhir.
    """
    
    available_models = []
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                available_models.append(m.name)
    except Exception as e:
        print(f"⚠️ Gagal deteksi otomatis: {e}")
        
    if not available_models:
        available_models = ['models/gemini-1.5-flash', 'models/gemini-2.5-flash']

    for model_name in available_models:
        try:
            print(f"🔄 Memakai model: {model_name}...")
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            if response and response.text:
                print(f"✅ Berhasil generate menggunakan model: {model_name}")
                return response.text
        except Exception as e:
            print(f"⚠️ Model {model_name} gagal: {e}")
            continue
            
    raise RuntimeError("Semua model Gemini gagal merespons.")


# ==========================================
# 3. EDITOR & ANIMATOR AGENT
# ==========================================
def editor_animator_agent(video_url):
    print("🎬 [EDITOR] Upload animasi ke Cloudinary...")
    try:
        res = cloudinary.uploader.upload_large(video_url, resource_type="video", folder="melek_kebijakan_id")
        return res.get("secure_url")
    except Exception as e:
        print(f"❌ Error Editor: {e}")
        return None


# ==========================================
# 4. MANAGER AGENT (AUTO-TRIM WA CAPTION)
# ==========================================
def manager_agent_send_whatsapp(chat_id, video_url, script_text):
    print(f"📱 [MANAGER] Kirim Laporan ke WA Owner...")
    url = f"https://api.green-api.com/waInstance{WA_INSTANCE_ID}/sendFileByUrl/{WA_API_TOKEN}"
    
    caption = f"🏛️ *KANTOR AI: DRAFT REELS BARU*\n\n{script_text}\n\n📌 Balas ACC untuk post, atau tuliskan catatan revisi."
    
    # Batasi panjang caption maksimal 980 karakter agar tidak ditolak WhatsApp (limit 1024)
    if len(caption) > 980:
        caption = caption[:975] + "\n\n...[teks dipotong untuk WA]"

    payload = {"chatId": chat_id, "urlFile": video_url, "fileName": "draft.mp4", "caption": caption}
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url, json=payload, headers=headers).json()
    print(f"Status WA: {res}")
    return res


# ==========================================
# KANTOR AI RUNNER
# ==========================================
if __name__ == "__main__":
    print("==================================================")
    print("🏢 KANTOR AI @melek.kebijakan.id ACTIVE & ONLINE")
    print("==================================================")
    
    topik_kebijakan = "Evaluasi Kebijakan Impor Pangan"
    hasil_riset = researcher_agent(topik_kebijakan)
    skrip_final = copywriter_agent(topik_kebijakan, hasil_riset)
    
    sample_video = "https://res.cloudinary.com/demo/video/upload/dog.mp4"
    video_ready = editor_animator_agent(sample_video)
    
    if video_ready:
        manager_agent_send_whatsapp(OWNER_WA_NUMBER, video_ready, skrip_final)
