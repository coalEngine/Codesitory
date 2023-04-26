import requests

url = "https://random-stuff-api.p.rapidapi.com/ai/response"

querystring = {"message":"Hi there, Tell me a joke!","user_id":"420"}

headers = {
	"content-type": "application/octet-stream",
	"Authorization": "q9Oh7Lg7J0Hd",
	"X-RapidAPI-Key": "f9cf5023b1msh6d7ad8eddd16e56p1252b6jsnb0c7ea851f2c",
	"X-RapidAPI-Host": "random-stuff-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())