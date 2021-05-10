import requests, json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

CITY = input("Enter name of the city: ")

API_KEY = 'a3664fd42385abd8fa358c01042d3fdd' #Get your API Key from openweather

URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

response = requests.get(URL)


if response.status_code == 200:

    data = response.json()
    #print(data)
    main = data['main']

    temperature = round((main['temp']-273.5),2)

    feelslike = round((main['feels_like']-273.5),2)

    humidity = main['humidity']

    pressure = main['pressure']

    visibility = int(data['visibility'])/1000.0

    #Country = data['country']

    #report = main['weather']

    print(f"{CITY} \n Temperature: {temperature} °C \n Feels-like: {feelslike} °C \n Humididty: {humidity} g/m3 \n Pressure: {pressure} mmHg \n visibility: {visibility} km")

    #print(f"Weather Report: {report[0]['description']}")

else:

    print("Error! Fetching Data. Try Again!")
    print(response)
