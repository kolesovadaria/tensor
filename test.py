from Pages import SearchHelper
import time


def test_google_search(browser):
    sbis_main_page = SearchHelper(browser)
    sbis_main_page.go_to_site()
    sbis_main_page.click_img("//a[@href='/contacts']")
    sbis_main_page.click_img("//img[@alt='Разработчик системы СБИС — компания «Тензор»']")
    sbis_main_page.window()
    time.sleep(10)
    button = sbis_main_page.find_unit(
        "//p[@class='tensor_ru-Index__card-title tensor_ru-pb-16' and contains(text(), "
        "'Сила в людях')]")
    sbis_main_page.execute_script("arguments[0].scrollIntoView(true);", button)
    time.sleep(5)
    sbis_main_page.click_img("//a[@class='tensor_ru-link "
                             "tensor_ru-Index__link' and contains(@href, "
                             "'/about')]")
    time.sleep(5)
    images = sbis_main_page.check_navigation_bar('.tensor_ru-About__block3-image-wrapper img')
    assert all(x.size == images[0].size for x in images)
