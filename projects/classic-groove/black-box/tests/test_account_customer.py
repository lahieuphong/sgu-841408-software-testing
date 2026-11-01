import time
from selenium.webdriver.common.by import By
from utils.base_driver import chrome_driver
from pages.login import login_success_customer
from pages.navigate import navigate_to_index_page


# bug: không sửa được trường username (customer)
def test_update_user_info_with_ui_issue(chrome_driver):
    # Thực hiện hành động thêm vào giỏ hàng và các bước khác
    print(f"\n")
    print(f"-" * 40)
    navigate_to_index_page(chrome_driver)  # Điều hướng đến trang chủ
    login_success_customer(chrome_driver)  # Đăng nhập thành công với khách hàng
    print(f"-" * 40)

    # Nhấn vào biểu tượng người dùng để xem đơn hàng
    user_icon = chrome_driver.find_element(By.CSS_SELECTOR, "i.fa-solid.fa-user")
    user_icon.click()
    time.sleep(1)  # Chờ form tải

    # Tìm và nhập thông tin vào các ô nhập
    input_fields = [
        {"id": "txtHoTen", "value": "La Hiểu Phong (customer)"},
        {"id": "txtSDT", "value": "0326526898"},  # Cập nhật số điện thoại mới
        {"id": "txtAddress", "value": "430/28/5 TA28 Street, District 12, HCM"},  # Cập nhật địa chỉ mới
        {"id": "txtEmail", "value": "hieuphong144@gmail.com"}  # Cập nhật email mới
    ]

    for field in input_fields:
        input_element = chrome_driver.find_element(By.ID, field["id"])

        # Đảm bảo ô nhập đã sẵn sàng trước khi nhập
        chrome_driver.implicitly_wait(5)  # Chờ trong 5 giây

        # Clear nội dung cũ và nhập lại
        input_element.clear()
        input_element.send_keys(field["value"])
        time.sleep(1)  # Chờ sau khi nhập liệu

    # Kiểm tra ô nhập disabled và mong đợi giá trị là 'lahieuphong_customer'
    disabled_input = chrome_driver.find_element(By.CSS_SELECTOR, "input[value='lahieuphong_customer']")

    # Lấy giá trị thực tế của ô nhập
    actual_value = disabled_input.get_attribute("value")

    # Mong đợi giá trị là 'lahieuphong_customer', nhưng thực tế lại là 'customer_lahieuphong'
    expected_value = "lahieuphong"

    # Assert fail condition (test will fail if actual value is different from expected)
    assert actual_value == expected_value, f"Test failed: Expected '{expected_value}', but got '{actual_value}'."

    # Nhấn nút "Save change"
    save_button = chrome_driver.find_element(By.CSS_SELECTOR, ".button-placeholder.btnSave")
    save_button.click()
    time.sleep(2)  # Chờ sau khi nhấn lưu

# bug (pass): lỗi giao diện khi nhấn nút hủy đơn (customer)
def test_cancel_order_with_ui_issue(chrome_driver):
    # Thực hiện hành động thêm vào giỏ hàng và các bước khác
    print(f"\n")
    print(f"-" * 40)
    navigate_to_index_page(chrome_driver)  # Điều hướng đến trang chủ
    login_success_customer(chrome_driver)  # Đăng nhập thành công với khách hàng
    print(f"-" * 40)

    # Nhấn vào biểu tượng người dùng để xem đơn hàng
    user_icon = chrome_driver.find_element(By.CSS_SELECTOR, "i.fa-solid.fa-user")
    user_icon.click()
    time.sleep(1)  # Chờ form tải

    # Cuộn xuống để tìm đơn hàng
    cancel_button_found = False  # Biến flag theo dõi xem nút hủy đơn có được tìm thấy không
    for _ in range(5):  # Thử cuộn 5 lần
        try:
            # Tìm nút cancel bằng CSS selector
            cancel_button = chrome_driver.find_element(By.CSS_SELECTOR, ".cancel-button")
            cancel_button.click()  # Nhấn nút hủy đơn
            print(f"Cancel your Order")  # In thông báo hủy đơn hàng
            print(f"-" * 40)
            cancel_button_found = True
            break  # Thoát vòng lặp khi đã hủy đơn
        except Exception as e:
            # Nếu không tìm thấy nút cancel, cuộn xuống và thử lại
            chrome_driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)  # Đợi một chút cho các đơn hàng mới tải lên
            print(f"Error: {e}. Scrolling down to try again.")  # In lỗi và tiếp tục cuộn

    if not cancel_button_found:
        print("Cancel button not found after scrolling. Exiting the test.")  # Thông báo không tìm thấy nút cancel sau khi cuộn
        return  # Dừng kiểm thử nếu không tìm thấy nút cancel

    time.sleep(2)

    # Tìm tất cả các dòng tài khoản trong danh sách
    account_rows = chrome_driver.find_elements(By.CSS_SELECTOR, ".list .placeholder")

    for row in account_rows:
        # Lấy thông tin chi tiết tài khoản từ mỗi dòng
        account_no = row.find_element(By.CSS_SELECTOR, ".item:nth-child(1)").text.strip()
        username = row.find_element(By.CSS_SELECTOR, ".item:nth-child(2)").text.strip()
        account_name = row.find_element(By.CSS_SELECTOR, ".item:nth-child(3)").text.strip()
        phone_number = row.find_element(By.CSS_SELECTOR, ".item:nth-child(4)").text.strip()
        role = row.find_element(By.CSS_SELECTOR, ".item:nth-child(5)").text.strip()
        status = row.find_element(By.CSS_SELECTOR, ".item:nth-child(6)").text.strip()

        # In ra thông tin tài khoản đã trích xuất
        print(f"Account No: {account_no}")
        print(f"Username: {username}")
        print(f"Account Name: {account_name}")
        print(f"Phone Number: {phone_number}")
        print(f"Role: {role}")
        print(f"Status: {status}")
        print("-" * 50)  # In dấu phân cách giữa các tài khoản