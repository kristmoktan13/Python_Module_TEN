import requests
API_KEY = "0371c9a5dc3f6b98c8146686dcaa19ad"
city = input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
response = requests.get(url)
data = response.json()
if response.status_code == 200:
    description = data["weather"][0]["description"]
    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15
    print(f"Condition: {description}")
    print(f"Temperature: {temp_celsius:.1f} °C")
else:
    print(f"City not found: {data['message']}")