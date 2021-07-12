import requests

##Docs located at: https://www.exchangerate-api.com/docs/standard-requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/4d1b4bfa298d8d3186159264/latest/USD'

# Making our request
response = requests.get(url, verify=False)
data = response.json()

# Your JSON object
print(data)
	
