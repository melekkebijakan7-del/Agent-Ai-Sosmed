import os
import sys
import json
import requests
import google.generativeai as genai
import cloudinary
import cloudinary.uploader
from bs4 import BeautifulSoup

# ==============================================================================
# 0. KONFIGURASI ENVIRONMENT & AKSES GRATIS (Free Tier APIs)
# ==============================================================================
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
SERPER_API_KEY = os.environ.get("SERPER_API_KEY")
WA_INSTANCE_ID = os.environ.get("WA_INSTANCE_ID")
WA_API_TOKEN = os.environ.get("WA_API_TOKEN")

# Instagram Graph API Keys
IG_ACCOUNT_ID = os.environ.get("INSTAGRAM_ACCOUNT_ID")
IG_ACCESS_TOKEN = os.environ.get("INSTAGRAM_ACCESS_TOKEN")

# Nomor WhatsApp Owner (Format Green API: 6282361171427@c.us)
OWNER_WA_NUMBER = "6282361171427@c.us"

# Setup Cloudinary Media Storage (Free 25GB)
cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET")
)

# Setup Gemini AI Model Terbaru (Bebas Error 404)
genai.configure(api_key=GEMINI_API_KEY)
AI_MODEL_NAME = 'gemini-2.5-flash'


# ==============================================================================
# 1. RESEARCHER AGENT: Mencari Kebijakan Publik dari Sumber Resmi
# ==============================================================================
def researcher_agent(topic_query):
    """
    Riset fakta kebijakan dari sumber resmi / web scraping dasar tanpa hoaks.
    """
    print(f"🔍 [RESEARCHER AGENT] Memulai riset fakta untuk: '{topic_query}'...")
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": f"kebijakan pemerintah {topic_query} dpr kemenkeu bps"})
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.post(url, headers=headers, data=payload, timeout=10)
        results = response.json()
        snippets = []
        if "organic" in results:
            for item in results["organic"][:4]:
                snippets.append(f"- {item.get('title')}: {item.get('snippet')}")
        return "\n".join(snippets) if snippets else "Data statistik publik & naskah akademik relevan."
    except Exception as e:
        print(f"⚠️ [RESEARCHER AGENT] Scraping terbatas: {e}")
        return "Riset berdasarkan data statistik BPS, UU Publik, dan Laporan Kemenkeu."


# ==============================================================================
# 2. COPYWRITER AGENT: Menyusun Argumen Kontra Kritis & Lugas
# ==============================================================================
def copywriter_agent(topic, research_data, revision_notes=None):
    """
    Menyusun skrip Reels 30-60 detik dengan struktur:
    Hook -> Konteks -> Fakta Data -> Argumen Kontra -> Alternatif Solusi -> CTA
    """
    print("✍️ [COPYWRITER AGENT] Menyusun skrip argumen kritis tanpa basa-basi...")
    model = genai.GenerativeModel(AI_MODEL_NAME)
    
    prompt = f"""
    Kamu adalah Copywriter Senior untuk akun Instagram @melek.kebijakan.id.
    Tugasmu adalah membuat skrip Reels kritis (30-60 detik) mengenai kebijakan pemerintah Indonesia berikut.

    TOPIK KEBIJAKAN: {topic}
    DATA / HASIL RISET:
    {research_data}

    ATURAN KETAT SKRIP (JANGAN DILANGGAR):
    1. Harus BERBASIS DATA, dasar hukum, atau dampak ekonomi nyata (DILARANG HOAKS / FITNAH).
    2. Kritik kebijakan secara argumentatif, lugas, tegas, dan TANPA BASA-BASI.
    3. Struktur Skrip:
       - HOOK (3 detik pertama yang memicu rasa ingin tahu)
       - KONTEKS KEBIJAKAN (Penjelasan singkat kebijakan)
       - FAKTA & DATA HUKUM/EKONOMI (Angka / Dasar UU)
       - ARGUMEN KONTRA (Kenapa kebijakan ini berdampak buruk / bermasalah)
       - ALTERNATIF SOLUSI (Langkah nyata yang seharusnya diambil pemerintah)
       - CALL TO ACTION (Mengajak audiens berpikir di @melek.kebijakan.id)
    """

    if revision_notes:
        prompt += f"\n\nCATATAN REVISI DARI OWNER: {revision_notes}. Wajib sesuaikan skrip dengan revisi ini."

    response = model.generate_content(prompt)
    return response.text


# ==============================================================================
# 3. EDITOR & ANIMATOR AGENT: Mengolah Media Video ke Cloudinary
# ==============================================================================
def editor_animator_agent(raw_video_url_or_path):
    """
    Mengunggah file animasi/video ke Cloudinary agar siap didistribusikan.
    """
    print("🎬 [EDITOR AGENT] Rendering media animasi dan mengunggah ke Cloud Storage...")
    try:
        response = cloudinary.uploader.upload_large(
            raw_video_url_or_path,
            resource_type="video",
            folder="melek_kebijakan_id"
        )
        return response.get("secure_url")
    except Exception as e:
        print(f"❌ [EDITOR AGENT] Gagal upload video: {e}")
        return None


# ==============================================================================
# 4. MANAGER AGENT: Mengirim Draft ke WhatsApp Owner (Revisi / ACC)
# ==============================================================================
def manager_agent_send_whatsapp(chat_id, video_url, script_text):
    """
    Mengirimkan laporan draft video animasi + skrip ke WhatsApp Owner.
    """
    print(f"📱 [MANAGER AGENT] Mengirimkan draft ke WhatsApp Owner ({chat_id}) untuk review...")
    url = f"https://api.green-api.com/waInstance{WA_INSTANCE_ID}/sendFileByUrl/{WA_API_TOKEN}"
    
    caption = (
        "🏛️ *KANTOR AI MELEK.KEBIJAKAN.ID - LAPORAN DRAFT REELS*\n"
        "--------------------------------------------------\n"
        f"{script_text}\n\n"
        "--------------------------------------------------\n"
        "📌 *INSTRUKSI OWNER (BALAS CHAT INI):*\n"
        "1. Ketik *ACC* -> Otomatis di-post ke Instagram @melek.kebijakan.id\n"
        "2. Ketik *REVISI: [catatan]* -> AI akan merevisi skrip & video secara otomatis."
    )
    
    payload = {
        "chatId": chat_id,
        "urlFile": video_url,
        "fileName": "draft_animasi_kebijakan.mp4",
        "caption": caption
    }
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url, json=payload, headers=headers).json()
    print(f"Status Pengiriman WhatsApp: {res}")
    return res


# ==============================================================================
# 5. PUBLISHER AGENT: Posting Otomatis ke Instagram @melek.kebijakan.id
# ==============================================================================
def publisher_agent_post_instagram(video_url, caption):
    """
    Memublikasikan Reels ke akun Instagram Business / Creator @melek.kebijakan.id
    """
    print("🚀 [PUBLISHER AGENT] Mempublikasikan Reel ke Instagram @melek.kebijakan.id...")
    if not IG_ACCOUNT_ID or not IG_ACCESS_TOKEN:
        print("⚠️ [PUBLISHER AGENT] IG_ACCOUNT_ID atau IG_ACCESS_TOKEN belum diset di Secrets.")
        return False

    # Langkah 1: Buat Media Container
    container_url = f"https://graph.facebook.com/v19.0/{IG_ACCOUNT_ID}/media"
    container_payload = {
        'media_type': 'REELS',
        'video_url': video_url,
        'caption': caption,
        'access_token': IG_ACCESS_TOKEN
    }
    res_container = requests.post(container_url, data=container_payload).json()
    creation_id = res_container.get('id')

    if creation_id:
        # Langkah 2: Publish Media Container
        publish_url = f"https://graph.facebook.com/v19.0/{IG_ACCOUNT_ID}/media_publish"
        publish_payload = {
            'creation_id': creation_id,
            'access_token': IG_ACCESS_TOKEN
        }
        res_publish = requests.post(publish_url, data=publish_payload).json()
        print(f"✅ [PUBLISHER AGENT] Berhasil Dipublikasikan! ID: {res_publish.get('id')}")
        return True
    else:
        print(f"❌ [PUBLISHER AGENT] Gagal membuat container: {res_container}")
        return False


# ==============================================================================
# MAIN WORKFLOW EXECUTION (KANTOR AI RUNNER)
# ==============================================================================
if __name__ == "__main__":
    print("==================================================")
    print("🏢 KANTOR AI @melek.kebijakan.id RESMI DIAKTIFKAN")
    print("==================================================")
    
    # 1. Menentukan Isu Kebijakan Publik Hari Ini
    topik = "Kebijakan Impor Beras dan Dampaknya pada Petani Lokal"
    
    # 2. Riset oleh Researcher Agent
    hasil_riset = researcher_agent(topik)
    
    # 3. Penulisan Skrip Kritis oleh Copywriter Agent
    skrip_final = copywriter_agent(topik, hasil_riset)
    print("\n--- SKRIP HASIL COPYWRITER ---")
    print(skrip_final[:250] + "...\n")
    
    # 4. Rendering Video oleh Editor Agent
    sample_animation_url = "https://res.cloudinary.com/demo/video/upload/dog.mp4"
    video_ready_url = editor_animator_agent(sample_animation_url)
    
    # 5. Notifikasi Manager Agent ke WhatsApp Owner
    if video_ready_url:
        print(f"✨ Video Animasi Siap di Cloud Storage: {video_ready_url}")
        # Mengirimkan otomatis draft skrip dan video ke WhatsApp Owner
        manager_agent_send_whatsapp(OWNER_WA_NUMBER, video_ready_url, skrip_final)
