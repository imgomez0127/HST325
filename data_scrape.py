from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
states = ["alabama","alaska","arizona","arkansas","california","colorado","connecticut","delaware","district-of-columbia","florida",
          "georgia","hawaii","idaho","illinois","indiana","iowa","kansas","kentucky","louisiana","maine","maryland","massachusetts","michigan","minnesota","mississippi",
          "missouri","montana","nebraska","nevada","new-hampshire","new-jersey","new-mexico","new-york","north-carolina","north-dakota","ohio","oklahoma","oregon","pennsylvania",
          "rhode-island","south-carolina","south-dakota","tennessee","texas","utah","vermont","virginia","washington","west-virginia",
          "wisconsin","wyoming"]
years = [2017,2016,2015,2014,2013,2012,2011,2010,2009,2008]
flag = True
data = {}
for state in states:
    url = "".join(["https://www.deptofnumbers.com/income/"+state+"/"])
    r = requests.get(url)
    soup = BeautifulSoup(r.text,features="lxml")
    print(state)
    for i in range(len(years)):
        print(list(soup.find_all("table")[1].find_all("tr")[i+1])[-2].text.replace("$","").replace(",",""))
        data[years[i]] = data.get(years[i],[])+ [list(soup.find_all("table")[1].find_all("tr")[i+1])[-2].text.replace("$","").replace(",","")]
print(data)
all_data = []
for year in reversed(list(data.keys())):
    median_salaries = data[year]
    for i,salary in enumerate(median_salaries):
        all_data.append([states[i],year,salary])
all_salaries = np.asarray(all_data)
pd.DataFrame(all_data).to_csv("test.csv",header=False,index=False)


