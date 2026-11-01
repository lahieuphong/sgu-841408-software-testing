# Assignment 2: OpenCart Selenium tests

This is the consolidated Assignment 2 source for the local OpenCart installation at `http://localhost/demo/`.
It retains the expanded navigation tests and the older Canon EOS 5D checkout scenario with product options.

## Setup and execution

From this directory, use Python 3.12 or newer with Chrome and Firefox installed:

```bash
python -m pip install -r requirements.txt pytest-html
python -m pytest -v
python -m pytest test_navigation.py -v
python -m pytest --html=report.html
```

The tests use the original local demo accounts, product data and administration setup defined in the scripts.
OpenCart and the matching test data must be available before running them. WebDriver Manager handles drivers for the Selenium fixtures.

## Source files

| File | Coverage |
| --- | --- |
| `test_login_logout.py` | Login, invalid credentials, logout and session behavior |
| `test_form_submission.py` | Contact forms and special-character inputs |
| `test_navigation.py` | Sitemap, products, cart, customer and guest checkout, product options |
| `test_data_validation.py` | Product details, cart totals and administration dashboard |
| `test_error_handling.py` | Invalid contact/registration fields and invalid quantities |
| `test_search_functionality.py` | Matching and nonmatching search terms |
| `test_responsive_design.py` | Chrome/Firefox page loading and layout checks |
| `test_all_links_status_report.py` | Link status checks and text output |
| `test_login_http.py` | Three HTTP login checks using requests and unittest |

The HTTP login file was formerly named `white_box_login.py`; it checks HTTP responses rather than internal application code.
Its new `test_` filename makes the existing checks discoverable by pytest.

`all_links_status_report.txt` is a saved link-check result. The three distinct historical HTML reports are in
[`../reports/`](../reports/), named `automation-2024-11-13.html`, `automation-2024-11-26.html` and `automation-2024-11-27.html`.
Those reports describe their original runs, before this source consolidation.
