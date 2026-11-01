import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Sao chép mã
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


OPENCART_DEMO_EMAIL = os.environ.get("OPENCART_DEMO_EMAIL", "")
OPENCART_DEMO_PASSWORD = os.environ.get("OPENCART_DEMO_PASSWORD", "")
if not OPENCART_DEMO_EMAIL or not OPENCART_DEMO_PASSWORD:
    raise SystemExit("Set OPENCART_DEMO_EMAIL and OPENCART_DEMO_PASSWORD before running this script.")

# Khởi tạo ChromeDriver mà không cần chỉ định đường dẫn
options = Options()
driver = webdriver.Chrome(options=options)  # Khởi tạo WebDriver

driver.get("https://demo.opencart.com/")

def login(username, password):
    # Wait for the Login link to be clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
    driver.find_element(By.ID, "input-email").send_keys(username)
    driver.find_element(By.ID, "input-password").send_keys(password)
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(2)
    if "My Account" in driver.title:
        print("Login successful")
    else:
        print("Login failed")


def logout():
    driver.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(2)

def navigate_to_page(page_name):
    driver.find_element(By.LINK_TEXT, page_name).click()
    time.sleep(2)
    print(f"Navigated to {page_name}")

def submit_form():
    driver.find_element(By.LINK_TEXT, "Contact Us").click()
    time.sleep(2)
    driver.find_element(By.ID, "input-name").send_keys("Test User")
    driver.find_element(By.ID, "input-email").send_keys("testuser@example.com")
    driver.find_element(By.ID, "input-enquiry").send_keys("This is a test message.")
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    time.sleep(2)
    print("Form submitted")

# Chạy kiểm thử
try:
    login(OPENCART_DEMO_EMAIL, OPENCART_DEMO_PASSWORD)  # Thay đổi tài khoản đăng nhập nếu cần
    submit_form()
    navigate_to_page("Home")
    logout()
finally:
    driver.quit()
