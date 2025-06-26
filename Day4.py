#csv = comma seperated value
# import csv
#
# data = [
#     ["name","age", "country"],
#     ["John", "29", "China"],
#     ["akshit","19","india"],
#     ["Ashish","21","USA"]
# ]
# with open('data.csv','w', newline="") as file:
#
#     writer = csv.writer(file)
#
#     for x in data:
#         writer.writerow(x)
#
# with open('data.csv','r', newline="") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
from math import degrees

#Exceptions handling
# try:
#     n1 = int(input("Enter a number:"))
#     y = 25/n1
#     print(y)
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except ValueError:
#     print("Number required")


#API = Application programming interface
# pip install request
# import requests
# def weather (cityy):
#     url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid=5037f55e942dee6751db608fc6d2526d"
#     final_url = url.format(city=cityy)
#     try:
#         response = requests.get(final_url)
#         data = response.json()
#         print(f"Temperature is {data['main']['temp']} kelvin(feels like:{data['main']['feels_like']}Kelvin)")
#         print(f"humidity is {data['main']['humidity']}%")
#         print(f"Wind Speed is {data['wind']['speed']}")
#         print(f"description is {data['weather'][0]['description']}")
#         print(f"country is {data['sys']['country']}")
#
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching weather data: {e}")
#
#     # city =input("Enter the city name: ")
# weather(input("Enter the city name: "))

    # dict ={"coord":{"lon":75.8167,"lat":26.9167},
    #        "weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],
    #        "base":"stations",
    #        "main":{"temp":303.29,
    #                "feels_like":307.8,
    #                "temp_min":303.29,
    #                "temp_max":303.29,
    #                "pressure":1000,
    #                "humidity":67,
    #                "sea_level":1000,
    #                "grnd_level":953},
    #        "visibility":10000,
    #        "wind":{"speed":7.96,
    #                "deg":276,
    #                "gust":8.25},
    #        "clouds":{"all":100},
    #        "dt":1750653133,
    #        "sys":{"country":"IN",
    #               "sunrise":1750637032,
    #               "sunset":1750686832},
    #        "timezone":19800,
    #        "id":1269515,
    #        "name":"Jaipur",
    #        "cod":200}











