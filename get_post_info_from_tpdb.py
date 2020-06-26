from bs4 import BeautifulSoup
import urllib.request
from urllib.error import URLError, HTTPError

# save content
def saveContent(data):
  f = open("test.txt", "wb")
  f.write(data)
  f.close

# get http response
def getResponse(url):

  try:
    headers = {'User-Agent':'Chrome/83.0.4103.116'}
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req)

  except HTTPError as e:
    err = e.read()
    code = e.getcode()

  html = res.read()
  res.close()

  # print(source)
  return html

def parsingData(html):

  soup = BeautifulSoup(html, 'html.parser')

  allPoster = soup.findAll('div', {'class':'overlay rounded'})
  allPosterName = soup.findAll('p', {'class':'p-0 mb-1 text-break'})

  for poster in allPoster:
    print(poster.find('p', {'class':'p-0 mb-1 text-break'}).text, ' = ', 'https://theposterdb.com/api/assets/',poster['data-poster-id'], sep='')


################### run ######################

url = 'https://theposterdb.com/set/253'

html = getResponse(url)

parsingData(html)

# saveContent(html)