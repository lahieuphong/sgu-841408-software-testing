# OpenCart Demo Testing Project 🚀

## Introduction ✨✨
This project is designed to test the OpenCart demo website. It includes various test cases to ensure the functionality and reliability of the website.

## Installation and Running Tests ✨✨

### Prerequisites ✨
- Python 3.x
- pip (Python package installer)
- Selenium
- WebDriver (e.g., ChromeDriver for Chrome)

### Setup ✨

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/Bug03/BlackBoxTesting-OpenCart.git>
   cd <BlackBoxTesting>
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

### Running Tests

You can run all tests by using the `run_tests.py` script:

   ```bash
   python run_tests.py
   ```

Alternatively, you can run specific tests using `pytest`. For example, to run the tests related to the Add to Cart functionality:

   ```bash
   pytest tests/test_add_to_cart.py
   ```
The test results will be generated in an `HTML` format and stored in the `report.html` file.

### Notes
- Ensure that the WebDriver executable (e.g., `chromedriver`, ) is in your system's PATH or specify its location in your test setup.
- You can customize the test configurations and add more test cases as needed.

## Project Structure ✨✨

- `tests/`: Contains all the test cases.
- `pages/`: Contains page object models for different pages of the OpenCart demo website.
- `utils/`: Contains utility files and configurations.

## Example Test Cases ✨✨

- **Login Tests:** These tests verify the user login functionality. They check if a registered user can log in to the OpenCart demo website using valid credentials and access their account.
- **Register Tests:** These tests verify the user registration functionality. They check if a new user can successfully register on the OpenCart demo website by filling out the registration form with valid data and submitting it.
- **Add to Cart Tests:** These tests ensure that products can be added to the shopping cart. They verify that the correct product is added to the cart and that the cart's total is updated accordingly.
- **Checkout Tests:** hese tests validate the checkout process. They simulate a user completing a purchase, including entering shipping and payment information, and confirm that the order is processed successfully.
- **Search Tests:** These tests validate the search functionality of the website. They verify that the search bar returns relevant results when a user enters a search query.
- **Navigation Tests:** These tests ensure that the website's navigation is working correctly. They check if users can navigate between different pages of the website using the navigation menu and links.
- **Responsive Design Tests:** These tests validate the responsiveness of the website. They check if the website's layout and design adapt correctly to different screen sizes and devices.

## Branches ✨
The repository contains the following branches:
- **main:** This is the default branch and contains the latest stable code.
- **test:** This branch contains the latest code changes and is used for testing purposes.
- **fix:** This branch contains bug fixes and is used for fixing issues found during testing.


## Example Pull Request ✨
Here is an example of a pull request:
![img.png](pull_request_example_img%2Fimg.png)
![img_1.png](pull_request_example_img%2Fimg_1.png)
![img_2.png](pull_request_example_img%2Fimg_2.png)
## Test Report
- Test Report: [Test Report](report/report.html)
![report-image-1.png](report%2Freport-image-1.png)
![report-image-2.png](report%2Freport-image-2.png)

## Contributing 🛠️
Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License ✨
This project is licensed under the MIT License.


