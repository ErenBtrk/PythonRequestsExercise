'''
5. Write a Python code to send a request to a web page, and print the JSON
value of the response. Also print each key value of the response.

'''

import requests

response = requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key=90121eb457d5689cc4b2291ba093bb74&language=en-US&page=1")

response = response.json()

for key,value in response.items():
    if(key == "results"):
        for item in response["results"]:
            for key,value in item.items():
                if(key == "title"):
                    print(value)
    