import time
import logging
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Cấu hình logging để xem thông tin debug
logging.basicConfig(level=logging.DEBUG)

# Cài đặt service cho Firefox
service = FirefoxService(GeckoDriverManager().install())

# Khởi động trình duyệt Firefox
options = Options()
options.headless = True  # Chạy Firefox không hiển thị giao diện

driver = webdriver.Firefox(service=service, options=options)

# Thiết lập kích thước cửa sổ trình duyệt
driver.set_window_size(1920, 1080)

# Mở một trang web
driver.get("https://demo.opencart.com/")

# Đợi 20 giây
time.sleep(20)

# Đóng trình duyệt sau khi hoàn thành
driver.quit()
