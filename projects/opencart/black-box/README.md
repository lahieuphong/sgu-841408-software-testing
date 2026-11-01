# OpenCart black-box testing

This suite combines the personal OpenCart black-box project and its expanded copy into one source tree.
The expanded wishlist, guest-checkout, navigation and review tests are retained together with the shared tests.

## Setup and execution

From this directory, use Python 3.12 or newer with Chrome and Firefox installed and OpenCart running at `http://localhost/demo/`:

```bash
python -m pip install -r requirements.txt pytest-html
python -m pytest tests -v
python -m pytest tests/test_add_to_cart.py -v
python run_tests.py
```

`run_tests.py` invokes pytest with `--html=report.html`. Run it from this directory.
The tests use the original local demo accounts, products, shipping configuration and administration data defined in the scripts.
The shared fixtures use WebDriver Manager; the additional tests using `webdriver.Chrome()` require a working Chrome driver setup.

## Structure

| Path | Purpose |
| --- | --- |
| `pages/` | Reusable login, navigation and cart interactions |
| `tests/` | Pytest cases and test import setup |
| `utils/base_driver.py` | Shared Chrome and Firefox fixtures |
| `imgs/` | Original test failure and report screenshots |
| `reports/` | Two distinct historical HTML test reports |
| `all_links_status_report.txt` | One preserved link-check output |

## Coverage

- Adding single and multiple products, invalid quantities and cart totals.
- Customer and guest checkout, product information and administration checks.
- Contact forms, authentication, session handling and error cases.
- Search results, empty or unusual keywords, Chrome/Firefox loading and layout.
- Wishlist with and without login, menu navigation and product reviews.
- Link status reporting.

The contact form failure test keeps the explicit waits from the expanded copy and the exact validation-message assertions from the original copy.

## Historical results

| Report | Original outcome |
| --- | --- |
| [2024-12-09 11:48](reports/black-box-2024-12-09-1148.html) | 34 passed, 5 failed |
| [2024-12-09 12:26](reports/black-box-2024-12-09-1226.html) | 35 passed, 4 failed |

These are saved results from the original runs. They do not represent a new execution after consolidation.

Original project: <https://github.com/lahieuphong/BlackBoxTestingOpenCartDemo_LaHieuPhong>.
