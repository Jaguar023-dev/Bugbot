import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import SESSION_PATH

def init_whatsapp_session():
    if not os.path.exists(SESSION_PATH):
        os.makedirs(SESSION_PATH)

    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={SESSION_PATH}")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--headless")  # Optional

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://web.whatsapp.com")

    print("Scan QR code if this is your first run...")
    time.sleep(15)
    print("WhatsApp session initialized! Session will persist automatically next time.")
    return driver