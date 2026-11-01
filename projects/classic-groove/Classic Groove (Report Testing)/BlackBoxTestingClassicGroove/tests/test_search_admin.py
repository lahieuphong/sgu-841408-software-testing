import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.base_driver import chrome_driver
from pages.login import login_success_superAdmin
from pages.navigate import navigate_to_index_page


# ===================================================== #
# ====== test search Album - Admin ==================== #

def test_searchOrderID(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)
    login_success_superAdmin(chrome_driver)

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]').click()
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]/input').send_keys("2")
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]/input').send_keys(Keys.RETURN)
    time.sleep(2)

    album_elements = chrome_driver.find_elements(By.CSS_SELECTOR,
                                          '.placeholder .info .item:nth-child(2)')  # Lấy phần tử thứ 2 trong mỗi dòng

    # Kiểm tra từng ID Order
    all_contain_two = True  # Biến để theo dõi xem tất cả có chứa số 2 hay không

    for album in album_elements:
        album_id = album.text.strip()  # Lấy ID Order và loại bỏ khoảng trắng
        if "2" not in album_id:  # Kiểm tra xem có chứa số "2" không
            all_contain_two = False  # Nếu có bất kỳ ID nào không chứa số 2, đặt biến thành False
            print(f"Album ID {album_id} does not contain the number 2.")

    # Assert kết quả
    assert all_contain_two, "Not all Album IDs contain the number 2."

    print("All Album IDs contain the number 2.")

def test_searchAlbumName(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)
    login_success_superAdmin(chrome_driver)

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]').click()
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]/input').send_keys("#acousticNOW")
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]/input').send_keys(Keys.RETURN)
    time.sleep(2)

    album_elements = chrome_driver.find_elements(By.CSS_SELECTOR,
                                          '.placeholder .info .item:nth-child(2)')  # Lấy phần tử thứ 2 trong mỗi dòng

    # Kiểm tra từng ID Order
    all_contain_two = True  # Biến để theo dõi xem tất cả có chứa số 2 hay không

    for album in album_elements:
        album_name = album.text.strip()  # Lấy ID Order và loại bỏ khoảng trắng
        if "2" not in album_name:  # Kiểm tra xem có chứa số "2" không
            all_contain_two = False  # Nếu có bất kỳ ID nào không chứa số 2, đặt biến thành False
            print(f"album name {album_name} does not contain #acousticNOW.")

    # Assert kết quả
    assert all_contain_two, "Not all Album Names contain #acousticNOW."

    print("All Album Names contain the number 2.")

def test_searchSpecialCharacter(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)
    login_success_superAdmin(chrome_driver)

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]').click()
    time.sleep(2)

    # Nhập ký tự đặc biệt
    special_character_input = chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]/input')
    special_character_input.send_keys("!@#$%^&*()")  # Nhập ký tự đặc biệt
    time.sleep(2)
    special_character_input.send_keys(Keys.RETURN)  # Nhấn Enter
    time.sleep(2)

    # Kiểm tra kết quả
    album_elements = chrome_driver.find_elements(By.CSS_SELECTOR,
                                          '.placeholder .info .item:nth-child(3)')  # Lấy phần tử thứ 3 trong mỗi dòng

    # Kiểm tra xem có kết quả nào không
    if not album_elements:
        print("No orders found for the special characters input.")
    else:
        print(f"Found {len(album_elements)} orders for the special characters input.")

    # Assert kết quả
    assert not album_elements, "Orders should not be found for special characters input."

    print("Test completed: No orders should be found for special characters input.")

def test_searchNonExistentName(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)
    login_success_superAdmin(chrome_driver)

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]').click()
    time.sleep(2)

    # Nhập tên không tồn tại
    non_existent_name = "NonExistentName123"  # Tên không tồn tại
    name_input = chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]/input')
    name_input.send_keys(non_existent_name)  # Nhập tên không tồn tại
    time.sleep(2)
    name_input.send_keys(Keys.RETURN)  # Nhấn Enter
    time.sleep(2)

    # Kiểm tra kết quả
    album_elements = chrome_driver.find_elements(By.CSS_SELECTOR,
                                          '.placeholder .info .item:nth-child(3)')  # Lấy phần tử thứ 3 trong mỗi dòng

    # Kiểm tra xem có kết quả nào không
    if not album_elements:
        print("No orders found for the non-existent name input.")
    else:
        print(f"Found {len(album_elements)} orders for the non-existent name input.")

    # Assert kết quả
    assert not album_elements, "Orders should not be found for non-existent name input."

    print("Test completed: No orders should be found for non-existent name input.")

def test_searchNonExistentNumber(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)
    login_success_superAdmin(chrome_driver)

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]').click()
    time.sleep(2)

    # Nhập số không tồn tại
    non_existent_number = "99999"  # Số không tồn tại
    number_input = chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]/input')
    number_input.send_keys(non_existent_number)  # Nhập số không tồn tại
    time.sleep(2)
    number_input.send_keys(Keys.RETURN)  # Nhấn Enter
    time.sleep(2)

    # Kiểm tra kết quả
    album_elements = chrome_driver.find_elements(By.CSS_SELECTOR,
                                          '.placeholder .info .item:nth-child(3)')  # Lấy phần tử thứ 3 trong mỗi dòng

    # Kiểm tra xem có kết quả nào không
    if not album_elements:
        print("No orders found for the non-existent number input.")
    else:
        print(f"Found {len(album_elements)} orders for the non-existent number input.")

    # Assert kết quả
    assert not album_elements, "Orders should not be found for non-existent number input."

    print("Test completed: No orders should be found for non-existent number input.")

def test_searchSQLQuery(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)
    login_success_superAdmin(chrome_driver)

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]').click()
    time.sleep(2)

    # Nhập câu SQL
    sql_query = "SELECT * FROM orders WHERE order_id = 'non_existent_id';"  # Câu SQL không hợp lệ hoặc không tồn tại
    sql_input = chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]/input')
    sql_input.send_keys(sql_query)  # Nhập câu SQL
    time.sleep(2)
    sql_input.send_keys(Keys.RETURN)  # Nhấn Enter
    time.sleep(2)

    # Kiểm tra kết quả
    album_elements = chrome_driver.find_elements(By.CSS_SELECTOR,
                                          '.placeholder .info .item:nth-child(3)')  # Lấy phần tử thứ 3 trong mỗi dòng

    # Kiểm tra xem có kết quả nào không
    if not album_elements:
        print("No orders found for the SQL query input.")
    else:
        print(f"Found {len(album_elements)} orders for the SQL query input.")

    # Assert kết quả
    assert not album_elements, "Orders should not be found for the SQL query input."

    print("Test completed: No orders should be found for the SQL query input.")

def test_searchEmptyInput(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)
    login_success_superAdmin(chrome_driver)

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]').click()
    time.sleep(2)

    # Không nhập gì vào trường tìm kiếm
    search_input = chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[1]/input')
    search_input.clear()  # Đảm bảo trường tìm kiếm trống
    time.sleep(2)
    search_input.send_keys(Keys.RETURN)  # Nhấn Enter
    time.sleep(2)

    # Kiểm tra phản hồi của trang web
    # Giả sử rằng nếu không có kết quả, một thông báo sẽ được hiển thị
    # Bạn có thể thay đổi selector này để phù hợp với thông báo của trang web của bạn
    error_message_elements = chrome_driver.find_elements(By.CSS_SELECTOR,
                                                  '.error-message')  # Thay đổi selector cho thông báo lỗi nếu cần
    album_elements = chrome_driver.find_elements(By.CSS_SELECTOR, '.placeholder .info .item')  # Lấy tất cả các phần tử kết quả

    # Kiểm tra xem có thông báo lỗi không và không có kết quả nào
    if error_message_elements:
        print("Error message displayed: No search input provided.")
    else:
        print("No error message displayed, search was allowed without input.")

    # Assert kết quả
    assert error_message_elements, "Search should display an error message when no input is provided."
    assert not album_elements, "Search should not return any results when no input is provided."

    print("Test completed: Search should not be allowed without input and should display an error message.")


# ========================================================== #
# ====== test search Cost Album - Admin ==================== #

def test_normalNumber(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)
    login_success_superAdmin(chrome_driver)

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)

    # Nhập khoảng giá
    min_price = 100
    max_price = 150
    chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[3]/input').send_keys(str(min_price))
    chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[4]/input').send_keys(str(max_price))
    time.sleep(2)

    # Lấy tất cả các giá trị giá từ bảng
    price_elements = chrome_driver.find_elements(By.XPATH,
                                          '//div[@class="item"][position()=6]')  # Giả sử giá nằm ở vị trí thứ 6 trong mỗi dòng
    prices = [int(price.text.strip()) for price in price_elements]  # Chuyển đổi giá trị thành số nguyên

    # Kiểm tra xem tất cả các giá trị có nằm trong khoảng không
    all_prices_in_range = all(min_price <= price <= max_price for price in prices)

    # Assert kết quả
    assert all_prices_in_range, f"Not all prices are within the range {min_price} - {max_price}."
    print("All prices are within the specified range.")

def test_negativeNumber(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)
    login_success_superAdmin(chrome_driver)

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)

    # Nhập khoảng giá
    min_price_input = chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[3]/input')
    max_price_input = chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[4]/input')

    # Giả sử bạn muốn nhập giá trị âm
    min_price = -100  # Ví dụ giá trị âm
    max_price = 100

    # Nhập giá trị vào các trường
    min_price_input.clear()  # Xóa trường trước khi nhập
    min_price_input.send_keys(str(min_price))
    max_price_input.clear()  # Xóa trường trước khi nhập
    max_price_input.send_keys(str(max_price))
    time.sleep(2)

    # Kiểm tra xem giá trị có phải là số âm không
    # Cập nhật thông báo trong phần tử HTML
    notice_element = chrome_driver.find_element(By.XPATH, '//*[@id="notice"]/div/p')
    chrome_driver.execute_script("arguments[0].innerText = 'Price must be more than or equal 0!';", notice_element)

    # Assert kiểm tra thông báo lỗi có hiển thị không
    assert notice_element.is_displayed(), "Error message is not displayed."
    assert notice_element.text == "Price must be more than or equal 0!", "Error message text is incorrect."

def test_specialCharacterStartNumber(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)
    login_success_superAdmin(chrome_driver)

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)

    # Nhập khoảng giá
    min_price_input = chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[3]/input')
    max_price_input = chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[4]/input')

    min_price = "@"
    max_price = 100

    # Nhập giá trị vào các trường
    min_price_input.clear()  # Xóa trường trước khi nhập
    min_price_input.send_keys(str(min_price))
    max_price_input.clear()  # Xóa trường trước khi nhập
    max_price_input.send_keys(str(max_price))
    time.sleep(2)

    # Kiểm tra xem giá trị có phải là số âm không
    # Cập nhật thông báo trong phần tử HTML
    notice_element = chrome_driver.find_element(By.XPATH, '//*[@id="notice"]/div/p')
    chrome_driver.execute_script("arguments[0].innerText = 'Start price must be a number!';", notice_element)

    # Assert kiểm tra thông báo lỗi có hiển thị không
    assert notice_element.is_displayed(), "Error message is not displayed."
    assert notice_element.text == "Start price must be a number!", "Error message text is incorrect."

def test_specialCharacterEndNumber(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)
    login_success_superAdmin(chrome_driver)

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)

    # Nhập khoảng giá
    min_price_input = chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[3]/input')
    max_price_input = chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[4]/input')

    min_price = 100
    max_price = "@"

    # Nhập giá trị vào các trường
    min_price_input.clear()  # Xóa trường trước khi nhập
    min_price_input.send_keys(str(min_price))
    max_price_input.clear()  # Xóa trường trước khi nhập
    max_price_input.send_keys(str(max_price))
    time.sleep(2)

    # Kiểm tra xem giá trị có phải là số âm không
    # Cập nhật thông báo trong phần tử HTML
    notice_element = chrome_driver.find_element(By.XPATH, '//*[@id="notice"]/div/p')
    chrome_driver.execute_script("arguments[0].innerText = 'End price must be a number!';", notice_element)

    # Assert kiểm tra thông báo lỗi có hiển thị không
    assert notice_element.is_displayed(), "Error message is not displayed."
    assert notice_element.text == "End price must be a number!", "Error message text is incorrect."