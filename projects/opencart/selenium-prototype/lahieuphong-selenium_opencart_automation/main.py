import time

from get_chrome_driver_with_custom_user_agent import get_driver_with_custom_profile

driver = get_driver_with_custom_profile(r'my_chrome_profile')
# Điều hướng đến trang OpenCart
driver.get("https://demo.opencart.com/")

time.sleep(1200)  # Tạm dừng để xem trang

# Đóng trình duyệt
driver.quit()