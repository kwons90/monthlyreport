from datetime import datetime
import pandas as pd
import quandl
import matplotlib.pyplot as plt
import requests
from flask import Flask
# import sys
# Creating variables sent in the rquest

# utils
mapDict = {
    'EV/EBITDA':'evebitda',
    'P/E': 'pe',
    'P/B': 'pb'
}

def parseTime(strdate):
    l = strdate.split('-')
    return datetime.datetime(int(l[0]),int(l[1]),int(l[2]))

# Initialize server
app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return '<h1>hello</h1>'

@app.route('/generateChart')
def generateChart(ticker,label, start_date,end_date):
    df = quandl.get_table('SHARADAR/DAILY', ticker=ticker) 

    # Parsing to the pandas label
    method = mapDict[label]
    
    # Mapping rolling average
    df["30-day Moving Average"] = df[method].rolling(window=30).mean()
    df["60-day Moving Average"] = df[method].rolling(window=60).mean()

    # Create a boolean in the time range after parsing string into datetime
    start_time = parseTime(start_date)
    end_time = parseTime(end_date)
    mask = (df['date'] > start_time) & (df['date'] <= end_time)
    
    # Generate average
    df["Average for Period"] = df.loc[mask][method].mean()

    #Chart
    plt.xlabel("Date")
    plt.ylabel(label)
    plt.title('Historical {label}'.format(label=label))
    plt.figure(figsize=(10,10))
    plt.plot(df.loc[mask].date, df.loc[mask]['30-day Moving Average'], 'g', label="30-day Moving Average")
    plt.plot(df.loc[mask].date, df.loc[mask]['60-day Moving Average'], 'r', label="60-day Moving Average")
    plt.plot(df.loc[mask].date, df.loc[mask]['Average for Period'], 'b', label="Average for Period")
    plt.plot(df.loc[mask].date, df.loc[mask]['evebitda'], 'k', label=label)
    plt.legend()
    jpegFile = plt.savefig('testplot.png')
    return jpegFile

if __name__ == "__main__":
    app.run()