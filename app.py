from datetime import datetime
import pandas as pd
import quandl
import matplotlib.pyplot as plt
import requests
from flask import Flask
# import sys
# Creating variables sent in the rquest

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>hello</h1>'

# @app.route('/generateChart')
# def generateChart(ticker, start_date, end_date):
#     ticker = requests.args.get('ticker')
#     start_date = requests.args.get('start_date')
#     end_date = requests.args.get('end_date')
#     api_key = requests.args.get('api_key')
#     df = get_historical_data(ticker, start_date, end_date, output_format='pandas', token=api_key)
#     plt.plot(df.index, df['close'])
#     plt.xlabel("date")
#     plt.ylabel("$ price")
#     plt.title("Stock Price")
#     df["30-day Moving Average"] = df['close'].rolling(window=30).mean()
#     df["60-day Moving Average"] = df['close'].rolling(window=60).mean()
#     df['ewma'] = df['close'].ewm(halflife=0.5, min_periods=20).mean()
#     plt.figure(figsize=(10,10))
#     plt.plot(df['30-day Moving Average'], 'g--', label="30-day Moving Average")
#     plt.plot(df['60-day Moving Average'], 'r--', label="60-day Moving Average")
#     plt.plot(df['close'], label="End of Day Price")
#     plt.legend()
#     plt.show()

# generateChart(ticker,start_date,end_date)
# ticker = sys.argv[1]
# start_date = sys.argv[2]
# end_date = sys.argv[3]
# quandl.ApiConfig.api_key = sys.argv[4]
# quandl.ApiConfig.api_key="KBmpxPvadzxotsKEm-nQ"

# print("Output from Python") 
# print("ticker: " + sys.argv[1]) 
# print("start_date: " + sys.argv[2]) 
# print("end_date: " + sys.argv[3])
# print("api_key: " + sys.argv[4])

# Getting historical data requested

# plt.figure(figsize=(10,8))

# Render Chart



# if __name__ == "__main__":
#     app.run(debug=True)

# generateChart("MSFT","2018-01-01","2020-08-15")

if __name__ == "__main__":
    app.run()