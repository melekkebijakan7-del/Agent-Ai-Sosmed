import os
import sys
import json
import requests
import google.generativeai as genai
import cloudinary
import cloudinary.uploader
from bs4 import BeautifulSoup

# ==============================================================================
# 0. KONFIGURASI ENVIRONMENT & AKSES GRATIS (Cloud Infrastructure)
# ==============================================================================
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
SERPER_API_KEY = os.environ.get("SERPER_API_KEY")
WA_INSTANCE_ID = os.environ.get("WA_INSTANCE_ID")
WA_API_TOKEN = os.environ.get("WA_API_TOKEN")

# Meta Instagram Graph API Keys
IG_ACCOUNT_ID = os.environ.get("INSTAGRAM_ACCOUNT_ID")
IG_ACCESS_TOKEN = os.environ.get("INSTAGRAM_ACCESS_TOKEN")

# Nomor WhatsApp Owner (@melek.kebijakan.id)
OWNER_WA_NUMBER = "6282361171427@c.us"

# Cloudinary Setup (25 GB Free Storage)
cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET")
)

# Gemini AI Setup
genai.configure(api_key=GEMINI_API_KEY)
AI_MODEL_NAME = 'gemini-2.5-flash'


# ==============================================================================
# 1. RESEARCHER AGENT (Mengambil Data Resmi & Bebas Hoaks)
# ==============================================================================
def researcher_agent(topic_query):
    """
    Mencari fakta & data dasar dari kementerian, BPS, atau DPR.
    """
    print(f"🔍 [RESEARCHER AGENT] Mengumpulkan data fakta kebijakan: '{topic_query}'...")
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": f"kebijakan pemerintah {topic_query} site:go.id OR site:bps.go.id OR site:dpr.go.id"})
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
                snippets.append(f"• {item.get('title')}: {item.get('snippet')} (Sumber: {item.get('link')})")
        return "\n".join(snippets) if snippets else "Data publik & peraturan perundang-undangan relevan."
    except Exception as e:
        print(f"⚠️ [RESEARCHER AGENT] Pengambilan web terbatas: {e}")
        return "Riset berdasarkan Laporan Resmi BPS, Putusan MK, dan Naskah Akademik."


# ==============================================================================
# 2. COPYWRITER AGENT (Formula Argumen Kontra Kritis 6-Tahap)
# ==============================================================================
def copywriter_agent(topic, research_data, revision_notes=None):
    """
    Menyusun skrip Reels (30-60 detik) berbasis formula kritis 6-tahap dari laporan.
    """
    print("✍️ [COPYWRITER AGENT] Menyusun skrip argumen kontra tanpa basa-basi...")
    model = genai.GenerativeModel(AI_MODEL_NAME)
    
    prompt = f"""
    Kamu adalah Copywriter Senior untuk akun Instagram @melek.kebijakan.id.
    Tugasmu adalah menyusun skrip edukasi publik kritis (30-60 detik) mengenai kebijakan berikut:

    TOPIK KEBIJAKAN: {topic}
    DATA / HASIL RISET FAKTA:
    {research_data}

    ATURAN KETAT SKRIP (DOKUMEN KANTOR AI V2):
    1. DILARANG HOAKS/FITNAH: Setiap klaim wajib berbasis fakta data, UU, atau dampak ekonomi nyata.
    2. DILARANG MENYERANG PRIBADI/FISIK PEJABAT: Fokus murni pada isi & dampak kebijakan publik.
    3. STRUKTUR WAKTU & NARASI (30-60 DETIK):
       - HOOK (3 Detik): "Pemerintah baru saja menerbitkan [kebijakan]. Tapi ada satu data yang jarang dibahas."
       - KONTEKS: Penjelasan singkat kebijakan & siapa yang terdampak.
       - FAKTA & DATA: Data resmi/hukum dari hasil riset.
       - ARGUMEN KONTRA: Kenapa kebijakan ini bermasalah / berdampak negatif bagi masyarakat.
       - ALTERNATIF SOLUSI: Solusi konkret yang seharusnya diambil pemerintah.
       - CALL TO ACTION (CTA): "Ikuti @melek.kebijakan.id untuk membaca kebijakan, bukan hanya ikut marah."

    BERIKAN JUGA:
    - Caption Instagram (Lengkap dengan Hastag: #KebijakanPublik #MelekKebijakan #EkonomiIndonesia)
    """

    if revision_notes:
        prompt += f"\n\nCATATAN REVISI DARI OWNER: {revision_notes}. Sesuaikan skrip dengan revisi ini."

    response = model.generate_content(prompt)
    return response.text


# ==============================================================================
# 3. EDITOR & ANIMATOR AGENT (Hosting & Rendering Cloud)
# ==============================================================================
def editor_animator_agent(raw_video_url_or_path):
    """
    Mengunggah klip animasi ke Cloudinary untuk siap didistribusikan.
    """
    print("🎬 [EDITOR AGENT] Menyiapkan klip video animasi dan mengunggah ke Cloud Storage...")
    try:
        response = cloudinary.uploader.upload_large(
            raw_video_url_or_path,
            resource_type="video",
            folder="melek_kebijakan_id"
        )
        return response.get("secure_url")
    except Exception as e:
        print(f"❌ [EDITOR AGENT] Upload video gagal: {e}")
        return None


# ==============================================================================
# 4. MANAGER AGENT (Kirim Laporan & Notifikasi ke WhatsApp Owner)
# ==============================================================================
def manager_agent_send_whatsapp(chat_id, video_url, script_text):
    """
    Mengirimkan laporan antrean draft lengkap ke WhatsApp Owner untuk peninjauan.
    """
    print(f"📱 [MANAGER AGENT] Mengirimkan draft lengkap ke WhatsApp Owner ({chat_id})...")
    url = f"https://api.green-api.com/waInstance{WA_INSTANCE_ID}/sendFileByUrl/{WA_API_TOKEN}"
    
    caption = (
        "🏛️ *KANTOR AI MELEK.KEBIJAKAN.ID - DRAFT REELS BARU*\n"
        "--------------------------------------------------\n"
        f"{script_text}\n\n"
        "--------------------------------------------------\n"
        "📌 *PERINTAH OWNER (BALAS CHAT INI):*\n"
        "1. Ketik *ACC* -> Langsung diposting otomatis ke Instagram @melek.kebijakan.id\n"
        "2. Ketik *REVISI: [catatan]* -> Tim AI akan merevisi skrip & video secara otomatis."
    )
    
    payload = {
        "chatId": chat_id,
        "urlFile": video_url,
        "fileName": "draft_melek_kebijakan.mp4",
        "caption": caption
    }
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url, json=payload, headers=headers).json()
    print(f"Status Pengiriman WhatsApp: {res}")
    return res


# ==============================================================================
# 5. PUBLISHER AGENT (Posting Otomatis ke Instagram Graph API)
# ==============================================================================
def publisher_agent_post_instagram(video_url, caption):
    """
    Mempublikasikan Reels otomatis ke Instagram Business @melek.kebijakan.id
    """
    print("🚀 [PUBLISHER AGENT] Mengunggah Reels ke Instagram @melek.kebijakan.id...")
    if not IG_ACCOUNT_ID or not IG_ACCESS_TOKEN:
        print("⚠️ [PUBLISHER AGENT] IG_ACCOUNT_ID / IG_ACCESS_TOKEN belum diset di Secrets.")
        return False

    # Step 1: Media Container
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
        # Step 2: Publish
        publish_url = f"https://graph.facebook.com/v19.0/{IG_ACCOUNT_ID}/media_publish"
        publish_payload = {
            'creation_id': creation_id,
            'access_token': IG_ACCESS_TOKEN
        }
        res_publish = requests.post(publish_url, data=publish_payload).json()
        print(f"✅ [PUBLISHER AGENT] Reels Berhasil Diposting! ID: {res_publish.get('id')}")
        return True
    return False


# ==============================================================================
# MAIN WORKFLOW (RUNNER AUTOMATION)
# ==============================================================================
if __name__ == "__main__":
    print("==================================================")
    print("🏢 KANTOR AI @melek.kebijakan.id ACTIVE & ONLINE")
    print("==================================================")
    
    # 1. Penetapan Topik Kritis
    topik_kebijakan = "Evaluasi Kebijakan Impor Pangan dan Perlindungan Petani Lokal"
    
    # 2. Riset Fakta
    hasil_riset = researcher_agent(topik_kebijakan)
    
    # 3. Penulisan Skrip Kritis
    skrip_final = copywriter_agent(topik_kebijakan, hasil_riset)
    
    # 4. Media Processing
    sample_animation_url = "https://res.cloudinary.com/demo/video/upload/dog.mp4"
    video_ready_url = editor_animator_agent(sample_animation_url)
    
    # 5. Laporan Manager ke WhatsApp Owner
    if video_ready_url:
        manager_agent_send_whatsapp(OWNER_WA_NUMBER, video_ready_url, skrip_final)
