#!/usr/bin/env python3

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import datetime as dt
from crontab import CronTab


#Load Bitcoin price data from csv file
df = pd.read_csv('btc.csv', names = ['date', 'price'])

# Define the app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
html.H1(children='Bitcoin Price Dashboard Aymeric Thiault IF4'),
dcc.Graph(id='bitcoin-price-graph'),
dcc.Interval(id='interval-component',interval=5*60*1000,n_intervals=0)])

# Define the callback function to update the graph
@app.callback(Output('bitcoin-price-graph', 'figure'),
[Input('interval-component', 'n_intervals')])

def update_graph(n):
  #Load Bitcoin price data from csv file
  df = pd.read_csv('btc.csv', names = ['date', 'price'])

  #Create the time series graph
  data = [go.Scatter(x=df['date'], y=df['price'])]
  layout = go.Layout(title='Bitcoin Price', xaxis=dict(title='date'), yaxis=dict(title='price'))
  figure = go.Figure(data=data, layout=layout)

return figure

# Define the function to create daily report

def create_daily_report():

  #Load Bitcoin price data from csv file
  df = pd.read_csv('btc.csv', names = ['date', 'price'])
  #Calculate daily volatility, open price, close price, and price evolution
  today = dt.date.today()
  yesterday = today - dt.timedelta(days=1)
  today_df = df[df['date'] == str(today)]
  yesterday_df = df[df['date'] == str(yesterday)]
  volatility = today_df['price'].std()
  open_price = today_df.iloc[0]['price']
  close_price = today_df.iloc[-1]['price']
  evolution = (close_price - open_price) / open_price * 100

  #Create the daily report string
  report = f'Daily Report - {today}\n\n'
  report += f'Volatility: {volatility:.2f}\n'
  report += f'Open price: {open_price:.2f}\n'
  report += f'Close price: {close_price:.2f}\n'
  report += f'Evolution: {evolution:.2f}%\n'
  
  #Write the daily report to a text file
  with open(f'daily_report_{today}.txt', 'w') as f:
    f.write(report) 
 

#Schedule the daily report to be created at 8pm each day
cron = CronTab(user = 'ubuntu')
job = cron.new(command='python3 /home/ubuntu/project/dashScript.py --daily-report')
job.setall('0 20 * * *')
cron.write()

#Run the app
if __name__ == '__main__':  
  app.run_server(debug=True, host='0.0.0.0')
