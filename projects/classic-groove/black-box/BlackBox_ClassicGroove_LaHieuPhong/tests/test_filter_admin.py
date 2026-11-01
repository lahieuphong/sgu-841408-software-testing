import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.base_driver import chrome_driver
from pages.login import login_success_superAdmin
from pages.navigate import navigate_to_index_page


@pytest.mark.parametrize("status_filter", ["Blues", "Acoustic", "Classical", "Country", "Electronic", "Jazz", "Pop/Rock"])
def test_filterAlbumAdmin(chrome_driver, status_filter):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)
    login_success_superAdmin(chrome_driver)

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//*[@id="productManager"]/div[1]/div[3]/div[2]').click()
    time.sleep(2)

    # Chọn tùy chọn từ danh sách thả xuống
    select_element = chrome_driver.find_element(By.XPATH, '//select[@onchange="loadAlbumByAjax()"]')
    select = Select(select_element)  # Tạo đối tượng Select
    select.select_by_visible_text(status_filter)  # Chọn trạng thái từ tham số status_filter
    time.sleep(2)

    # Lấy tất cả các dòng trong bảng
    album_elements = chrome_driver.find_elements(By.CSS_SELECTOR, '.placeholder .info')  # Lấy tất cả các phần tử chứa thông tin album

    # Kiểm tra trạng thái của từng album
    all = True
    for album in album_elements:
        # Tìm phần tử trạng thái trong mỗi dòng
        status_element = album.find_elements(By.CSS_SELECTOR, '.item')[4].text  # Lấy tất cả các phần tử con
        if status_element:
            print(f"Album Status: {status_element}")  # In ra trạng thái của album
            if status_element != status_filter:  # Kiểm tra trạng thái so với status_filter
                all = False
                break

    # Assert kết quả
    assert all, f"Not all albums are in '{status_filter}' status."

    print(f"Test completed: All albums are in '{status_filter}' status.")


@pytest.mark.parametrize("order_status", ["Pending", "Shipping", "Delivered", "Cancel"])
def test_filterOrderAdmin(chrome_driver, order_status):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)
    login_success_superAdmin(chrome_driver)

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[2]').click()

    # Chọn tùy chọn trạng thái từ danh sách thả xuống
    select_element = chrome_driver.find_element(By.XPATH, '//select[@onchange="loadOrderByAjax()"]')
    select = Select(select_element)  # Tạo đối tượng Select
    select.select_by_visible_text(order_status)  # Chọn trạng thái từ tham số order_status
    time.sleep(2)

    # Lấy tất cả các dòng trong bảng
    order_elements = chrome_driver.find_elements(By.CSS_SELECTOR, '.placeholder .info')  # Lấy tất cả các phần tử chứa thông tin đơn hàng

    # Kiểm tra trạng thái của từng đơn hàng
    all_status_correct = True
    for order in order_elements:
        # Tìm phần tử trạng thái trong mỗi dòng
        status_element = order.find_elements(By.CSS_SELECTOR, '.item')[-1].text  # Lấy phần tử trạng thái (cột cuối cùng)
        if status_element:
            print(f"Order Status: {status_element}")  # In ra trạng thái của đơn hàng
            if status_element != order_status:  # Kiểm tra trạng thái so với giá trị order_status
                all_status_correct = False
                break

    # Assert kết quả
    assert all_status_correct, f"Not all orders are in '{order_status}' status."

    print(f"Test completed: All orders are in '{order_status}' status.")