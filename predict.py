import click
import requests
import pandas as pd
import json
import yfinance as yf
from yahoofinancials import YahooFinancials
from datetime import date, timedelta


def test():
    df = pd.read_csv("TWTR.csv")

    close = df["Close"].tolist()
    volume = df["Volume"].tolist()

    requests.get("http://35.231.236.253:5000/balance").json()

    for i in range(1):
        data = json.dumps([close[i], volume[i]])
        requested = requests.get("http://35.231.236.253:5000/trade?data=" + data).json()
        print(requested)


@click.command()
@click.option("--name", prompt="Enter Stock Name", help="The stock you want to check.")
def show_data(name):
    today = date.today()
    dta = timedelta(days=30)
    prev = today - dta
    d1 = today.strftime("%Y-%m-%d")
    d2 = prev.strftime("%Y-%m-%d")
    # Specify Dataframe and download past months figures
    df = yf.download(name, start=d2, end=d1, progress=False)

    close = df["Close"].tolist()
    volume = df["Volume"].tolist()

    requested = requests.get("http://35.231.236.253:5000/balance").json()
    print(requested)

    for i in range(len(close)):
        data = json.dumps([close[i], volume[i]])
        requested = requests.get("http://35.231.236.253:5000/trade?data=" + data).json()
        print(requested)


@click.command()
@click.option("--money", prompt="Enter Amount", help="To reset money")
def reset_money(money):
    requested = requests.get("http://35.231.236.253:5000/reset?money=" + money).json()
    print(requested)


if __name__ == "__main__":
    # reset_money()
    show_data()
