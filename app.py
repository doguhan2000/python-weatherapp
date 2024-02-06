import requests
from datetime import datetime, timedelta

def get_weather(city):
    api_key = 'eb7113d44fceaa1eefb34ce8a28b6b2c'  
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        ana_hava_durumu = data["main"]
        ruzgar_hava_durumu = data["wind"]
        hava_durumu_durumu = data["weather"][0]
        sicaklik = ana_hava_durumu["temp"]
        hissedilen_sicaklik = ana_hava_durumu["feels_like"]
        nem_orani = ana_hava_durumu["humidity"]
        ruzgar_hizi = ruzgar_hava_durumu["speed"]
        hava_durumu_aciklama = hava_durumu_durumu["description"]

        print(f"Hava Durumu: {hava_durumu_aciklama.capitalize()}")
        print(f"Sıcaklık: {sicaklik}°C")
        print(f"Hissedilen Sıcaklık: {hissedilen_sicaklik}°C")
        print(f"Nem Oranı: {nem_orani}%")
        print(f"Rüzgar Hızı: {ruzgar_hizi} m/s")

        # 3 günlük hava durumu tahmini
        print("\n3 Günlük Hava Durumu Tahmini:")
        for i in range(1, 4):
            forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()
            forecast_day = (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d')
            for item in forecast_data["list"]:
                if item["dt_txt"].split()[0] == forecast_day:
                    forecast_weather = item["weather"][0]["description"]
                    forecast_temperature = item["main"]["temp"]
                    print(f"{forecast_day}: {forecast_weather.capitalize()}, Sıcaklık: {forecast_temperature}°C")
                    break
    else:
        print("Şehir bulunamadı.")

if __name__ == "__main__":
    city = input("Hava durumunu öğrenmek istediğiniz şehri girin: ")
    get_weather(city)
