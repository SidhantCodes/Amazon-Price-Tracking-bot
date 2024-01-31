from bs4 import BeautifulSoup
import requests
import lxml

site = requests.get(
    "https://www.amazon.in/Seagate-Expansion-1TB-External-HDD/dp/B08ZJDWTJ1/ref=sr_1_3?crid=1UUDKSXYKFXEE&keywords=hard+disk&qid=1706671937&sprefix=hard+disk%2Caps%2C298&sr=8-3", headers={"User-Agent":"Mozilla/5.0", "Accept-Language":"en-US,en;q=0.5"}
    )
# print(site.text)
soup = BeautifulSoup(site.content, "lxml")
# print(soup.prettify())
product_title = soup.find(name="span", id="productTitle").getText().strip()
print(product_title)

product_price = soup.find(name="span", class_="a-price-whole").getText().strip()[:-1]
print(product_price)

