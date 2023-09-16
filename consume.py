import requests


# https://urban-space-garbanzo-4rqxrqx9997c7w76-8000.app.github.dev/apimovies/
response = requests.get('https://urban-space-garbanzo-4rqxrqx9997c7w76-8000.app.github.dev/apimovies/')
print(response.json)