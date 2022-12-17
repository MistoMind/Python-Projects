import requests
from bs4 import BeautifulSoup
import smtplib

AMAZON_PRODUCT_URL = "https://www.amazon.in/ASUS-15-6-inch-i7-12700H-RTX-3050-FX507ZE-HN038W/dp/B09TTFTFQH"

header = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}
response = requests.get(url=AMAZON_PRODUCT_URL, headers=header).text

soup = BeautifulSoup(response, "html.parser")
price = soup.find(name="span", class_="a-price-whole").getText()
price = price.split(".")[0].split(",")
price = int("".join(price))

if price < 120000:
    MY_EMAIL = "khushseervi@gmail.com"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, "tqoentshixfgjime")
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:The price is lower.\n\nThe price of the product is {price}"
    )
