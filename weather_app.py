import requests

API_KEY = "d42b3aa886b6f1bac9ec447a3125119b"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    print("\nWeather Details:")
    print("City:", data["name"])
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Wind Speed:", wind_speed, "m/s")
    print("Condition:", description)

else:
    print("Error:", data["message"])