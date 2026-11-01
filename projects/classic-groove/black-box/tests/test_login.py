import time
from selenium.webdriver.common.by import By
from utils.base_driver import chrome_driver
from pages.navigate import navigate_to_index_page
from pages.login_with_roles import loginRoleInAdmin, wait_for_clickable_element, click_element


# ============================================ #
# ====== Login with Roles ==================== #

def test_loginAdmin(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(chrome_driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(chrome_driver, login)
    time.sleep(2)

    # Perform login
    chrome_driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong_superAdmin")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Verify login success
    check_login = chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/h3').text
    assert "Hello" in check_login, "Đăng nhập không thành công"

    # Verify admin privileges
    expected_values = {
        "statistic": "statistic",
        "album": "album",
        "order": "order",
        "account": "account",
        "supply": "supply",
        "structure": "structure",
        "permission": "permission"
    }

    for field, expected_value in expected_values.items():
        element = chrome_driver.find_element(By.XPATH,
                                      f'//*[@id="header"]/div/div[1]/div[2]/div[{list(expected_values.keys()).index(field) + 1}]/div[2]')
        actual_value = element.text.strip().lower()
        assert actual_value == expected_value, f"Lỗi: {field} không khớp, giá trị thực tế: {actual_value} - Không phải admin"

    loginRoleInAdmin(chrome_driver, "lahieuphong_superAdmin", "superAdmin")

def test_loginCustomer(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(chrome_driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(chrome_driver, login)
    time.sleep(2)

    # Perform login
    chrome_driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong_customer")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Verify login success
    check_login = chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/h3').text
    assert "Hello" in check_login, "Đăng nhập không thành công"

    expected_values = {
        "home": "home",
        "favorites": "favorites",
        "cart": "cart",
        "account": "account",
    }

    for field, expected_value in expected_values.items():
        element = chrome_driver.find_element(By.XPATH,
                                      f'//*[@id="header"]/div/div[1]/div[2]/div[{list(expected_values.keys()).index(field) + 1}]/div[2]')
        actual_value = element.text.strip().lower()
        assert actual_value == expected_value, f"Lỗi: {field} không khớp, giá trị thực tế: {actual_value} - Không phải customer"

    loginRoleInAdmin(chrome_driver, "lahieuphong_customer", "customer")

def test_loginSeller(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(chrome_driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(chrome_driver, login)
    time.sleep(2)

    # Perform login
    chrome_driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong_seller")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Verify login success
    check_login = chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/h3').text
    assert "Hello" in check_login, "Đăng nhập không thành công"

    # Expected values for the "Seller" role
    expected_values = {
        "album": "album",
        "order": "order",
    }

    # Loop through the expected values and check if they match
    for field, expected_value in expected_values.items():
        element = chrome_driver.find_element(By.XPATH,
                                      f'//*[@id="header"]/div/div[1]/div[2]/div[{list(expected_values.keys()).index(field) + 1}]/div[2]')
        actual_value = element.text.strip().lower()
        assert actual_value == expected_value, f"Lỗi: {field} không khớp, giá trị thực tế: {actual_value} - Không phải Seller"

    # Call the login role verification function
    loginRoleInAdmin(chrome_driver, "lahieuphong_seller", "seller")

def test_loginDesign(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(chrome_driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(chrome_driver, login)
    time.sleep(2)

    # Perform login
    chrome_driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong_design")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Verify login success
    check_login = chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/h3').text
    assert "Hello" in check_login, "Đăng nhập không thành công"

    expected_values = {
        "structure": "structure",
    }

    for field, expected_value in expected_values.items():
        element = chrome_driver.find_element(By.XPATH,
                                      f'//*[@id="header"]/div/div[1]/div[2]/div[{list(expected_values.keys()).index(field) + 1}]/div[2]')
        actual_value = element.text.strip().lower()
        assert actual_value == expected_value, f"Lỗi: {field} không khớp, giá trị thực tế: {actual_value} - Không phải Design"

    loginRoleInAdmin(chrome_driver, "lahieuphong_design", "design")

def test_loginAnalyst(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(chrome_driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(chrome_driver, login)
    time.sleep(2)

    # Perform login
    chrome_driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong_analyst")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Verify login success
    check_login = chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/h3').text
    assert "Hello" in check_login, "Đăng nhập không thành công"

    expected_values = {
        "statistic": "statistic",
        "order": "order",
        "supply": "supply"
    }

    for field, expected_value in expected_values.items():
        element = chrome_driver.find_element(By.XPATH,
                                      f'//*[@id="header"]/div/div[1]/div[2]/div[{list(expected_values.keys()).index(field) + 1}]/div[2]')
        actual_value = element.text.strip().lower()
        assert actual_value == expected_value, f"Lỗi: {field} không khớp, giá trị thực tế: {actual_value} - Không phải Analyst"

    loginRoleInAdmin(chrome_driver, "lahieuphong_analyst", "analyst")

def test_loginStocker(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(chrome_driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(chrome_driver, login)
    time.sleep(2)

    # Perform login
    chrome_driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong_stocker")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Verify login success
    check_login = chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/h3').text
    assert "Hello" in check_login, "Đăng nhập không thành công"

    expected_values = {
        "album": "album",
        "supply": "supply"
    }

    for field, expected_value in expected_values.items():
        element = chrome_driver.find_element(By.XPATH,
                                      f'//*[@id="header"]/div/div[1]/div[2]/div[{list(expected_values.keys()).index(field) + 1}]/div[2]')
        actual_value = element.text.strip().lower()
        assert actual_value == expected_value, f"Lỗi: {field} không khớp, giá trị thực tế: {actual_value} - Không phải Stocker"

    loginRoleInAdmin(chrome_driver, "lahieuphong_stocker", "stocker")

# ============================================ #
# ============================================ #


def test_loginEmptyUserName(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(chrome_driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(chrome_driver, login)
    time.sleep(2)

    # Perform login with empty fields
    chrome_driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Check for the notice
    notice = chrome_driver.find_element(By.XPATH,
                                 '//p[@class="cart-removing" and contains(text(), "Please, enter username!")]').text
    expected_notice = "Please, enter username!"
    assert notice == expected_notice, f"Expected notice: '{expected_notice}', but got: '{notice}'"

def test_loginEmptyPasswordName(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(chrome_driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(chrome_driver, login)
    time.sleep(2)

    # Perform login with empty fields
    chrome_driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong_customer")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Check for the notice
    notice = chrome_driver.find_element(By.XPATH,
                                 '//p[@class="cart-removing" and contains(text(), "Please, enter your password!")]').text
    expected_notice = "Please, enter your password!"
    assert notice == expected_notice, f"Expected notice: '{expected_notice}', but got: '{notice}'"

def test_loginAccountNoExist(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(chrome_driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(chrome_driver, login)
    time.sleep(2)

    # Perform login with non-existing account
    chrome_driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("AAAAAAAAAAAAAA")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Check for the notice
    notice = chrome_driver.find_element(By.XPATH,
                                 '//p[@class="cart-removing" and contains(text(), "Account does not exist!")]').text
    expected_notice = "Account does not exist!"
    assert notice == expected_notice, f"Expected notice: '{expected_notice}', but got: '{notice}'"