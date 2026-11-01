import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

SGU_USERNAME = os.environ.get("SGU_USERNAME", "")
SGU_PASSWORD = os.environ.get("SGU_PASSWORD", "")


# Hàm xóa các trường nhập liệu
def clear_input_fields(browser):
    username_field = browser.find_element(By.NAME, "username")
    password_field = browser.find_element(By.NAME, "password")
    username_field.clear()
    password_field.clear()


# Hàm thực hiện đăng nhập và trả về kết quả thành công hoặc thất bại
def perform_login(browser, username, password):
    clear_input_fields(browser)

    username_field = browser.find_element(By.NAME, "username")
    password_field = browser.find_element(By.NAME, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = browser.find_element(By.XPATH, "/html/body/app-root/div/div/div/div[1]/div/div/div[2]/app-right/app-login/div/div[2]/div/div[4]/button")
    login_button.click()

    time.sleep(2)

    # Kiểm tra điều kiện sau khi đăng nhập để xác nhận thành công hoặc thất bại
    try:
        WebDriverWait(browser, 5).until(EC.url_contains("#/home"))
        return True  # Pass
    except:
        return False  # Fail


# Test cases
# ==========
def validate_with_username_and_not_password(browser):
    return perform_login(browser, SGU_USERNAME, "")

def validate_with_password_and_not_username(browser):
    return perform_login(browser, "", SGU_PASSWORD)
# ==========

def validate_with_username_incorrect_and_password_correct(browser):
    return perform_login(browser, SGU_USERNAME + "_invalid", SGU_PASSWORD)

def validate_with_username_correct_and_password_incorrect(browser):
    return perform_login(browser, SGU_USERNAME, SGU_PASSWORD + "_invalid")
# ==========

def validate_with_username_html_and_password_correct(browser):
    return perform_login(browser, f"<b>{SGU_USERNAME}</b>", SGU_PASSWORD)
# ==========

def validate_with_username_correct_and_password_less(browser):
    return perform_login(browser, SGU_USERNAME, "short")
# ==========

def validate_with_username_correct_and_password_correct(browser):
    return perform_login(browser, SGU_USERNAME, SGU_PASSWORD)
# ==========


def click_button(browser):
    browser.refresh() # Refresh lại trang
    try:
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/div/div/div[1]/div/div/div[2]/app-right/app-login/div/div[2]/div/div[4]/button"))
        )
        time.sleep(2)
    except Exception as e:
        print(f"Error while waiting for button: {e}")


if __name__ == '__main__':
    if not SGU_USERNAME or not SGU_PASSWORD:
        raise SystemExit("Set SGU_USERNAME and SGU_PASSWORD before running this script.")
    chrome_options = Options()
    browser = webdriver.Chrome(options=chrome_options)

    # Open the target URL
    browser.get("https://thongtindaotao.sgu.edu.vn/#/home")
    time.sleep(2)

    results = [["Name", "Description", "Result"]]

    # Run each test case and store the results
    test_cases = [
        ("Case 1", "validate_with_username_and_not_password", validate_with_username_and_not_password),
        ("Case 2", "validate_with_password_and_not_username", validate_with_password_and_not_username),
        ("Case 3", "validate_with_username_incorrect_and_password_correct", validate_with_username_incorrect_and_password_correct),
        ("Case 4", "validate_with_username_correct_and_password_incorrect", validate_with_username_correct_and_password_incorrect),
        ("Case 5", "validate_with_username_html_and_password_correct", validate_with_username_html_and_password_correct),
        ("Case 6", "validate_with_username_correct_and_password_less", validate_with_username_correct_and_password_less),
        ("Case 7", "validate_with_username_correct_and_password_correct", validate_with_username_correct_and_password_correct),
    ]

    for case_name, description, test_func in test_cases:
        print(f"Running {case_name}: {description}...")
        click_button(browser)
        result = test_func(browser)
        results.append([case_name, description, "Pass" if result else "Fail"])
        print(f"{case_name} result: {'Pass' if result else 'Fail'}\n")


    browser.quit()