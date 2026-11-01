"""Open the public OpenCart demo using a Chrome or Firefox profile."""
import argparse
import time

from browser_profiles import get_driver_with_custom_profile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--browser", choices=("chrome", "firefox"), default="chrome")
    args = parser.parse_args()
    driver = get_driver_with_custom_profile(f"my_{args.browser}_profile")
    try:
        driver.get("https://demo.opencart.com/")
        time.sleep(1200)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
