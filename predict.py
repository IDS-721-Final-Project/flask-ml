import requests
import pandas as pd
import json

df = pd.read_csv('TWTR.csv')

close = df['Close'].tolist()
volume = df['Volume'].tolist()

requests.get('http://35.231.236.253:5000/balance').json()

for i in range(200):
    data = json.dumps([close[i], volume[i]])
    requested = requests.get('http://35.231.236.253:5000/trade?data=' + data).json()
    print(requested)
