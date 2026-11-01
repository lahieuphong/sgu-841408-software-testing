from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class LoginTests(unittest.TestCase):
    def setUp(self):
        # Khởi tạo trình duyệt
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://example.com/login")

    def tearDown(self):
        # Đóng trình duyệt
        self.driver.quit()

    def test_login_with_valid_credentials(self):
        driver = self.driver
        driver.find_element(By.ID, "email").send_keys("validuser@example.com")
        driver.find_element(By.ID, "password").send_keys("validpassword")
        driver.find_element(By.ID, "login-button").click()

        # Kiểm tra xem trang chính có hiển thị hay không
        self.assertIn("Welcome Page", driver.page_source)

    def test_login_with_invalid_email(self):
        driver = self.driver
        driver.find_element(By.ID, "email").send_keys("invaliduser@example.com")
        driver.find_element(By.ID, "password").send_keys("validpassword")
        driver.find_element(By.ID, "login-button").click()

        # Kiểm tra thông báo lỗi
        self.assertIn("Invalid email or password", driver.page_source)

    def test_login_with_invalid_password(self):
        driver = self.driver
        driver.find_element(By.ID, "email").send_keys("validuser@example.com")
        driver.find_element(By.ID, "password").send_keys("invalidpassword")
        driver.find_element(By.ID, "login-button").click()

        # Kiểm tra thông báo lỗi
        self.assertIn("Invalid email or password", driver.page_source)


if __name__ == "__main__":
    unittest.main()
