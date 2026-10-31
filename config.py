"""
الإعدادات. القيم الافتراضية هي نفس قيمك القديمة، وتقدر تغيّرها بدون لمس الكود
عبر متغيرات البيئة أو ملف .env بجانب app.py:
    RECO_BOT_TOKEN=...   RECO_API_ID=...   RECO_API_HASH=...
"""
import os


def _load_env(path=".env"):
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


_load_env()

BOT_TOKEN = os.getenv("RECO_BOT_TOKEN", "8761949055:AAHmm761ypE_dEhz3DltgVUHNQWkAyvVgag")
API_ID = int(os.getenv("RECO_API_ID", "28494906"))
API_HASH = os.getenv("RECO_API_HASH", "004295a4ebda27f44ecb312215f10284")
