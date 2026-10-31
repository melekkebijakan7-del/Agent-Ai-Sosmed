import os
import requests
import google.generativeai as genai
import cloudinary
import cloudinary.uploader

# Config Environment Variables
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
SERPER_API_KEY = os.environ.get("SERPER_API_KEY")
WA_INSTANCE_ID = os.environ.get("WA_INSTANCE_ID")
WA_API_TOKEN = os.environ.get("WA_API_TOKEN")

cloudinary.config( 
  cloud_name = os.environ.get("CLOUDINARY_CLOUD_NAME"), 
  api_key = os.environ.get("CLOUDINARY_API_KEY"), 
  api_secret = os.environ.get("CLOUDINARY_API_SECRET") 
)

genai.configure(api_key=GEMINI_API_KEY)

def generate_critical_script(policy_topic, revision_notes=None):
    """
    Menghasilkan skrip argumen kontra terhadap kebijakan pemerintah.
    Argumen didasarkan pada data/hukum mendasar, tanpa basa-basi.
    """
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    Bertindaklah sebagai analis kebijakan publik yang kritis, berbasis data, dan obyektif.
    Topik Kebijakan: {policy_topic}
    
    Tugas:
    1. Buatkan argumentasi penolakan/kontra terhadap kebijakan tersebut secara lugas, tegas, dan TANPA BASA-BASI.
    2. Wajib menyertakan dasar hukum, data statistik, atau dampak ekonomi/sosial yang nyata (dilarang menggunakan informasi palsu/hoaks).
    3. Tuliskan dalam bentuk Skrip Narasi Video Animasi durasi singkat (30-60 detik) untuk akun Instagram 'melek kebijakan Indonesia'.
    """
    
    if revision_notes:
        prompt += f"\n\ncatatan revisi dari pengguna: {revision_notes}. Sesuaikan skrip berdasarkan revisi ini."

    response = model.generate_content(prompt)
    return response.text

def upload_video_to_cloudinary(video_path_or_url):
    """Mengunggah file video animasi ke Cloudinary."""
    try:
        response = cloudinary.uploader.upload_large(
            video_path_or_url,
            resource_type = "video",
            folder = "melek_kebijakan_indonesia"
        )
        return response.get("secure_url")
    except Exception as e:
        print(f"Error upload ke Cloudinary: {e}")
        return None

def send_draft_to_whatsapp(chat_id, video_url, script_text):
    """Mengirimkan draft video dan skrip ke WhatsApp pengguna untuk di-review."""
    url = f"https://api.green-api.com/waInstance{WA_INSTANCE_ID}/sendFileByUrl/{WA_API_TOKEN}"
    caption = (
        "🎬 *DRAFT VIDEO ANIMASI BARU*\n"
        "------------------------------------\n"
        f"{script_text}\n\n"
        "------------------------------------\n"
        "Balas pesan ini dengan:\n"
        "1. *ACC* -> Untuk langsung mengunggah ke Instagram 'melek kebijakan Indonesia'.\n"
        "2. Tuliskan *instruksi revisi* jika ada bagian yang perlu diperbaiki."
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
    """Fungsi mengunggah otomatis ke akun Instagram melek kebijakan Indonesia."""
    # Memerlukan Access Token & Account ID dari Meta Developer
    print(f"Mengunggah video {video_url} ke Instagram 'melek kebijakan Indonesia'...")
    # Integrasi API Instagram Graph dijalankan setelah konfirmasi ACC
    return True

if __name__ == "__main__":
    print("Agent AI 'Melek Kebijakan Indonesia' Aktif...")
    
    # 1. Contoh Penentuan Topik Kebijakan Terbaru
    topik = "Kebijakan Impor Beras saat Musim Panen Raya"
    
    # 2. Pembuatan Skrip Kritis Basah-Data
    skrip_narasi = generate_critical_script(topik)
    print("Skrip Kritis Berhasil Disusun.")
    
    # 3. Contoh URL Video Hasil Generator Animasi
    sample_video_url = "https://res.cloudinary.com/demo/video/upload/dog.mp4"
    uploaded_url = upload_video_to_cloudinary(sample_video_url)
    
    if uploaded_url:
        print("Video berhasil diproses dan dikirim ke WhatsApp untuk peninjauan.")
        # Masukkan nomor WhatsApp Anda (Format: 628xxxxxxxxxx@c.us)
        # my_whatsapp = "628xxxxxxxxxx@c.us"
        # send_draft_to_whatsapp(my_whatsapp, uploaded_url, skrip_narasi)
