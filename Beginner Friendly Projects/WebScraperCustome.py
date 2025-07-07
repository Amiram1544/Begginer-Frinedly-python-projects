from bs4 import BeautifulSoup
import requests
import sys
import time
from datetime import datetime
import pandas as pd
import re

#فارسی 
sys.stdout.reconfigure(encoding='utf-8')  # ست کردن UTF-8 برای خروجی





def remove_persian(text):
    persian =re.compile(r'[\u0600-\u06FF]+')
    return re.sub(persian, '', text).strip()
    






#first get the basics

def scraper(link, pages):

    data = []
    index = 1

    for page in range(1, pages+1 ):
        url = f"{link}&page={page}"
        response = requests.get(url)


        #if true
        if response.status_code == 200:

            #parsing
            soup = BeautifulSoup(response.text, "lxml")

            #names
            names = soup.find_all("h6", class_ = "font-weight-bold ltr")
            #prices
            prices = soup.find_all("button", class_ = "btn green-btn")

            print(f"\n ♠️  Page {page} ♠️")
            print("=" * 60)



            
            for name, price in zip(names, prices):
                
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                product_name = remove_persian(name.get_text(strip=True))
                product_price = remove_persian(price.get_text(strip=True))
                

                data.append((index, now, product_name, product_price))
                index += 1

                #print(product_name)
                #print(product_price)
                #print("-" * 60)

    return data



            

















if __name__ == "__main__":

    link = "https://pspro.ir/category/Gaming-Keyboard?sort=p.viewed&order=DESC&limit=75"
    pages = 3

    #scrape:
    scraper(link, pages)

    #time for file name
    file_time = datetime.now().strftime("%d %m %Y_%H-%M-%S")
    
    

    #dataframe creation
    df = pd.DataFrame(scraper(link,pages), columns= ["Index","Time", "Product Name", "Price"])
    print(df)


    df.to_csv(f"scraped_data_{file_time}.csv", encoding="utf-8", index=False)


