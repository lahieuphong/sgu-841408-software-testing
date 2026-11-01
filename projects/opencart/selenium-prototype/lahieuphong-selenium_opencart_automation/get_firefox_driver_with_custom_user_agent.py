# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
#
#
# def get_firefox_driver_with_custom_user_agent(profile_path):
#     options = Options()
#     options.set_preference("general.useragent.override",
#                            "Mozilla/5.0 (Macintosh; Apple M2) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/130.0.6723.92 Safari/537.36")
#     options.set_preference("browser.cache.disk.enable", False)
#     options.set_preference("browser.cache.memory.enable", False)
#     options.set_preference("browser.cache.offline.enable", False)
#     options.set_preference("browser.cache.disk_cache_ssl", False)
#     options.set_preference("network.http.use-cache", False)
#     options.add_argument(f"--profile={profile_path}")
#
#     return webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def get_firefox_driver_with_custom_user_agent(profile_path):
    options = Options()
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Macintosh; Apple M2) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/130.0.6723.92 Safari/537.36")
    options.add_argument(f"--profile={profile_path}")  # Đảm bảo profile path đúng

    # Loại bỏ các cài đặt cache khác vì chúng không cần thiết ở đây
    return webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
