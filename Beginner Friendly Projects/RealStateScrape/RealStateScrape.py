import requests
from bs4 import BeautifulSoup
import pandas as pd
import time as ty
import sys
from itertools import zip_longest
import pandas as pd



#فارسی 
sys.stdout.reconfigure(encoding='utf-8')  # ست کردن UTF-8 برای خروجی





def scraper(link, pages):
    full_data = []
    desc_data = []
    price_data = []
    loc_data = []
    feature_data = []
    link_data = []
    time_data = []
    index = 0





    for page in range(1 , pages + 1): 
       
        url = link.format(page)
        #Response
        response = requests.get(url)
        
        if response.status_code == 200:

            #parse HTMl
            soup = BeautifulSoup(response.content, "lxml")


            #Description
            descriptions = soup.find_all("h2", class_ = "text-xs font-bold leading-[18px] md:text-sm text-grey-600")
            for description in descriptions:
                desc_data.append(description.get_text(strip=True))
            



            #Price
            prices = soup.find_all("span", class_ = "text-lg font-bold")
            for price in prices:
                price_data.append(price.get_text(strip=True))
            



            #Location
            p_tags = soup.find_all("p", class_ = "inline-flex text-grey-500")

            for p_tag in p_tags:
                loc_data.append( p_tag.find("span").text)
                

            #Features
            features_divs = soup.find_all("div", class_ = "inline-flex flex-wrap -m-2")

            for div in features_divs:
                spans = div.find_all("span")
                feature_text = "-".join(span.get_text(strip=True).replace(" ", "-")for span in spans)
                feature_data.append(feature_text)
                
            

            #Links
            links = soup.find_all('a', class_ = "style_plp-card-link__yPlrt")
            for a_tag in links:               
                link_data.append(a_tag.get("href"))
                


            #time of the publicize
            timess = soup.find_all("span", class_ ="hidden text-sm text-grey-500 md:inline-block")
            

            for timee in timess:
                
                zamann = timee.get_text(strip=True)
                time_data.append(zamann)
                  

                
            

            #for loop
            for tozihat, gheymat, makan, vizhegi, address, zaman in zip_longest(desc_data, price_data, loc_data,feature_data,link_data,time_data):
                full_data.append((index,tozihat, gheymat, makan, vizhegi, address, zaman))
                
                #index
                index += 1
                #timesleep
                #ty.sleep(1)
    return full_data
        

            
          
             







if __name__ == "__main__":
    link = str('https://kilid.com/buy/tehran?page={}&size=25&sort=trueCheck_desc,searchDate_desc')
    
       # Debugging check
    if link is None:
        print("Error: 'link' is None!")
        sys.exit(1)  # Stop execution if link is None

    print(f"Using link: {link}")  # Confirm that link is correctly assigne
      
    pages = 4
    
   
    df = pd.DataFrame(scraper(link, pages), columns=["Index","Tozihat", "Gheymat", "Makan", "Vizhegi", "Address", "Zaman"])
    print(df)


    df.to_csv("RealStateScape.csv",encoding="utf-8", index=False)
    




    #api shit and email it
    #use pylint