from BaseApp import BasePage
from selenium.webdriver.common.by import By


class SeacrhLocators:
    LOCATOR_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_SEARCH_FIELD_XPATH = (By.XPATH, "//a[@href='/contacts']")
    LOCATOR_SEARCH_TAG_NAME = (By.TAG_NAME, "Разработчик системы СБИС — компания «Тензор»")


class SearchHelper(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def find_word(self, text):
        return self.find_element((SeacrhLocators.LOCATOR_SEARCH_FIELD[0], text), time=5).click()

    def find_unit(self, xpath):
        return self.find_element((SeacrhLocators.LOCATOR_SEARCH_FIELD_XPATH[0], xpath), time=5)

    def click_img(self, xpath):
        return self.find_element((SeacrhLocators.LOCATOR_SEARCH_FIELD_XPATH[0], xpath), time=5).click()

    def check_navigation_bar(self, selector):
        return self.find_elements((SeacrhLocators.LOCATOR_NAVIGATION_BAR[0], selector), time=5)

    def check_url_and_title(self):
        new_reg = self.get_url_and_title()
        values_region = [x for x in new_reg if len(x) > 0]
        return values_region


