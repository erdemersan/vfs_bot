import os
import requests

URL = os.getenv("TARGET_URL", "https://example.com")
CHECK_TEXT = os.getenv("CHECK_TEXT", "Example Domain")

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(URL, headers=headers, timeout=30)

status = r.status_code
found = CHECK_TEXT in r.text
snippet = r.text[:50000].replace("\n", " ").replace("\r", " ")

result_lines = [
    f"URL: {URL}",
    f"HTTP: {status}",
    f"ARANAN_METIN: {CHECK_TEXT}",
    f"BULUNDU_MU: {'EVET' if found else 'HAYIR'}",
    f"ILK_50000_KARAKTER: {snippet}",
]

result_text = "\n".join(result_lines)
print(result_text)

summary_path = os.getenv("GITHUB_STEP_SUMMARY")
if summary_path:
    with open(summary_path, "a", encoding="utf-8") as f:
        f.write("## Sonuç\n\n")
        f.write("```\n")
        f.write(result_text)
        f.write("\n```\n")
