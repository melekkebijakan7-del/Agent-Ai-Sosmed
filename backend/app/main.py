import os, json, datetime, logging, httpx, pathlib
from jinja2 import Environment, FileSystemLoader

log = logging.getLogger("melek")
log.setLevel(logging.INFO)

# Mengambil Kunci Rahasia
ANTHROPIC_API = os.getenv("ANTHROPIC_API_KEY")
OPENAI_API = os.getenv("OPENAI_API_KEY")
TOPIC = os.getenv("ARTICLE_TOPIC", "Dampak UU ITE terhadap Kebebasan Pers")

def _anthropic(messages):
    resp = httpx.post(
        "https://api.anthropic.com/v1/messages",
        headers={"x-api-key": ANTHROPIC_API, "anthropic-version": "2023-06-01"},
        json={"model": "claude-3-5-sonnet-20240620", "max_tokens": 8000, "messages": messages},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["content"][0]["text"]

def _openai(messages):
    resp = httpx.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENAI_API}"},
        json={"model": "gpt-4o", "messages": messages},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]

print(f"Memulai tugas harian: Membuat 1 Artikel untuk topik '{TOPIC}'...")

# 1. BIKIN TEPAT 1 ARTIKEL (Menghemat Token Claude)
article_prompt = f"Tulis 1 artikel investigasi hukum mendalam ala Kompas tentang: '{TOPIC}'. Sertakan Latar Belakang, Analisis Hukum, dan Daftar Pustaka (Bibliografi) di akhir."
article_content = _anthropic([{"role":"user", "content": article_prompt}])
summary = article_content.split("\n\n")[0]
bibliography = article_content.split("Bibliografi")[-1].strip() if "Bibliografi" in article_content else ""

# 2. BIKIN TEPAT 1 CAPTION SOSMED (Menghemat Token OpenAI)
caption_prompt = f"Buat 1 caption sosmed dramatis (maks 150 huruf) untuk artikel ini: '{TOPIC}' yang mengarah ke link melek.kebijakan.id"
caption = _openai([{"role":"user", "content": caption_prompt}])

# 3. BIKIN TEPAT 1 PROMPT GAMBAR & 1 PROMPT VIDEO (Untuk dicopy ke Kling/Haiper)
prompt_gambar = f"Hyper-realistic editorial photography for a legal investigation about '{TOPIC}'. Dramatic lighting, dark navy and crimson colors, 8k resolution."
prompt_video = f"Cinematic animation scene for a legal investigation titled '{TOPIC}'. Smooth camera pan, courtroom elements, high-budget documentary style."

# --- PROSES MEMASUKKAN KE HTML ---
web_dir = pathlib.Path(__file__).parents[2] / "web"
web_dir.mkdir(parents=True, exist_ok=True)

env = Environment(loader=FileSystemLoader(web_dir / "templates"))
tmpl = env.get_template("article.html")
rendered_html = tmpl.render(
    title=TOPIC,
    date=datetime.datetime.now().strftime("%d %B %Y"),
    content=article_content,
    bibliography=bibliography,
    caption=caption,
    prompt_gambar=prompt_gambar,
    prompt_video=prompt_video
)

filename = f"{TOPIC.replace(' ', '_')}.html"
out_path = web_dir / filename
out_path.write_text(rendered_html, encoding="utf-8")

# --- UPDATE DAFTAR ISI WEBSITE ---
manifest_path = web_dir / "manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else []
manifest.append({
    "title": TOPIC, "file": filename, "summary": summary, "caption": caption
})
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Tugas harian selesai! 1 Artikel, 1 Prompt Gambar, dan 1 Prompt Video berhasil dibuat.")
