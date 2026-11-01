import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import os


def get_firefox_driver_with_custom_user_agent(profile_path):
    options = Options()

    # Set user agent
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Macintosh; Apple M2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.92 Safari/537.36")

    # Use custom profile path
    if profile_path:
        if not os.path.exists(profile_path):
            os.makedirs(profile_path)
        options.add_argument(f"-profile")
        options.add_argument(profile_path)

    # Set additional options
    options.set_preference("dom.webnotifications.enabled", False)  # Disable notifications
    options.set_preference("media.peerconnection.enabled", False)  # Disable WebRTC
    options.set_preference("network.http.use-cache", False)  # Disable caching
    options.set_preference("webdriver_assume_untrusted_issuer", False)  # Ignore certificate errors

    # Start Firefox WebDriver with custom options
    return webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)


# Example usage of the function
profile_path = "./my_firefox_profile"  # Set your desired profile path
driver = get_firefox_driver_with_custom_user_agent(profile_path)

# Navigate to OpenCart
driver.get("https://demo.opencart.com/")

# Perform actions or keep browser open as needed
time.sleep(1200)  # Pause to observe the loaded page

# Close the browser
driver.quit()
