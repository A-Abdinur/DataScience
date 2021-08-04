import bs4
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

URL = 'https://www.kaggle.com/c/santander-customer-transaction-prediction/data'
Filetype = ['.csv', '.xlsx']
def scrapedata(URL):
    r =requests.get(URL)
    return r


if __name__ == "__main__":

    #r = scrapedata()
    #print(r)

    import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bank_data.csv')
df.head()

