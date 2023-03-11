from bs4 import BeautifulSoup
import requests

def get_soup(url):
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
  html = requests.get(url, headers = headers)
  soup = BeautifulSoup(html.content,'html.parser')
  return soup