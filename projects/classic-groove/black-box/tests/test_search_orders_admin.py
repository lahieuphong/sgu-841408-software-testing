import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


# Fixture to initialize the WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Ensure ChromeDriver is correctly installed and in PATH
    driver.maximize_window()
    yield driver
    driver.quit()


# Helper function for waiting for clickable elements
def wait_for_clickable_element(driver, locator, timeout=10):
    """Wait for an element to be clickable and return it."""
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable(locator))


# Helper function for clicking an element
def click_element(driver, element):
    """Click an element safely."""
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()


# Test case for admin login and validation
def test_searchOrderID(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove/index.php")
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong_superAdmin")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]/input').send_keys("2")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]/input').send_keys(Keys.RETURN)
    time.sleep(2)

    order_elements = driver.find_elements(By.CSS_SELECTOR,
                                          '.placeholder .info .item:nth-child(2)')  # Lấy phần tử thứ 2 trong mỗi dòng

    # Kiểm tra từng ID Order
    all_contain_two = True  # Biến để theo dõi xem tất cả có chứa số 2 hay không

    for order in order_elements:
        order_id = order.text.strip()  # Lấy ID Order và loại bỏ khoảng trắng
        if "2" not in order_id:  # Kiểm tra xem có chứa số "2" không
            all_contain_two = False  # Nếu có bất kỳ ID nào không chứa số 2, đặt biến thành False
            print(f"Order ID {order_id} does not contain the number 2.")

    # Assert kết quả
    assert all_contain_two, "Not all Order IDs contain the number 2."

    print("All Order IDs contain the number 2.")


def test_searchAccountID(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove/index.php")
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong_superAdmin")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]/input').send_keys("lahieuphong")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]/input').send_keys(Keys.RETURN)
    time.sleep(2)

    order_elements = driver.find_elements(By.CSS_SELECTOR,
                                          '.placeholder .info .item:nth-child(3)')  # Lấy phần tử thứ 2 trong mỗi dòng

    # Kiểm tra từng ID Order
    all_contain_two = True  # Biến để theo dõi xem tất cả có chứa số 2 hay không

    for order in order_elements:
        order_id = order.text.strip()  # Lấy ID Order và loại bỏ khoảng trắng
        if "lahieuphong" not in order_id:  # Kiểm tra xem có chứa số "2" không
            all_contain_two = False  # Nếu có bất kỳ ID nào không chứa số 2, đặt biến thành False
            print(f"Account ID {order_id} does not contain lahieuphong")

    # Assert kết quả
    assert all_contain_two, "Not all Account IDs contain leduyquan account."

    print("All Account IDs contain lahieuphong account.")


def test_searchSpecialCharacter(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove/index.php")
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong_superAdmin")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]').click()
    time.sleep(2)

    # Nhập ký tự đặc biệt
    special_character_input = driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]/input')
    special_character_input.send_keys("!@#$%^&*()")  # Nhập ký tự đặc biệt
    time.sleep(2)
    special_character_input.send_keys(Keys.RETURN)  # Nhấn Enter
    time.sleep(2)

    # Kiểm tra kết quả
    order_elements = driver.find_elements(By.CSS_SELECTOR,
                                          '.placeholder .info .item:nth-child(3)')  # Lấy phần tử thứ 3 trong mỗi dòng

    # Kiểm tra xem có kết quả nào không
    if not order_elements:
        print("No orders found for the special characters input.")
    else:
        print(f"Found {len(order_elements)} orders for the special characters input.")

    # Assert kết quả
    assert not order_elements, "Orders should not be found for special characters input."

    print("Test completed: No orders should be found for special characters input.")


def test_searchNonExistentName(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove/index.php")
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong_superAdmin")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]').click()
    time.sleep(2)

    # Nhập tên không tồn tại
    non_existent_name = "NonExistentName123"  # Tên không tồn tại
    name_input = driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]/input')
    name_input.send_keys(non_existent_name)  # Nhập tên không tồn tại
    time.sleep(2)
    name_input.send_keys(Keys.RETURN)  # Nhấn Enter
    time.sleep(2)

    # Kiểm tra kết quả
    order_elements = driver.find_elements(By.CSS_SELECTOR,
                                          '.placeholder .info .item:nth-child(3)')  # Lấy phần tử thứ 3 trong mỗi dòng

    # Kiểm tra xem có kết quả nào không
    if not order_elements:
        print("No orders found for the non-existent name input.")
    else:
        print(f"Found {len(order_elements)} orders for the non-existent name input.")

    # Assert kết quả
    assert not order_elements, "Orders should not be found for non-existent name input."

    print("Test completed: No orders should be found for non-existent name input.")


def test_searchNonExistentNumber(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove/index.php")
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong_superAdmin")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]').click()
    time.sleep(2)

    # Nhập số không tồn tại
    non_existent_number = "99999"  # Số không tồn tại
    number_input = driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]/input')
    number_input.send_keys(non_existent_number)  # Nhập số không tồn tại
    time.sleep(2)
    number_input.send_keys(Keys.RETURN)  # Nhấn Enter
    time.sleep(2)

    # Kiểm tra kết quả
    order_elements = driver.find_elements(By.CSS_SELECTOR,
                                          '.placeholder .info .item:nth-child(3)')  # Lấy phần tử thứ 3 trong mỗi dòng

    # Kiểm tra xem có kết quả nào không
    if not order_elements:
        print("No orders found for the non-existent number input.")
    else:
        print(f"Found {len(order_elements)} orders for the non-existent number input.")

    # Assert kết quả
    assert not order_elements, "Orders should not be found for non-existent number input."

    print("Test completed: No orders should be found for non-existent number input.")


def test_searchSQLQuery(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove/index.php")
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong_superAdmin")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]').click()
    time.sleep(2)

    # Nhập câu SQL
    sql_query = "SELECT * FROM hoadon;"  # Câu SQL không hợp lệ hoặc không tồn tại
    sql_input = driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]/input')
    sql_input.send_keys(sql_query)  # Nhập câu SQL
    time.sleep(2)
    sql_input.send_keys(Keys.RETURN)  # Nhấn Enter
    time.sleep(2)

    # Kiểm tra kết quả
    order_elements = driver.find_elements(By.CSS_SELECTOR,
                                          '.placeholder .info .item:nth-child(3)')  # Lấy phần tử thứ 3 trong mỗi dòng

    # Kiểm tra xem có kết quả nào không
    if not order_elements:
        print("No orders found for the SQL query input.")
    else:
        print(f"Found {len(order_elements)} orders for the SQL query input.")

    # Assert kết quả
    assert not order_elements, "Orders should not be found for the SQL query input."

    print("Test completed: No orders should be found for the SQL query input.")


def test_searchEmptyInput(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove/index.php")
    time.sleep(2)

    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong_superAdmin")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]').click()
    time.sleep(2)

    # Không nhập gì vào trường tìm kiếm
    search_input = driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[1]/input')
    search_input.clear()  # Đảm bảo trường tìm kiếm trống
    time.sleep(2)
    search_input.send_keys(Keys.RETURN)  # Nhấn Enter
    time.sleep(2)

    # Kiểm tra phản hồi của trang web
    # Giả sử rằng nếu không có kết quả, một thông báo sẽ được hiển thị
    # Bạn có thể thay đổi selector này để phù hợp với thông báo của trang web của bạn
    error_message_elements = driver.find_elements(By.CSS_SELECTOR,
                                                  '.error-message')  # Thay đổi selector cho thông báo lỗi nếu cần
    order_elements = driver.find_elements(By.CSS_SELECTOR, '.placeholder .info .item')  # Lấy tất cả các phần tử kết quả

    # Kiểm tra xem có thông báo lỗi không và không có kết quả nào
    if error_message_elements:
        print("Error message displayed: No search input provided.")
    else:
        print("No error message displayed, search was allowed without input.")

    # Assert kết quả
    assert error_message_elements, "Search should display an error message when no input is provided."
    assert not order_elements, "Search should not return any results when no input is provided."

    print("Test completed: Search should not be allowed without input and should display an error message.")