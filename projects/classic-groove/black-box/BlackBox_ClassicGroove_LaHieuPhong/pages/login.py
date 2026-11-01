import time
from selenium.webdriver.common.by import By
from utils.base_driver import chrome_driver


def login_success_customer(chrome_driver):
    # Nhấn nút "Log in"
    login_button = chrome_driver.find_element(By.CSS_SELECTOR, "div.left-button-login input[type='button'][value='Log in']")
    login_button.click()

    # Chờ cho popup hoặc form login xuất hiện
    time.sleep(2)

    # Điền username
    username_field = chrome_driver.find_element(By.ID, "username-field")
    username_field.send_keys("lahieuphong_customer")
    time.sleep(1)

    # Điền password
    password_field = chrome_driver.find_element(By.ID, "password-field")
    password_field.send_keys("Tatooboys123@")
    time.sleep(1)

    # Nhấn nút Login
    submit_button = chrome_driver.find_element(By.CSS_SELECTOR, "div.submit input[type='button'][value='Login']")
    submit_button.click()

    # Chờ để đảm bảo đăng nhập đã hoàn tất
    time.sleep(5)

    # Kiểm tra xem nếu đăng nhập thành công (kiểm tra phần tử có class "info-placeholder" cho thấy người dùng đã đăng nhập)
    try:
        # Kiểm tra phần tử thông tin người dùng (đăng nhập thành công)
        info_placeholder = chrome_driver.find_element(By.CSS_SELECTOR, "div.info-placeholder")
        assert info_placeholder.is_displayed(), "Đăng nhập không thành công: Không tìm thấy thông tin người dùng."

        # Nếu assertion đúng (đăng nhập thành công), in ra thông báo
        print("Đăng nhập thành công - customer")

    except Exception as e:
        # Nếu không tìm thấy info-placeholder, kiểm tra sự hiện diện của các nút "Log in" và "Sign up" (đăng nhập không thành công)
        login_button = chrome_driver.find_element(By.CSS_SELECTOR,
                                                  "div.left-button-login input[type='button'][value='Log in']")
        sign_up_button = chrome_driver.find_element(By.CSS_SELECTOR,
                                                    "div.right-button-register input[type='button'][value='Sign up']")
        assert login_button.is_displayed() and sign_up_button.is_displayed(), "Đăng nhập không thành công: Không tìm thấy nút 'Log in' hoặc 'Sign up'."

        # In ra thông báo khi đăng nhập thất bại (bạn có thể thay thế nếu cần)
        print("Đăng nhập thất bại - customer")


def login_success_superAdmin(chrome_driver):
    # Nhấn nút "Log in"
    login_button = chrome_driver.find_element(By.CSS_SELECTOR, "div.left-button-login input[type='button'][value='Log in']")
    login_button.click()

    # Chờ cho popup hoặc form login xuất hiện
    time.sleep(2)

    # Điền username
    username_field = chrome_driver.find_element(By.ID, "username-field")
    username_field.send_keys("lahieuphong_superAdmin")
    time.sleep(1)

    # Điền password
    password_field = chrome_driver.find_element(By.ID, "password-field")
    password_field.send_keys("Tatooboys123@")
    time.sleep(1)

    # Nhấn nút Login
    submit_button = chrome_driver.find_element(By.CSS_SELECTOR, "div.submit input[type='button'][value='Login']")
    submit_button.click()

    # Chờ để đảm bảo đăng nhập đã hoàn tất
    time.sleep(5)

    # Kiểm tra xem nếu đăng nhập thành công (kiểm tra phần tử có class "info-placeholder" cho thấy người dùng đã đăng nhập)
    try:
        # Kiểm tra phần tử thông tin người dùng (đăng nhập thành công)
        info_placeholder = chrome_driver.find_element(By.CSS_SELECTOR, "div.info-placeholder")
        assert info_placeholder.is_displayed(), "\nĐăng nhập không thành công: Không tìm thấy thông tin người dùng."

        # Nếu assertion đúng (đăng nhập thành công), in ra thông báo
        print("Đăng nhập thành công - superAdmin")

    except Exception as e:
        # Nếu không tìm thấy info-placeholder, kiểm tra sự hiện diện của các nút "Log in" và "Sign up" (đăng nhập không thành công)
        login_button = chrome_driver.find_element(By.CSS_SELECTOR,
                                                  "div.left-button-login input[type='button'][value='Log in']")
        sign_up_button = chrome_driver.find_element(By.CSS_SELECTOR,
                                                    "div.right-button-register input[type='button'][value='Sign up']")
        assert login_button.is_displayed() and sign_up_button.is_displayed(), "Đăng nhập không thành công: Không tìm thấy nút 'Log in' hoặc 'Sign up'."

        # In ra thông báo khi đăng nhập thất bại (bạn có thể thay thế nếu cần)
        print("Đăng nhập thất bại - superAdmin")