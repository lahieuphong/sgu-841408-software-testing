import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

product_titles = [
    "ASPEN",
    "Bird Cherry trees",
    "Black Walnut trees",
    "Downy Birch"
]

product_values = [
    1054,
    1144,
    68948,
    1135
]

def test_add_products_to_basket(driver):
    driver.get("https://www.tree-shop.co.uk/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "s")))

    selected_titles = random.sample(product_titles, 2)
    total_price = 0  # Initialize total price variable

    for title in selected_titles:
        index = product_titles.index(title)
        value = product_values[index]

        search_field = driver.find_element(By.NAME, "s")
        search_field.clear()
        search_field.send_keys(title)

        search_button = driver.find_element(By.CLASS_NAME, "search-submit")
        search_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(@class, 'woocommerce-loop-product__title')]")))

        search_results = driver.find_elements(By.XPATH, "//h2[contains(@class, 'woocommerce-loop-product__title')]")
        for result in search_results:
            print(result.text)  # In ra tên sản phẩm

        if title not in [result.text for result in search_results]:
            print(f"Sản phẩm '{title}' không có trong kết quả tìm kiếm.")
            continue

        product_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, f"//h2[contains(@class, 'woocommerce-loop-product__title')]/a[text()='{title}']"))
        )
        product_link.click()

        random_quantity = random.randint(2, 5)
        for _ in range(random_quantity - 1):
            increase_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "increase"))
            )
            increase_button.click()

        add_to_basket_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[@name='variation_id' and @value='{value}']"))
        )
        add_to_basket_button.click()

        # Kiểm tra và in giá sản phẩm
        product_price = float(driver.find_element(By.XPATH, "//span[contains(@class, 'woocommerce-Price-amount')]/bdi").text.replace('£', '').replace(',', ''))
        print(f"Giá sản phẩm: {product_price:.2f}, Số lượng: {random_quantity}")
        total_price += product_price * random_quantity
        print(f"Tổng giá hiện tại: {total_price:.2f}")

        driver.get("https://www.tree-shop.co.uk/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "s")))

    basket_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'link') and @title='View basket']"))
    )
    basket_link.click()

    return total_price  # Trả về tổng giá trị đã tính toán


def test_verify_subtotal(driver):
    # Thêm sản phẩm vào giỏ hàng
    total_price = test_add_products_to_basket(driver)

    if total_price is None:
        print("Lỗi: Tổng giá trị sản phẩm không được xác định.")
        return  # Hoặc có thể raise Exception

    # Tìm phần tử subtotal hiển thị trên trang
    subtotal_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tr[contains(@class, 'cart-subtotal')]/td/span[contains(@class, 'woocommerce-Price-amount')]"))
    )
    subtotal_text = subtotal_element.text
    subtotal_value = float(subtotal_text.replace('£', '').replace(',', ''))

    # Debugging: In ra cả hai giá trị để xác thực
    print(f"Calculated Total: £{total_price:.2f}, Subtotal from page: £{subtotal_value:.2f}")

    # Kiểm tra nếu tổng giá trị đã tính toán khớp với subtotal hiển thị
    assert abs(subtotal_value - total_price) < 0.01, f"Subtotal does not match! Expected: £{total_price:.2f}, Found: £{subtotal_value:.2f}"

