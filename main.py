import requests, json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

CITY = input("Enter name of the city:")

API_KEY = 'a3664fd42385abd8fa358c01042d3fdd'

URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

response = requests.get(URL)

if response.status_code == 200:

    data = response.json()#

    main = data['main']

    temperature = (main['temp']-273.5)

    humidity = main['humidity']

    pressure = main['pressure']

    #report = main['weather']

    print(f"{CITY} \n Temperature: {temperature} \n Humididty: {humidity} \n Pressure: {pressure}")

    #print(f"Weather Report: {report[0]['description']}")

else:

    print("Error! Fetching Data. Try Again!")
    print(response)