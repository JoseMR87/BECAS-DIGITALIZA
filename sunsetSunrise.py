import requests

url = "https://api.sunrise-sunset.org/json?lat=40.714270&lng=-74.0059"
json = requests.get(url).json()
print ("La hora del amanecer en Nueva York es:", json['results']['sunrise'])
print ("La hora de la puesta de sol en Nueva York es:", json['results']['sunset'])