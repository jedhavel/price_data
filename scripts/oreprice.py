from urllib.request import Request, urlopen
import schedule
import time
import os
import json
from secrets import * # Put your api keys here
from config import *

class OreTicker():

  # Call the PancakeSwap API
  def callpcs():
    req = Request("https://api.pancakeswap.info/api/v2/tokens/0x8e2D8f40818FbaBA663Db6a24FB9B527Fc7100BE", headers={'User-Agent': 'Mozilla/5.0'}) # Arbitray user-agent to pass pcs "security"
    data = urlopen(req).read()
    price = json.loads(data)["data"]["price"]
    time = json.loads(data)["updated_at"]
    print(f"Price: {price}, DTG: {time}")

import urllib.request
url = "https://api.nomics.com/v1/currencies/ticker?key=21cfa690359b2042f96a3cb8e3c4918272bdd4ff&ids=ORE4&interval=1d,30d&convert=USD&per-page=100&page=1"
print(urllib.request.urlopen(url).read())

url = "https://api.nomics.com/v1/volume/history?key=21cfa690359b2042f96a3cb8e3c4918272bdd4ff&ids=ORE4&start=2021-09-17T00%3A00%3A00Z&end=2021-10-25T00%3A00%3A00Z&convert=USD"
print(urllib.request.urlopen(url).read())

  def callbscscan():
    QF8KMKBK48MR3JNDTKDUPH8HB59Z4FD82N

  def getvolume():
    url = f"https://api.nomics.com/v1/volume/history?key={api_keys["nomics"]}&start=2021-09-17T00%3A00%3A00Z&end=2021-10-25T00%3A00%3A00Z&convert=USD"
    print(urllib.request.urlopen(url).read())

  def getprice(api):
    if api == "nomics":
      ID  = "ORE4"
      url = f"https://api.nomics.com/v1/currencies/ticker?key={api_keys["nomics"]}&ids={ID}&interval=FALSE&convert=USD"
      filename = "ORE.js"
      filepath = "/var/www/html/price"
      data = urllib.request.urlopen(url).read()
      price = json.loads(data)[0]["price"]
      time = json.loads(data)[0]["price_timestamp"]

      js = "[{\"symbol\":\"ORE" + f"\",\"price_usd\":\"{price}\",\"last_updated\":{time}" + "}]"
      print("Working...")
      with open(os.path.join(filepath, filename), "w") as f:
        f.write(js)
    else if api == "cmc"

  def run(fun):
    schedule.every(interval).minutes.do(getprice)
    while True:
        schedule.run_pending()
        time.sleep(interval)

#callpcs()
#getprice()
