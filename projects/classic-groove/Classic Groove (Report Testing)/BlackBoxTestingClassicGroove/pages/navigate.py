import time


def navigate_to_index_page(chrome_driver):
    chrome_driver.get("http://localhost/Classic-Groove/index.php")
    time.sleep(1)
    return chrome_driver