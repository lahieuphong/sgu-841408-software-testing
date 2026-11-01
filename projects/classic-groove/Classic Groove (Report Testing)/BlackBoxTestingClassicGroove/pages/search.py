import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clear_search_input(chrome_driver):
    search_input = chrome_driver.find_element(By.ID, "search-btn")
    search_input.clear()


@pytest.mark.parametrize("product_name", ["J97", "Evo Sessions", "Dawn FM", "Beleive"])
def search_product(chrome_driver, product_name):
    # Tìm kiếm và nhập tên sản phẩm vào ô tìm kiếm
    search_input = chrome_driver.find_element(By.ID, "search-btn")
    search_input.click()
    search_input.send_keys(product_name)
    time.sleep(1)

    # Nhấn vào nút tìm kiếm (biểu tượng magnifying glass)
    search_button = chrome_driver.find_element(By.CSS_SELECTOR, "div.search i.fa-solid.fa-magnifying-glass")
    search_button.click()
    time.sleep(1)

    # Chờ để kết quả tìm kiếm hiển thị
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.grid-item")))


# @pytest.mark.parametrize("product_name", ["Evo Sessions", "Dawn FM"])
def search_and_select_product(chrome_driver, product_name):
    search_product(chrome_driver, product_name)

    # Chọn sản phẩm dựa trên tên
    product_item = chrome_driver.find_element(By.XPATH, f"//div[@class='grid-item']//p[contains(text(), '{product_name}')]")
    product_item.click()
    time.sleep(1)