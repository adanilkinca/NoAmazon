import pytest
from NoAmazon.source.pages.MyAccountSignedOut import MyAccountSignedOut
from NoAmazon.source.pages.MyAccountSignedIn import MyAccountSignedIn
from NoAmazon.source.helpers.generic_helpers import generate_random_email_and_password

@pytest.mark.usefixtures('init_driver')
class TestRegisterNewUser:

    @pytest.mark.tcid146
    def test_register_valid_new_user(self):
        my_account_o = MyAccountSignedOut(self.driver)
        my_account_i = MyAccountSignedIn(self.driver)

        my_account_o.go_to_my_account()

        random_email = generate_random_email_and_password()
        my_account_o.input_register_email(random_email['email'])
        my_account_o.input_register_password('098xyJop!b')
        my_account_o.click_register_button()

        # verify user is registered
        my_account_i.verify_user_is_signed_in()