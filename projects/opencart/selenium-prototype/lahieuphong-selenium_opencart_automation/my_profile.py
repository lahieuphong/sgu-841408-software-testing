import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def create_chrome_profile(profile_path):
    """
    Mở Chrome với đường dẫn profile để tạo và cấu hình profile mới.
    Người dùng có thể đăng nhập và thay đổi các cài đặt của Chrome trong cửa sổ này.
    """
    options = Options()
    options.add_argument(f"user-data-dir={profile_path}")
    options.add_argument("start-maximized")  # Mở Chrome toàn màn hình

    # Khởi động Chrome để người dùng cấu hình profile
    print("Đang mở Chrome để tạo profile...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Đợi người dùng tùy chỉnh profile
    print("Cấu hình profile của bạn trong Chrome. Đóng trình duyệt khi hoàn tất.")
    driver.get("https://www.google.com")  # Mở trang Google để kiểm tra
    input("Nhấn Enter sau khi bạn đóng trình duyệt để hoàn tất.")

    driver.quit()
    print(f"Profile đã được tạo tại: {profile_path}")


def get_chrome_driver_with_profile(profile_path):
    """
    Hàm khởi tạo WebDriver với profile đã tạo.
    """
    options = Options()
    options.add_argument(f"user-data-dir={profile_path}")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



if __name__ == "__main__":  # Corrected to use double underscores
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current file
    profile_path = os.path.join(current_directory, "my_chrome_profile")  # Path to profile in the current directory

    # Check if profile does not exist, then create a new profile
    if not os.path.exists(profile_path):
        create_chrome_profile(profile_path)
    else:
        print(f"Profile already exists at: {profile_path}")

    # Start WebDriver with the created profile
    driver = get_chrome_driver_with_profile(profile_path)
    driver.get("https://demo.opencart.com/")

    # Perform necessary actions on the page (e.g., login, check, etc.)
    time.sleep(120)  # Pause to view the page
    driver.quit()