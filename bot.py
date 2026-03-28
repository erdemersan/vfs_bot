import requests

URL = "https://www.digikey.com/en/maker/projects/realtime-gps-tracker-with-raspberry-pi-pico-sim800l-gsm-module/d133a048a1ef4f40bb14e3be15be7467?utm_campaign=real-time_gps_tracker_wit&utm_content=digikey&utm_medium=social&utm_source=twitter"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    r = requests.get(URL, headers=headers, timeout=30)
    print("HTTP status:", r.status_code)
    print("İlk 1000 karakter:")
    print(r.text[:1000])

    if "No appointments available" in r.text:
        print("Sonuç: Randevu yok metni bulundu")
    else:
        print("Sonuç: Randevu yok metni bulunamadı")
except Exception as e:
    print("Hata oluştu:", str(e))
    raise
