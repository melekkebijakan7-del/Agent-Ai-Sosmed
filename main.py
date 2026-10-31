import os
import requests
import google.generativeai as genai
import cloudinary
import cloudinary.uploader

# Configuration & Environment Variables
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
SERPER_API_KEY = os.environ.get("SERPER_API_KEY")
WA_INSTANCE_ID = os.environ.get("WA_INSTANCE_ID")
WA_API_TOKEN = os.environ.get("WA_API_TOKEN")

# Configuration Instagram Graph API
IG_ACCOUNT_ID = os.environ.get("INSTAGRAM_ACCOUNT_ID")
IG_ACCESS_TOKEN = os.environ.get("INSTAGRAM_ACCESS_TOKEN")

# Setup Cloudinary
cloudinary.config( 
  cloud_name = os.environ.get("CLOUDINARY_CLOUD_NAME"), 
  api_key = os.environ.get("CLOUDINARY_API_KEY"), 
  api_secret = os.environ.get("CLOUDINARY_API_SECRET") 
)

genai.configure(api_key=GEMINI_API_KEY)

def generate_critical_script(policy_topic, revision_notes=None):
    """
    Menghasilkan skrip kritis terhadap kebijakan pemerintah Indonesia.
    Argumen berbasis data, hukum, obyektif, tanpa hoaks & tanpa basa-basi.
    """
    # Menggunakan model gemini-2.5-flash
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = f"""
    Bertindaklah sebagai analis kebijakan publik yang kritis, berbasis data, dan obyektif untuk akun Instagram 'melek.kebijakan.id'.
    Topik Kebijakan: {policy_topic}
    
    Tugas:
    1. Buatkan argumentasi penolakan/kontra terhadap kebijakan tersebut secara lugas, tegas, dan TANPA BASA-BASI.
    2. Wajib menyertakan dasar hukum, data statistik, atau dampak nyata (dilarang menggunakan informasi palsu/hoaks).
    3. Tuliskan dalam bentuk Skrip Narasi Video Animasi durasi singkat (30-60 detik) beserta usulan caption Instagram.
    """
    
    if revision_notes:
        prompt += f"\n\nCATATAN REVISI PENGGUNA: {revision_notes}. Sesuaikan skrip berdasarkan instruksi revisi ini."

    response = model.generate_content(prompt)
    return response.text

def upload_video_to_cloudinary(video_path_or_url):
    """Mengunggah file video animasi ke Cloudinary."""
    try:
        response = cloudinary.uploader.upload_large(
            video_path_or_url,
            resource_type = "video",
            folder = "melek_kebijakan_id"
        )
        return response.get("secure_url")
    except Exception as e:
        print(f"Error upload ke Cloudinary: {e}")
        return None

def send_draft_to_whatsapp(chat_id, video_url, script_text):
    """Mengirimkan draft video animasi & skrip ke WhatsApp pengguna untuk review/revisi."""
    url = f"https://api.green-api.com/waInstance{WA_INSTANCE_ID}/sendFileByUrl/{WA_API_TOKEN}"
    caption = (
        "🎬 *DRAFT VIDEO ANIMASI MELEK.KEBIJAKAN.ID*\n"
        "--------------------------------------------------\n"
        f"{script_text}\n\n"
        "--------------------------------------------------\n"
        "Balas pesan ini dengan:\n"
        "1. *ACC* -> Untuk mengunggah otomatis ke akun Instagram @melek.kebijakan.id\n"
        "2. *Tuliskan revisi* -> Jika ada bagian argumen atau skrip yang ingin diperbaiki."
    )
    payload = {
        "chatId": chat_id,
        "urlFile": video_url,
        "fileName": "melek_kebijakan_draft.mp4",
        "caption": caption
    }
    headers = {'Content-Type': 'application/json'}
    return requests.post(url, json=payload, headers=headers).json()

def post_to_instagram(video_url, caption):
    """Fungsi posting otomatis ke akun Instagram @melek.kebijakan.id via Instagram Graph API."""
    if not IG_ACCOUNT_ID or not IG_ACCESS_TOKEN:
        print("Pengunggahan ke Instagram dilewati: Access Token / Account ID belum diset.")
        return False
        
    # 1. Buat Container Media Reel
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
        # 2. Publish Container Media
        publish_url = f"https://graph.facebook.com/v19.0/{IG_ACCOUNT_ID}/media_publish"
        publish_payload = {
            'creation_id': creation_id,
            'access_token': IG_ACCESS_TOKEN
        }
        res_publish = requests.post(publish_url, data=publish_payload).json()
        print(f"Status Posting Instagram @melek.kebijakan.id: {res_publish}")
        return True
    return False

if __name__ == "__main__":
    print("Agent AI 'melek.kebijakan.id' Berjalan...")
    
    # 1. Riset & Pembuatan Skrip Kritis
    topik_kebijakan = "Evaluasi Kebijakan Impor Pangan Saat Musim Panen"
    skrip_narasi = generate_critical_script(topik_kebijakan)
    print("Skrip Argumen Kritis Berhasil Dibuat.")
    
    # 2. Pengolahan & Upload Video Animasi
    sample_video_url = "https://res.cloudinary.com/demo/video/upload/dog.mp4"
    uploaded_url = upload_video_to_cloudinary(sample_video_url)
    
    if uploaded_url:
        print(f"Video Animasi Berhasil Diunggah ke Cloudinary: {uploaded_url}")
