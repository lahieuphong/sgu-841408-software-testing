from selenium.webdriver.common.by import By
import time

class AddToCart:
    def __init__(self, driver):
        self.driver = driver

    def go_to_cart_page(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/ul/li[4]/a').click()
        time.sleep(2)

    def choose_product_by_name(self, product_name):
        try:
            self.driver.find_element(By.LINK_TEXT, product_name).click()
            time.sleep(2)
        except:
            print(f"Product with name: {product_name} not found")
            return

    def add_to_cart_in_product_page_with_qty(self, qty):
        self.driver.find_element(By.ID, 'input-quantity').clear()
        self.driver.find_element(By.ID, 'input-quantity').send_keys(qty)
        self.scroll_to_element(self.driver.find_element(By.ID, 'button-cart'))
        self.driver.find_element(By.ID, 'button-cart').click()
        time.sleep(2)

    def get_product_info_in_cart(self):
        products = []
        product_rows = self.driver.find_elements(By.XPATH, '//*[@id="shopping-cart"]//tbody/tr')

        print(f"Found {len(product_rows)} product rows")  # Debug statement

        for product_row in product_rows:
            product = {}
            try:
                product['name'] = product_row.find_element(By.XPATH, 'td[2]/a').text
                product['unit_price'] = product_row.find_element(By.XPATH, 'td[5]').text
                product['quantity'] = product_row.find_element(By.XPATH, 'td[4]//input').get_attribute('value')
                print(f"Product found: {product}")  # Debug statement
                products.append(product)
            except Exception as e:
                print(f"Error retrieving product details: {e}")  # Debug statement

        time.sleep(1)
        return products

    def get_total_price(self):
        total_price = self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div[1]/div/table/tfoot/tr[4]/td[2]').text
        total_price = total_price.replace('$', '').replace(',', '')
        total_price = float(total_price)
        print(f"Total price: {total_price}")
        time.sleep(2)
        return total_price

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")
        time.sleep(1)

    def get_message(self, element_locator):
        """
        Get the message from an element using the provided locator.
        element_locator: A tuple that defines the locator strategy and value (e.g., By.XPATH, 'some_xpath')
        """
        try:
            message_element = self.driver.find_element(*element_locator)
            message = message_element.text
            print(f"Message: {message}")
            return message
        except Exception as e:
            print(f"Error retrieving message: {e}")
            return None