import requests

city = input("Masukkan nama kota: ")

url = "https://api.aladhan.com/v1/timingsByCity"
params = {
    "city": city,
    "country": "Indonesia",
    "method": 20
}

response = requests.get(url, params=params).json()
timings = response["data"]["timings"]
hijri = response["data"]["date"]["hijri"]["date"]

print("Jadwal Sholat:")
print("Subuh   :", timings["Fajr"])
print("Dzuhur  :", timings["Dhuhr"])
print("Ashar   :", timings["Asr"])
print("Maghrib :", timings["Maghrib"])
print("Isya    :", timings["Isha"])
print("Tanggal Hijriah:", hijri)
