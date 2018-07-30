#! python3

#first use of a shebang line^ so that I don't have to run this from idle

"""
My first webscraper
lets see if we cannot get some info on local food trucks
""" 

import re, os, requests, bs4


res = requests.get('http://sf.lobstatruck.com/')
res.raise_for_status()
lobstaTruck = bs4.BeautifulSoup(res.text, 'html.parser')
selElems = lobstaTruck.select('div[class="main4"] > strong ')
results = []
results = selElems[0].getText()
numOfRes = str(len(selElems))

print ("found" + numOfRes + " results")

print (results)
