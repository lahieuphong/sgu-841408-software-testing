from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def logout(chrome_driver):
    # Đợi cho đến khi phần tử chứa nút logout xuất hiện và có thể nhấn được
    logout_button = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.info-placeholder .log-out-button"))
    )

    # Dùng ActionChains để nhấn vào nút "Logout"
    actions = ActionChains(chrome_driver)
    actions.move_to_element(logout_button).click().perform()