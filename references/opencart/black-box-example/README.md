# OpenCart Selenium reference example

Independent Page Object Model example imported from [Bug03/BlackBoxTesting-OpenCart](https://github.com/Bug03/BlackBoxTesting-OpenCart). It contains distinct registration, search, navigation, responsive, cart and checkout cases; it is not a duplicate of the personal OpenCart suite.

From this directory, install `requirements.txt` and pytest, prepare the matching local OpenCart demo at `http://localhost/demo/`, then run tests directly, for example `python -m pytest tests/test_add_to_cart.py -v`. The supplied snapshot does not contain the `run_tests.py` mentioned in the former README.

| Path | Content |
| --- | --- |
| `pages/` | Page objects |
| `tests/` | Reference tests |
| `utils/` | Driver setup |
| [report.html](report.html) | Historical HTML output |
| [report/](report/) | Historical report screenshots |
| [pull_request_example_img/](pull_request_example_img/) | Original pull-request examples |

Original authorship and upstream license notices remain applicable. This example retains its historical source and local setup assumptions.

[Reference index](../../README.md)
