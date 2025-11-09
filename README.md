# 🏠 Zillow Data Scraper & Google Form Automation

This project automatically scrapes property listings (addresses, prices, and links) from the **Zillow Clone** website and submits them into a **Google Form**, which stores the data in a linked **Google Spreadsheet**.

---

## 🚀 Features

- Scrapes property listings using **BeautifulSoup**
- Cleans and formats data for readability
- Automates form submissions with **Selenium WebDriver**
- Automatically stores listing data in a **Google Sheet**
- Easy to modify for your own form or dataset

---

## 🧠 Technologies Used

- Python 3
- Requests
- BeautifulSoup (bs4)
- Selenium
- Google Forms / Sheets

---

## ⚙️ How It Works

1. **Scrape Data**  
   The script requests and parses data from the Zillow Clone site:
   - Property **links**
   - Property **prices**
   - Property **addresses**

2. **Clean Data**  
   Removes unnecessary symbols and formatting for cleaner output.

3. **Submit Data Automatically**  
   Uses Selenium to:
   - Open the Google Form
   - Input property details
   - Submit entries automatically

4. **Store Results**  
   The submitted data appears in your linked Google Spreadsheet.

---

## 🧩 Setup Instructions

### 1️⃣ Install Dependencies
```bash
pip install requests beautifulsoup4 selenium
```

### 2️⃣ Download ChromeDriver  
Make sure you have **Google Chrome** and **ChromeDriver** installed.  
You can download ChromeDriver from:  
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

### 3️⃣ Update Google Form Link  
Replace the placeholder form link in the code:
```python
GOOGLE_FORM_LINK = "https://docs.google.com/forms/..."
```

### 4️⃣ Run the Script
```bash
python main.py
```

The script will open the browser, fill out the form automatically, and close after submission.

---

## 📊 Spreadsheet Output

Your collected data will appear in the linked Google Sheet:  
👉 [**View Spreadsheet**](https://docs.google.com/spreadsheets/d/1dEpcLPnwuPm1bJKvF-TSp7ZtvONy4eUV2dtHDNkaBRE/edit?usp=sharing)

---

## 🧑‍💻 Author

**Param Sangani**  
Python Developer | Automation Enthusiast  
📧 *Contact via GitHub or LinkedIn*

---

## ⚠️ Disclaimer
This project is for **educational purposes only**.  
Do not use it for scraping or automating data from real Zillow or other sites without permission.
