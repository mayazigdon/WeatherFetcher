import requests
API_KEY = "15808e9b610f748e628b1895e8786263"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter A City: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temp = round(data['main']['temp']-273.15, 2)

    print("the weather is : ", weather)
    print("the temperature is: ", temp, "celsius")
else:
    print("an error has occur")





