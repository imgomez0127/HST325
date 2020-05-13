from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
states = ["alabama","alaska","arizona","arkansas","california","colorado","connecticut","delaware","district-of-columbia","florida",
          "georgia","hawaii","idaho","illinois","indiana","iowa","kansas","kentucky","louisiana","maine","maryland","massachusetts","michigan","minnesota","mississippi",
          "missouri","montana","nebraska","nevada","new-hampshire","new-jersey","new-mexico","new-york","north-carolina","north-dakota","ohio","oklahoma","oregon","pennsylvania",
          "rhode-island","south-carolina","south-dakota","tennessee","texas","utah","vermont","virginia","washington","west-virginia",
          "wisconsin","wyoming"]
url = "https://dqydj.com/average-income-by-state-median-top-percentiles/"
r = requests.get(url)
soup = BeautifulSoup(r.text,features="lxml")
data = []
for i in range(len(states)):
    data.append([states[i],2019,int(soup.find_all("table")[1].find_all("tr")[i+1].find_all("td")[-1].text.replace("$","").replace(",","")[:-3])])
print(data)
pd.DataFrame(data).to_csv("test2.csv",header=False,index=False)
