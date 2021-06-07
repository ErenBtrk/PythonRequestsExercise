'''
6. Write a Python code to send a request to a web page and stop waiting
for a response after a given number of seconds. In the event of times
out of request, raise Timeout exception

'''

import requests
print("timeout = 0.001")
try:
    r = requests.get('https://github.com/', timeout = 0.001)
    print("Connected....")
except requests.exceptions.RequestException as e:
    print(e)    

print("\ntimeout = 1.0")    
try:
    r = requests.get('https://github.com/', timeout = 1.0)
    print("Connected....!")
except requests.exceptions.RequestException as e:
    print(e)