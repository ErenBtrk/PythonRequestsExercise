'''
9. Write a Python code to verify the SSL certificate for a website which is certified.

'''

import requests   
#Requests ignore verifying the SSL certificate if you set verify to False
# Making a get request 
response = requests.get('https://rigaux.org/', verify=False)
print(response) 
print("\n=======================================================\n")
#Requests verifies SSL certificates for HTTPS requests, just like a web browser.
response1 = requests.get('https://google.com/')
print(response1)
print("\n=======================================================\n")
#Requests ignore verifying the SSL certificate if you set verify to True (Default value)
response1 = requests.get('https://rigaux.org/', verify=True)
print(response1) 