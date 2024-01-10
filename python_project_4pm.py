# -*- coding: utf-8 -*-
"""python_project_4pm

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12qiPirtQe9spus3uNKuav230131sY7Iw
"""

#!pip install beautifulsoup4

from bs4 import BeautifulSoup
import requests
url = BeautifulSoup('https://www.worldometers.info/coronavirus/', 'html.parser')
soup = requests.get(url)
# print(soup)



code = BeautifulSoup(soup.text, "lxml")
code = code.table

data = []
tags = code.find_all('tr')
for tag in tags:
  y = tag.text.split('\n')
  if y[1] != "":
    data.append(y[1:])

import csv
file = open('covid_data.csv','w')
x = csv.writer(file)
x.writerows(data)
file.close()

import pandas as pd
df = pd.read_csv('covid_data.csv', encoding = "latin1")
print(df)

df = df.iloc[0:10]

df['TotalCases'] = list(map(lambda x: int(x.replace(',','')),df['TotalCases']))

df['TotalDeaths'] = list(map(lambda x: int(x.replace(',','')),df['TotalDeaths']))

import plotly.express as px
fig = px.bar(df, x='Country,Other', y='TotalCases')
fig.show()

import plotly.graph_objects as go
fig = go.Figure(data=[
    go.Bar(name='TotalCases', x=df['Country,Other'], y=df['TotalCases']),
    go.Bar(name='TotalDeaths', x=df['Country,Other'], y=df['TotalDeaths'])
])
# Change the bfig.show()ar mode
fig.update_layout(barmode='group')

import plotly.express as px
fig = px.pie(df, values='TotalCases', names='Country,Other', title='Covid Cases Of 10 Countries')
fig.show()