# White Box Testing OpenCart Demo

## Important things to note about testing
* Tests should only be run on a test system, never a live one.
* They have been created to help developers test and improve not only OpenCart but also modules too.

## Requirements:
* [GIT](http://git-scm.com/)
* [Composer](https://getcomposer.org/download/)
* A bit of command line knowledge
* Selenium (optional)

## Instructions
* Install Git (most developers will already have this!)
* Install composer
* Git clone OpenCart (you cannot download the ZIP as this will not include the tests).
* Install OpenCart as normal
* Go to your command line (Windows > Run > Cmd), Shell, or Git Bash
* Change directory to /tests/phpunit/ folder
* Type in the command line: composer update (this will create you a vendor folder and download all dependencies)
* Composer will now pull in all of the required externals/dependencies
* run: vendor\bin\phpunit --bootstrap bootstrap.php opencart\admin to run tests in admin folder
* run: vendor\bin\phpunit --bootstrap bootstrap.php opencart\catalog to run tests in catalog folder
* run: vendor\bin\phpunit --bootstrap bootstrap.php opencart\system to run tests in system folder

## Selenium instructions

Running Acceptance (Functional) Tests with Selenium requires a standalone selenium server on your machine.
The server can be downloaded from [here](http://code.google.com/p/selenium/downloads/list). Before starting your Selenium Tests
you have to run the standalone server: `java -jar selenium-server-standalone-2.32.0.jar`. Writing Selenium Tests requires you to extend the OpenCartSeleniumTest class.

* run: vendor\bin\phpunit --bootstrap bootstrap.php selenium\catalog to run tests in system folder

## Please READ!
The tests are still under development, there is hundreds of them to do.

The tests will drop and recreate tables in database specified in `config.php` and `admin/config.php`

## Jenkins Users
You will also see a build.xml file inside the project root which you can use to configure a Jenkins build.

## We need you
If you understand testing, then you know how important it is to any project. If you have a suggestion then we would really like to hear it!

Forum thread: http://forum.opencart.com/viewtopic.php?f=177&t=124532

Please help by contributing to writing unit tests and submitting a pull request!

##  Directory Structure
**The test cases are organized in the following directories:**

*`tests/phpunit/opencart/admin/controller/common/LoginTest.php`: Unit test for the Login controller in the admin section.
*`tests/phpunit/opencart/admin/model/common/LoginModelTest.php`: Unit test for the LoginModel in the admin section.

*`tests/phpunit/opencart/catalog/controller/checkout/CartTest.php`: Unit test for the Cart controller in the frontend.
*`tests/phpunit/opencart/catalog/model/account/ActivityTest.php`: Unit test for the Activity model in the frontend.
*`tests/phpunit/opencart/catalog/model/account/AddressTest.php`: Unit test for the Address model in the frontend.
*`tests/phpunit/opencart/catalog/model/checkout/OrderTest.php`: Unit test for the Order model in the frontend.

*`tests/phpunit/opencart/system/library/CurrencyTest.php`: Unit test for the Currency library.
*`tests/phpunit/opencart/system/library/UrlTest.php`: Unit test for the Url library.

*`tests/phpunit/selenium/catalog/AccountTest.php`: Selenium test for the Account.
*`tests/phpunit/selenium/catalog/CategoryTest.php`: Selenium test for the Category.
*`tests/phpunit/selenium/catalog/CheckoutTest.php`: Selenium test for the Checkout.
*`tests/phpunit/selenium/catalog/ProductTest.php`: Selenium test for the Product.


### Testing Controllers and Models in the Admin Section
```bash
./vendor/bin/phpunit --bootstrap vendor/autoload.php tests/phpunit/opencart/admin/controller/common/LoginTest.php
./vendor/bin/phpunit --bootstrap vendor/autoload.php tests/phpunit/opencart/admin/model/common/LoginModelTest.php
```

### Testing Controllers and Models in the Catalog Section
```bash
./vendor/bin/phpunit --bootstrap vendor/autoload.php tests/phpunit/opencart/catalog/controller/checkout/CartTest.php
./vendor/bin/phpunit --bootstrap vendor/autoload.php tests/phpunit/opencart/catalog/model/account/ActivityTest.php
./vendor/bin/phpunit --bootstrap vendor/autoload.php tests/phpunit/opencart/catalog/model/account/AddressTest.php
./vendor/bin/phpunit --bootstrap vendor/autoload.php tests/phpunit/opencart/catalog/model/checkout/OrderTest.php
```

### Testing System Libraries
```bash
./vendor/bin/phpunit --bootstrap vendor/autoload.php tests/phpunit/opencart/system/library/CurrencyTest.php
./vendor/bin/phpunit --bootstrap vendor/autoload.php tests/phpunit/opencart/system/library/UrlTest.php
```

### Testing Selenium (UI Automation)
```bash
./vendor/bin/phpunit --bootstrap vendor/autoload.php tests/phpunit/selenium/catalog/AccountTest.php
./vendor/bin/phpunit --bootstrap vendor/autoload.php tests/phpunit/selenium/catalog/CategoryTest.php
./vendor/bin/phpunit --bootstrap vendor/autoload.php tests/phpunit/selenium/catalog/CheckoutTest.php
./vendor/bin/phpunit --bootstrap vendor/autoload.php tests/phpunit/selenium/catalog/ProductTest.php
```

## Explanation
- `--bootstrap vendor/autoload.php`: This option ensures that Composer's autoload is loaded before running the tests, allowing classes to be loaded automatically. 
- **Test files**: Each test file is designed to test specific parts of the system, from controllers to models, helping to detect bugs and assess the reliability of the code. 

## Conclusion 
Running the tests is an effective way to ensure the quality of the OpenCart system. White-box testing not only helps detect bugs but also supports the maintenance and sustainable development of the system.