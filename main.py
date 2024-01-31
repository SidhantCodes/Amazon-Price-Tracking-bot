from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
url = input("Enter the url of the amazon product here: ")
tgt_price = float(input("Enter the target amount: "))
site = requests.get(
    url, headers={"User-Agent":"Mozilla/5.0", "Accept-Language":"en-US,en;q=0.5"}
    )
# print(site.text)
soup = BeautifulSoup(site.content, "lxml")
# print(soup.prettify())
product_title = soup.find(name="span", id="productTitle").getText().strip()
print("Product Title: "+product_title)

product_price = float((soup.find(name="span", class_="a-price-whole").getText().strip()[:-1]).replace(',',''))

print("Current Price: "+str(product_price))

if product_price<tgt_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        sender_email = os.getenv("EMAIL")
        sender_password = os.getenv("PASSWORD")
        receiver_email = os.getenv("RECEIVER_EMAIL")
        message = f"{product_title} is now {product_price}"
        connection.starttls()
        result = connection.login(sender_email, sender_password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )