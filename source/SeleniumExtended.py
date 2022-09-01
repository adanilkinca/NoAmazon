from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import Select
import time

class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()
        except StaleElementReferenceException:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element

    def wait_and_get_elements(self, locator, timeout=None, error=None):
        timeout = timeout if timeout else self.default_timeout
        error = error if error else f"Unable to find elements located by '{locator}'," \
                              f'after timeout of {timeout}'
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(error)
        return elements

    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element_text = element.text
        return element_text

    def wait_and_select_dropdown(self, locator, to_select, select_by='visible_text'):
        """
        :param locator:
        :param to_select:
        :param select_by: Options are 'visible_text', 'index', or value 'value'
        :return:
        """
        select_element = self.wait_until_element_is_visible(locator)
        select = Select(select_element)
        if select_by.lower() == 'visible_text':
            select.select_by_visible_text(to_select)
        elif select_by.lower() == 'index':
            select.select_by_index(to_select)
        elif select_by.lower() == 'value':
            select.select_by_value(to_select)
        else:
            raise Exception(f"Invalid option for 'to_select' parameter. Valid values are 'visible_text', 'index', or value 'value'.")