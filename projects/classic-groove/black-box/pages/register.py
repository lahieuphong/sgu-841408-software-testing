import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_driver import chrome_driver


def get_notice_text(chrome_driver):
    # Wait for the notice div to appear after form submission
    notice_element = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.ID, "notice"))
    )

    # Get the text inside the notice div
    notice_text = notice_element.text

    return notice_text


def generate_random_username(length=10):
    # Các ký tự có thể sử dụng: chữ cái (hoa + thường), chữ số, và ký tự đặc biệt
    special_characters = string.punctuation  # Tạo danh sách ký tự đặc biệt
    characters = string.ascii_letters + string.digits + special_characters

    # Tạo tên người dùng ngẫu nhiên
    return ''.join(random.choice(characters) for i in range(length))