import pytest
from NoAmazon.source.pages.MyAccountSignedOut import MyAccountSignedOut

@pytest.mark.usefixtures('init_driver')
class TestLoginNegative:

    @pytest.mark.tcid145
    @pytest.mark.smoke
    def test_login_nonexisting_user(self):
        print('*******')
        print('TEST LOGIN DOES NOT EXIST')
        print('*******')
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username('dj;lJPf')
        my_account.input_login_password('iso<Djg')
        my_account.click_login_button()

        # verify error message
#TO DO: not hardcode keys of the 'my_account.input_login_username'!       
        expected_err = 'HError: The username dj;lJPf is not registered on this site. If you are unsure of your username, try your email address instead.'
        my_account.wait_until_error_is_displayed(expected_err)