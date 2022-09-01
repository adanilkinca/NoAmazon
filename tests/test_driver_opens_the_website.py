import pytest

@pytest.mark.usefixtures("init_driver")
class TestOpenSite():

    def test_open_site(self):
        print('I am first test line 1')
        print('I am first test line 2')
        self.driver.get('http://localhost/noamazon/')
        # import pdb; pdb.set_trace()
#DONT FORGET TO WRITE in CMD: set BROWSER=chrome (or another one) in Windows
# or 'export BROWSER=chrome' in Mac!