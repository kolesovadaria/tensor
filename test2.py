from Pages import SearchHelper
import time


def test_google_search(browser):
    sbis_main_page = SearchHelper(browser)
    sbis_main_page.go_to_site()
    sbis_main_page.click_img("//a[@href='/contacts']")
    sbis_main_page.find_unit("//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link' and contains(text(), "
        "'Нижегородская обл.')]")

    sbis_main_page.find_unit("//div[@class='sbisru-Contacts-List__name sbisru-Contacts-List--ellipsis "
                                      "sbisru-Contacts__text--md pb-4 pb-xm-12 pr-xm-32']")

    button = sbis_main_page.click_img("//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link' and contains(text(), "
                                      "'Нижегородская обл.')]")

    #sbis_main_page.click_img("//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link' and contains(text(), "
                             #"'Нижегородская обл.')]")
    time.sleep(10)

    sbis_main_page.click_img("//span[@title='Камчатский край']")
    time.sleep(5)

    sbis_main_page.find_unit("//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link' and contains(text(), "
                                     "'Камчатский край')]")

    sbis_main_page.find_unit("//div[@class='sbisru-Contacts-City__item-name sbisru-link pr-4 pr-xm-8 "
                                      "sbisru-text-main' and contains(text(),"
                                      "'Петропавловск-Камчатский')]")
