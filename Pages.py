from BaseApp import BasePage
from selenium.webdriver.common.by import By


class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_SEARCH_FIELD_XPATH = (By.XPATH, "//a[@href='/contacts']")
    LOCATOR_SEARCH_TAG_NAME = (By.TAG_NAME, "Разработчик системы СБИС — компания «Тензор»")


class SearchHelper(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def find_word(self, text):
        return self.find_element((YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD[0], text), time=5).click()

    def find_unit(self, xpath):
        return self.find_element((YandexSeacrhLocators.LOCATOR_SEARCH_FIELD_XPATH[0], xpath), time=5)

    def click_img(self, xpath):
        return self.find_element((YandexSeacrhLocators.LOCATOR_SEARCH_FIELD_XPATH[0], xpath), time=5).click()

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=5).click()

    def click_on_the_search_field_text(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_SEARCH_FIELD_XPATH, time=5).click()

    def check_navigation_bar(self, selector):
        return self.find_elements((YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR[0], selector), time=5)

    def click_on_the_search_tag_name(self):
        all_img = self.find_elements(YandexSeacrhLocators.LOCATOR_SEARCH_TAG_NAME, time=5)
        img_menu = [x.text for x in all_img if len(x.text) > 0]
        return img_menu







