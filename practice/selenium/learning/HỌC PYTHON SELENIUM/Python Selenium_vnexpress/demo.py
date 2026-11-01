from selenium import webdriver
from selenium.webdriver.common.by import By

# Khởi tạo trình điều khiển Chrome
driver = webdriver.Chrome()  # Không cần executable_path nếu chromedriver đã có trong PATH
# driver = webdriver.Chrome(executable_path="/Users/lahieuphong/Documents/Python Selenium/chromedriver-mac-arm64/chromedriver")

# Mở trang web
driver.get("https://vnexpress.net/")

# In tiêu đề trang
print(driver.title)

# Tìm tất cả các phần tử theo CSS selector
elements = driver.find_elements(By.CSS_SELECTOR, "article.item-news h3")

# In nội dung của từng phần tử
for el in elements:
    print(el.text)

# Đóng trình duyệt
driver.quit()