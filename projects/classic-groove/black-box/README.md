# Classic Groove black-box tests

Selenium/Pytest tests for customer and administrative workflows: registration, role-based login, searches, account editing, albums, orders, cart quantities, checkout totals and error handling.

Run from this directory with the matching local Classic Groove application and original test data available:

```bash
python -m pip install pytest selenium webdriver-manager pytest-html
python -m pytest tests -v
```

`pages/` contains interactions and `utils/base_driver.py` supplies browser fixtures. The local URL remains configured in `pages/navigate.py`.

The [25 December 2024 report](reports/black-box-2024-12-25.html) records 52 passed and 20 failed tests from the original execution. It is historical evidence, not a fresh result after consolidation.

[Classic Groove project](../README.md)
