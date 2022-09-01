NoAmazon is a wooCommerce web project by wordpress and MySQL. Currently is only local.
Some important things before run tests ('set' for Windows, 'export' for Mac):

1. source\helpers\config_helpers.py - ask you to login in database, so, use commands:
set DB_USER=<user_name>
set DB_PASSWORD=<password>

2. conftest.py demands to set which browser use, type like:
set BROWSER=chrome

3. tests\api-tests.py demands to fill consumer_key and consumer_secret with correct data.

4. There are 4 marked for @pytest tests:
mark.usefixtures - just to ensure that the site is open
tcid145 - test_login_negative.py (There is text had been changed deliberately: "expected_err = 'HError: The username...", the right one: "'Error: The username..." - to demonstrate various report results)
tcid146 - test_register_new_user.py
tcid147 - test_end_to_end_checkout_guest_user.py (the most complicated one)

5. You can set parameters in source\generic_configs.py and source\helpers\config_helpers.py

6. You should to set standard reports spot, using command like:
set REPORTS_DIR=<Path>\NoAmazon\reports

In order to use allure:
pytest --alluredir=<Path>\NoAmazon\allure_reports
allure serve <Path>\NoAmazon\allure_reports