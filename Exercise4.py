'''
4. Write a Python code to send a request to a web page, and print
the information of headers. Also parse these values and print 
key-value pairs holding various information.

'''

import requests
r = requests.get('https://api.github.com/')
response = r.headers
print("Headers information of the said response:")
print(response)
print("\nVarious Key-value pairs information of the said resource and request:")

for key,value in response.items():
    print(f"{key} = {value}")