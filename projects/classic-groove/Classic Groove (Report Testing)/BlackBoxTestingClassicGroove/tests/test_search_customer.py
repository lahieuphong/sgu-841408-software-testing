import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_driver import chrome_driver
from pages.login import login_success_customer
from pages.navigate import navigate_to_index_page


@pytest.mark.parametrize(
    "search_term",
    [
        "Evo Sessions",
        "acousticNOW",
        "It Serves You Right To Suffer",
        "Love For Sale",
        "Dawn FM",
        "Fearless (Taylor’s Version)",
        "Gold",
        "Beleive",
        "Jordi",
        "J97",
        "Mochiii"
    ]
)
def test_search_valid(chrome_driver, search_term):
    # Điều hướng tới trang chính
    navigate_to_index_page(chrome_driver)
    print(f"\n")
    print(f"-" * 40)

    # Đăng nhập thành công với tư cách khách hàng
    login_success_customer(chrome_driver)
    print(f"-" * 40)

    # Tìm kiếm và nhập từ khóa vào ô tìm kiếm
    search_input = chrome_driver.find_element(By.ID, "search-btn")
    search_input.click()
    search_input.send_keys(search_term)
    time.sleep(1)

    # In tiêu đề "Features"
    print("Features")

    # Nhấn vào nút tìm kiếm (biểu tượng kính lúp)
    search_button = chrome_driver.find_element(By.CSS_SELECTOR, "div.search i.fa-solid.fa-magnifying-glass")
    search_button.click()
    time.sleep(1)

    # Chờ để kết quả tìm kiếm hiển thị
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.grid-item")))

    # Lấy danh sách tất cả các phần tử có class "grid-item"
    grid_items = chrome_driver.find_elements(By.CSS_SELECTOR, "div.grid-item")

    # Tạo danh sách các chỉ số của các mục
    item_indices = list(range(1, len(grid_items) + 1))

    # In danh sách các chỉ số
    print(f"Tìm kiếm với từ khóa '{search_term}':")
    print(f"Các mục tìm thấy: {item_indices}")

    # In số lượng mục tìm thấy
    print(f"Có {len(item_indices)} mục được tìm thấy với search '{search_term}'")

# bug: tìm kiếm kí tự đặc biệt "%" nhưng lại hiển thị danh sách
def test_search_percent(chrome_driver):
    # Điều hướng tới trang chính
    navigate_to_index_page(chrome_driver)
    print(f"\n")
    print(f"-" * 40)

    # Đăng nhập thành công với tư cách khách hàng
    login_success_customer(chrome_driver)
    print(f"-" * 40)

    # Tìm kiếm và nhập ký tự "%" vào ô tìm kiếm
    search_input = chrome_driver.find_element(By.ID, "search-btn")
    search_input.click()
    search_input.send_keys("%")
    time.sleep(1)

    # In tiêu đề "Features"
    print("Features")

    # Nhấn vào nút tìm kiếm (biểu tượng kính lúp)
    search_button = chrome_driver.find_element(By.CSS_SELECTOR, "div.search i.fa-solid.fa-magnifying-glass")
    search_button.click()
    time.sleep(1)

    # Chờ để kết quả tìm kiếm hiển thị
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.grid-item")))

    # Lấy danh sách tất cả các phần tử có class "grid-item"
    grid_items = chrome_driver.find_elements(By.CSS_SELECTOR, "div.grid-item")

    # Tạo danh sách các chỉ số của các mục
    item_indices = list(range(1, len(grid_items) + 1))

    # In danh sách các chỉ số
    print(f"Các mục tìm thấy: {item_indices}")

    # Assertion: Kỳ vọng item_indices phải rỗng (0 mục được tìm thấy)
    expected_item_count = 0
    actual_item_count = len(item_indices)

    assert actual_item_count == expected_item_count, (
        f"Test Fail: Số lượng mục tìm thấy ({actual_item_count}) không khớp với kỳ vọng ({expected_item_count})"
    )