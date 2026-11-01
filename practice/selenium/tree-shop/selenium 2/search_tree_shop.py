import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Sử dụng Chrome WebDriver
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize("keyword", ["abc"])
def test_search_tree_shop(driver, keyword):
    driver.get("https://www.tree-shop.co.uk/")

    time.sleep(3)

    # Tìm và trỏ chuột vào ô tìm kiếm
    search_box = driver.find_element(By.CSS_SELECTOR, "input.search-field")
    search_box.click()

    # Gửi từ khóa vào ô tìm kiếm
    search_box.send_keys(keyword)

    # Tìm và nhấn nút tìm kiếm
    search_button = driver.find_element(By.CSS_SELECTOR, "input.search-submit")
    search_button.click()

    time.sleep(3)

    # Lấy URL hiện tại sau khi tìm kiếm
    current_url = driver.current_url

    expected_url = f"https://www.tree-shop.co.uk/?s={keyword}&post_type=product"
    if expected_url in current_url:
        print(f"Trang kết quả tìm kiếm: {current_url}")

        try:
            result_count = driver.find_element(By.CSS_SELECTOR, "p.woocommerce-result-count")
            print(result_count.text)
        except:
            no_product_message = driver.find_element(By.CSS_SELECTOR, "div.woocommerce-info")
            print(no_product_message.text)

        # print("Không tìm thấy kết quả phù hợp.")


@pytest.mark.parametrize("keyword", ["Tree"])
def test_select_one_product(driver, keyword):
    # Gọi hàm tìm kiếm sản phẩm
    test_search_tree_shop(driver, keyword)

    # Chờ thêm để trang kết quả tải hoàn toàn
    time.sleep(3)

    # Tìm và nhấn vào nút 'View Product'
    view_product_button = driver.find_element(By.CSS_SELECTOR, "a.button")
    view_product_button.click()

    # Chờ để trang sản phẩm tải hoàn toàn
    time.sleep(3)

    # Tìm và nhấn nút 'Add to basket'
    add_to_basket_button = driver.find_element(By.CSS_SELECTOR, "button[name='variation_id'][value='117636']")
    add_to_basket_button.click()

    # Chờ để xác nhận thêm sản phẩm vào giỏ hàng
    time.sleep(3)

    # Kiểm tra nếu sản phẩm đã được thêm thành công
    success_message = driver.find_element(By.CSS_SELECTOR, "div.woocommerce-message")
    if success_message:
        print("Sản phẩm đã được thêm vào giỏ hàng thành công.")
    else:
        print("Không thành công trong việc thêm sản phẩm vào giỏ hàng.")


@pytest.mark.parametrize("keyword", ["Tree"])
def test_select_one_product_increase_quantity(driver, keyword):
    # Gọi hàm để tìm kiếm và chọn sản phẩm
    test_select_one_product(driver, keyword)

    # Chờ để trang sản phẩm tải hoàn toàn
    time.sleep(3)

    # Tìm nút tăng số lượng và nhấn hai lần
    increase_button = driver.find_element(By.CSS_SELECTOR, "button.increase")
    increase_button.click()  # Lần thứ nhất
    # time.sleep(1)  # Chờ một chút giữa các lần nhấn
    # increase_button.click()  # Lần thứ hai

    # Chờ để xem kết quả
    time.sleep(3)

    # Tìm và nhấn nút 'Add to basket'
    add_to_basket_button = driver.find_element(By.CSS_SELECTOR, "button[name='variation_id'][value='117636']")
    add_to_basket_button.click()

    # Chờ để xác nhận thêm sản phẩm vào giỏ hàng
    time.sleep(3)

    # Kiểm tra nếu sản phẩm đã được thêm thành công
    success_message = driver.find_element(By.CSS_SELECTOR, "div.woocommerce-message")
    if success_message:
        print("Sản phẩm đã được thêm vào giỏ hàng thành công.")

        # Kiểm tra giỏ hàng
        view_basket_button = driver.find_element(By.CSS_SELECTOR, "a.link[href='https://www.tree-shop.co.uk/basket/']")
        view_basket_button.click()
        time.sleep(3)

        # Kiểm tra xem đã tới trang giỏ hàng chưa
        assert "https://www.tree-shop.co.uk/basket/" in driver.current_url

    else:
        print("Không thành công trong việc thêm sản phẩm vào giỏ hàng.")


@pytest.mark.parametrize("keyword", ["Tree"])
def test_select_many_product(driver, keyword):
    # Thêm sản phẩm 1 vào giỏ hàng
    test_search_tree_shop(driver, keyword)
    time.sleep(3)
    product1_button = driver.find_element(By.CSS_SELECTOR, "a[href='https://www.tree-shop.co.uk/product/hornbeam-tree-carpinus-betula/']")
    product1_button.click()
    time.sleep(3)
    add_to_basket_button1 = driver.find_element(By.CSS_SELECTOR, "button[value='117636']")
    add_to_basket_button1.click()
    time.sleep(3)
    # Kiểm tra nếu sản phẩm đã được thêm thành công
    success_message = driver.find_element(By.CSS_SELECTOR, "div.woocommerce-message")
    if success_message:
        print("Sản phẩm đã được thêm vào giỏ hàng thành công.")

        # Kiểm tra giỏ hàng
        view_basket_button = driver.find_element(By.CSS_SELECTOR, "a.link[href='https://www.tree-shop.co.uk/basket/']")
        view_basket_button.click()
        time.sleep(3)

        # Kiểm tra xem đã tới trang giỏ hàng chưa
        assert "https://www.tree-shop.co.uk/basket/" in driver.current_url

    else:
        print("Không thành công trong việc thêm sản phẩm vào giỏ hàng.")

    # Thêm sản phẩm 2 vào giỏ hàng
    test_search_tree_shop(driver, keyword)
    time.sleep(3)
    product2_button = driver.find_element(By.CSS_SELECTOR, "a[href='https://www.tree-shop.co.uk/product/wild-cherry-tree-prunus-avium/']")
    product2_button.click()
    time.sleep(3)
    add_to_basket_button2 = driver.find_element(By.CSS_SELECTOR, "button[value='1049']")
    add_to_basket_button2.click()
    time.sleep(3)
    # Kiểm tra nếu sản phẩm đã được thêm thành công
    success_message = driver.find_element(By.CSS_SELECTOR, "div.woocommerce-message")
    if success_message:
        print("Sản phẩm đã được thêm vào giỏ hàng thành công.")

        # Kiểm tra giỏ hàng
        view_basket_button = driver.find_element(By.CSS_SELECTOR, "a.link[href='https://www.tree-shop.co.uk/basket/']")
        view_basket_button.click()
        time.sleep(3)

        # Kiểm tra xem đã tới trang giỏ hàng chưa
        assert "https://www.tree-shop.co.uk/basket/" in driver.current_url

    else:
        print("Không thành công trong việc thêm sản phẩm vào giỏ hàng.")

    # Thêm sản phẩm 3 vào giỏ hàng
    test_search_tree_shop(driver, keyword)
    time.sleep(3)
    product3_button = driver.find_element(By.CSS_SELECTOR, "a[href='https://www.tree-shop.co.uk/product/patio-plum-tree-opal-prunus-domestica-patio-fruit-tree-2/']")
    product3_button.click()
    time.sleep(3)
    add_to_basket_button3 = driver.find_element(By.CSS_SELECTOR, "button[value='1332']")
    add_to_basket_button3.click()
    time.sleep(3)
    # Kiểm tra nếu sản phẩm đã được thêm thành công
    success_message = driver.find_element(By.CSS_SELECTOR, "div.woocommerce-message")
    if success_message:
        print("Sản phẩm đã được thêm vào giỏ hàng thành công.")

        # Kiểm tra giỏ hàng
        view_basket_button = driver.find_element(By.CSS_SELECTOR, "a.link[href='https://www.tree-shop.co.uk/basket/']")
        view_basket_button.click()
        time.sleep(3)

        # Kiểm tra xem đã tới trang giỏ hàng chưa
        assert "https://www.tree-shop.co.uk/basket/" in driver.current_url

    else:
        print("Không thành công trong việc thêm sản phẩm vào giỏ hàng.")

    # Kiểm tra giỏ hàng
    view_basket_button = driver.find_element(By.CSS_SELECTOR, "a.link[href='https://www.tree-shop.co.uk/basket/']")
    view_basket_button.click()
    time.sleep(3)

    # Kiểm tra xem đã tới trang giỏ hàng chưa
    assert "https://www.tree-shop.co.uk/basket/" in driver.current_url


# def test_check_all_links(driver):
#     # Truy cập trang web
#     driver.get("https://www.tree-shop.co.uk/")
#
#     # Chờ để trang web tải hoàn toàn
#     time.sleep(3)
#
#     # Tìm tất cả các liên kết trên trang
#     links = driver.find_elements(By.TAG_NAME, "a")
#
#     # Danh sách để lưu các liên kết hỏng
#     broken_links = []
#
#     for link in links:
#         url = link.get_attribute("href")
#         # Kiểm tra nếu liên kết không phải là None và không phải là mailto hay tel
#         if url and not (url.startswith('mailto:') or url.startswith('tel:')):
#             try:
#                 # Gửi yêu cầu HTTP tới liên kết
#                 response = requests.head(url, allow_redirects=True)
#                 # Kiểm tra mã trạng thái HTTP
#                 if response.status_code >= 400:
#                     print(f"Liên kết hỏng: {url} - Status Code: {response.status_code}")
#                     broken_links.append(url)
#                 else:
#                     print(f"Liên kết hoạt động: {url} - Status Code: {response.status_code}")
#             except requests.exceptions.RequestException as e:
#                 print(f"Không thể kiểm tra liên kết: {url} - Lỗi: {e}")
#                 broken_links.append(url)
#         elif url and (url.startswith('mailto:') or url.startswith('tel:')):
#             continue  # Bỏ qua các liên kết mailto và tel
#         else:
#             print("Liên kết không có URL hợp lệ.")
#
#     # In ra tổng số liên kết hỏng và danh sách các liên kết hỏng
#     if broken_links:
#         print(f"Đã tìm thấy {len(broken_links)} liên kết hỏng: {', '.join(broken_links)}")
#     else:
#         print("Tất cả các liên kết đều hoạt động tốt.")


def test_check_all_links():
    url = "https://www.tree-shop.co.uk/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()

        # Lấy tất cả thẻ <a> và trích xuất href
        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href']
            # Nếu liên kết bắt đầu bằng "https://www.tree-shop.co.uk/" thì thêm vào danh sách
            if link.startswith("https://www.tree-shop.co.uk/"):
                links.add(link)

        # Kiểm tra trạng thái của các liên kết
        for link in links:
            try:
                link_response = requests.get(link)
                if link_response.status_code == 200:
                    print(f"Liên kết hoạt động: {link} - Status Code: {link_response.status_code}")
                else:
                    print(f"Liên kết lỗi: {link} - Status Code: {link_response.status_code}")
            except requests.RequestException as e:
                print(f"Liên kết lỗi: {link} - Error: {e}")

    except requests.RequestException as e:
        print(f"Không thể truy cập trang web: {url} - Error: {e}")
