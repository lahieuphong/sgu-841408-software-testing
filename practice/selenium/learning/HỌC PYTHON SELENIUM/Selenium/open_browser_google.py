from selenium import webdriver
from time import sleep
import os

# Path to the profile directory where data will be saved
account_google = '/Users/lahieuphong/Documents/Selenium/account_google'

# Launch Chrome with the correct command
os.popen('/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --user-data-dir=/Users/lahieuphong/Documents/Selenium/account_google --remote-debugging-port=8990')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={account_google}")
chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:8990')

driver = webdriver.Chrome(options=chrome_options)
sleep(1)
driver.get('https://accounts.google.com')
sleep(2)
print('Browser loaded successfully')