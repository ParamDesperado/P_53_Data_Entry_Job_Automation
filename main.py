import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSeqWYydQcYC0YQuYUs7uG4WBcDi3BRpdvOf2eGOyJTwORDSKg/viewform?usp=publish-editor"
FINAL_PRODUCT_LINK="https://docs.google.com/spreadsheets/d/1dEpcLPnwuPm1bJKvF-TSp7ZtvONy4eUV2dtHDNkaBRE/edit?usp=sharing"
response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
zillow_website = response.text

soup = BeautifulSoup(zillow_website, "html.parser")

# ----------------------------
# LINKS
# ----------------------------
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link.get("href") for link in all_link_elements]

for i in range(len(all_links)):
    if not all_links[i].startswith("https"):
        all_links[i] = f"https://appbrewery.github.io{all_links[i]}"

print("LISTING LINKS:")
print(all_links)
print()

# ----------------------------
# PRICES
# ----------------------------
all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text() for price in all_price_elements]

clean_prices = []
for price in all_prices:
    price = price.strip()
    price = price.split('+')[0].split('/')[0].strip()
    clean_prices.append(price)

print("CLEAN PRICES:")
print(clean_prices)
print()

# ----------------------------
# ADDRESSES
# ----------------------------
all_address_elements=soup.select(".StyledPropertyCardDataWrapper address")
raw_addresses = [addr.get_text() for addr in all_address_elements]

clean_addresses = []
for addr in raw_addresses:
    addr = addr.replace("\n", "").replace("|", "").strip()
    clean_addresses.append(addr)

print("CLEAN ADDRESSES:")
print(clean_addresses)
print()

# ----------------------------
# SAFELY COMBINE ALL LISTINGS
# ----------------------------
min_length = min(len(all_links), len(clean_prices), len(clean_addresses))
listings = []
for i in range(min_length):
    listings.append({
        "link": all_links[i],
        "price": clean_prices[i],
        "address": clean_addresses[i]
    })

print("ALL LISTINGS:")
for listing in listings:
    print(listing)

# ----------------------------------------------------
# SUBMIT TO GOOGLE FORM (with Selenium)
# ----------------------------------------------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for i in range(len(all_links)):
    driver.get(GOOGLE_FORM_LINK)
    time.sleep(2)

    # Update these XPaths if your form has different field order
    address_field = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_btn = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address_field.send_keys(clean_addresses[i])
    price_field.send_keys(clean_prices[i])
    link_field.send_keys(all_links[i])
    submit_btn.click()

    print(f"Submitted form #{i+1}")
    time.sleep(1)

driver.quit()