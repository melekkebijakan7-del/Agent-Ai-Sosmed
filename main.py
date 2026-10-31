import os
import requests
import google.generativeai as genai
import cloudinary
import cloudinary.uploader

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
SERPER_API_KEY = os.environ.get("SERPER_API_KEY")
WA_INSTANCE_ID = os.environ.get("WA_INSTANCE_ID")
WA_API_TOKEN = os.environ.get("WA_API_TOKEN")

IG_ACCOUNT_ID = os.environ.get("INSTAGRAM_ACCOUNT_ID")
IG_ACCESS_TOKEN = os.environ.get("INSTAGRAM_ACCESS_TOKEN")

cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET")
)

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY belum diset di environment variable.")

genai.configure(api_key=GEMINI_API_KEY)


def generate_critical_script(policy_topic, revision_notes=None):
    model = genai.GenerativeModel('gemini-2.5-flash')

    prompt = f"""
    Bertindaklah sebagai analis kebijakan publik yang kritis, berbasis data, dan obyektif
    untuk akun Instagram 'melek.kebijakan.id'.
    Topik Kebijakan: {policy_topic}

    Tugas:
    1. Buatkan argumentasi penolakan/kontra terhadap kebijakan tersebut secara lugas dan tegas.
    2. Wajib menyertakan dasar hukum, data statistik, atau dampak nyata.
    3. Dilarang menggunakan informasi palsu atau hoaks.
    4. Tuliskan skrip narasi video animasi durasi 30-60 detik beserta caption Instagram.
    """

    if revision_notes:
        prompt += f"\n\nCATATAN REVISI PENGGUNA: {revision_notes}"

    response = model.generate_content(prompt)

    if not response.candidates:
        raise ValueError("Gemini tidak mengembalikan kandidat respons.")

    finish_reason = response.candidates[0].finish_reason
    if finish_reason != 1:
        raise ValueError(f"Respons Gemini diblokir atau tidak selesai. finish_reason={finish_reason}")

    return response.text


def upload_video_to_cloudinary(video_path_or_url):
    try:
        if video_path_or_url.startswith(("http://", "https://")):
            response = cloudinary.uploader.upload(
                video_path_or_url,
                resource_type="video",
                folder="melek_kebijakan_id"
            )
        else:
            response = cloudinary.uploader.upload_large(
                video_path_or_url,
                resource_type="video",
                folder="melek_kebijakan_id"
            )

        secure_url = response.get("secure_url")
        if not secure_url:
            raise ValueError(f"Cloudinary tidak mengembalikan secure_url: {response}")

        return secure_url

    except Exception as e:
        print(f"Error upload ke Cloudinary: {e}")
        return None


def send_draft_to_whatsapp(chat_id, video_url, script_text):
    url = f"https://api.green-api.com/waInstance{WA_INSTANCE_ID}/sendFileByUrl/{WA_API_TOKEN}"

    caption = (
        "🎬 *DRAFT VIDEO ANIMASI MELEK.KEBIJAKAN.ID*\n"
        "--------------------------------------------------\n"
        f"{script_text}\n\n"
        "--------------------------------------------------\n"
        "Balas pesan ini dengan:\n"
        "1. *ACC* -> Untuk mengunggah otomatis ke Instagram @melek.kebijakan.id\n"
        "2. *Tuliskan revisi* -> Jika ada bagian yang ingin diperbaiki."
    )

    payload = {
        "chatId": chat_id,
        "urlFile": video_url,
        "fileName": "melek_kebijakan_draft.mp4",
        "caption": caption
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()


def post_to_instagram(video_url, caption):
    if not IG_ACCOUNT_ID or not IG_ACCESS_TOKEN:
        print("Instagram dilewati: INSTAGRAM_ACCOUNT_ID / INSTAGRAM_ACCESS_TOKEN belum diset.")
        return False

    container_url = f"https://graph.facebook.com/v19.0/{IG_ACCOUNT_ID}/media"
    container_payload = {
        "media_type": "REELS",
        "video_url": video_url,
        "caption": caption,
        "access_token": IG_ACCESS_TOKEN
    }

    res_container = requests.post(container_url, data=container_payload, timeout=60).json()
    creation_id = res_container.get("id")

    if not creation_id:
        print(f"Gagal membuat media container Instagram: {res_container}")
        return False

    publish_url = f"https://graph.facebook.com/v19.0/{IG_ACCOUNT_ID}/media_publish"
    publish_payload = {
        "creation_id": creation_id,
        "access_token": IG_ACCESS_TOKEN
    }

    res_publish = requests.post(publish_url, data=publish_payload, timeout=60).json()
    print(f"Status Posting Instagram: {res_publish}")

    return "id" in res_publish


if __name__ == "__main__":
    print("Agent AI 'melek.kebijakan.id' Berjalan...")

    topik_kebijakan = "Evaluasi Kebijakan Impor Pangan Saat Musim Panen"

    try:
        skrip_narasi = generate_critical_script(topik_kebijakan)
        print("Skrip Argumen Kritis Berhasil Dibuat.")
    except Exception as e:
        print(f"Gagal membuat skrip: {e}")
        raise SystemExit(1)

    sample_video_url = "https://res.cloudinary.com/demo/video/upload/dog.mp4"
    uploaded_url = upload_video_to_cloudinary(sample_video_url)

    if uploaded_url:
        print(f"Video Berhasil Diunggah ke Cloudinary: {uploaded_url}")
    else:
        print("Upload video ke Cloudinary gagal.")
