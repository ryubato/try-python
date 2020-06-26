from bs4 import BeautifulSoup
import urllib.request
from urllib.error import URLError, HTTPError

# save content
def saveContent(data):
  f = open("test.txt", "wb")
  f.write(data)
  f.close

# get http response
def getResponseBySetId(setId):

  url = 'https://theposterdb.com/set/' + setId

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

def printPosterNameAndUrl(html):

  soup = BeautifulSoup(html, 'html.parser')

  allPoster = soup.findAll('div', {'class':'overlay rounded'})

  maxLen = 0

  for poster in allPoster:
    strLen = len(poster.find('p', {'class':'p-0 mb-1 text-break'}).text)
    if strLen > maxLen:
      maxLen = strLen

  for poster in allPoster:
    print(str(poster.find('p', {'class':'p-0 mb-1 text-break'}).text).ljust(maxLen), ' | ', 'https://theposterdb.com/api/assets/',poster['data-poster-id'], sep='')


################### run ######################

setId = '253'

html = getResponseBySetId(setId)

printPosterNameAndUrl(html)

# saveContent(html)