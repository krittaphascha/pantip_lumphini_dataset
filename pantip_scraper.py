from bs4 import BeautifulSoup
import lxml
import pandas as pd
import requests

r = requests.get('www.google.com')
print(r)