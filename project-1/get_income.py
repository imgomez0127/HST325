import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import time
import csv
def get_average_income(zip_code):
    numbers_regex = re.compile("[0-9]+")
    r = requests.get("https://www.incomebyzipcode.com/newyork/"+str(zip_code))
    parser = BeautifulSoup(r.text,'lxml')
    try:
        price_string = parser.find_all("td", class_="hilite")[1].contents[0]
    except:
        return 0
    return int("".join(numbers_regex.findall(price_string)))

if __name__ == "__main__":
    df = pd.read_csv("nyc_zipcode_population.csv")
    income_map = []
    zip_codes = list(np.asarray(df["ZIPCODE"]))
    population = list(np.asarray(df["POPULATION"]))
    for zip_code,population in zip(zip_codes,population):
        income = get_average_income(zip_code)
        income_map.append([zip_code,income])
        time.sleep(1)
        print(zip_code)
        print(income)
    data = pd.DataFrame(income_map)
    data.to_csv("income.csv",index=False)
    print(data)