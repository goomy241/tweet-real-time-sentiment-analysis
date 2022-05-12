import requests

query = {'text':'Leftists lose it over Joe Manchin thwarting Dem abortion bill'}
response = requests.get('http://127.0.0.1:8000/sentiment_analysis/', params=query)
print(response.json())