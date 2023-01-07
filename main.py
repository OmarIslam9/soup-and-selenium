import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
form="https://forms.gle/gEPKy2KQ1zaSycq27"
chrome_drive="/Users/Islam/OneDrive/Desktop/chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_drive)

response=requests.get("https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A38.40110553494251%2C%22east%22%3A-121.35392226171875%2C%22south%22%3A37.14413479175498%2C%22west%22%3A-123.51273573828125%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D",headers=header)
data=response.text
soup=BeautifulSoup(data,"html.parser")
all_links=soup.find_all(class_="property-card-link")
links=[]
for l in all_links:
    href = l["href"]
    if "http" not in href:
        links.append(f"https://www.zillow.com{href}")
    else:
        links.append(href)
print(links)

prices=[]
all_prices=soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-81-1__sc-yipmu-0 wgiFT")
for p in all_prices:
    price=p.text
    prices.append(price)
print(prices)

addresses=[]
all_addresses=soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-81-1__sc-yipmu-0 lpqUkW property-card-link")
for a in all_addresses:
    address=a.text
    addresses.append(address)
print(addresses)

driver.get(form)
time.sleep(5)
linkss=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
linkss.send_keys(links[1])
time.sleep(5)
Add=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
Add.send_keys(addresses[1])
time.sleep(5)
Pricesss=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
Pricesss.send_keys(prices[1])
time.sleep(5)
button=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
button.click()
time.sleep(10)







