from config import TestData
from pages.locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.start_page)

    def all_elements_are_presents(self, locator):
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.presence_of_all_elements_located(locator))
        return elements

    def element_are_present(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        return element

    def element_find(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def elements_find(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements

    def elements_find_true(self, locator) -> bool:
        elements = self.driver.find_elements(*locator)
        return bool(elements)

    def missing_element(self, locator):
        element = WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(locator))
        return element

    def missing_element_true(self, locator) -> bool:
        element = WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(locator))
        return bool(element)

    def element_visibility(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element

    def element_invisibility(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.invisibility_of_element_located(locator))
        return element

    def element_visibility_true(self, element_page) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of(element_page))
        return bool(element)

    def element_invisibility_true(self, element_page) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of(element_page))
        return bool(element)

    def element_present_true(self, locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return bool(element)

    def text_are_present_in_element(self, locator, text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.text_to_be_present_in_element(locator, text))
        return element
        # assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), "PetFriends"))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def accept_cookies_btn(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.AUTH_ACCEPT_COOKIES_BTN)).click()

    def hover_cursor(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def hover_cursor_click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).click(element).perform()

    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.click(element).perform()

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def get_url(self):
        page_url = self.driver.current_url
        return page_url

    def click_clear_send_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).click().pause(2)
        element.clear()
        element.send_keys(text)

    def click_clear_field(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).click().pause(2)
        element.clear()

    def clear_field(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()

    def send_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    def send_text_1(self, locator, text):
        element = self.driver.find_element(*locator)
        return element.send_keys(text)

    def get_attribute_value(self, locator, attr_name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        value = element.get_attribute(attr_name)
        return value

    def elementes_get_attribute_value(self, locator, attribut):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        list_attr_name = []
        for i in range(len(elements)):
            value = elements[i].get_attribute(attribut)
            list_attr_name.append(value)
        return list_attr_name
