class BaseLocators:
    LOCATOR_IMAGES = ".//img"
    

class SbisLocators:
    LOCATOR_SBIS_CONTACTS = "//a[text()='Контакты']"
    LOCATOR_SBIS_CONTACTS_REGION = "//*[contains(@class, 'sbis_ru-Region-Chooser__text')]"
    LOCATOR_SBIS_CONTACTS_PARTNERS = "//*[@id='contacts_list']"
    LOCATOR_SBIS_CONTACTS_PARTNERS_CITY = ".//*[contains(@class, 'sbisru-Contacts-List__city')]"
    LOCATOR_SBIS_REGION_SELECTION_PANEL = "//span[contains(@class, 'sbis_ru-Region-Panel')]"
    LOCATOR_SBIS_REGION_SELECTION_PANEL_REGION = "//li[@class='sbis_ru-Region-Panel__item']/span[@class='sbis_ru-link' and contains(text(), 'new_region')]"
    LOCATOR_TENSOR_BANNER = "//*[contains(@class, 'sbisru-Contacts__logo-tensor')]"


class TensorLocators:
    LOCATOR_ABOUT_POWER_IN_PEOPLE_BLOCK = "//div[contains(@class, 's-Grid-col--6') and .//div[contains(@class, 'tensor_ru-Index__block4-content') and .//p[contains(text(), 'Сила в людях')]]]"
    LOCATOR_ABOUT_POWER_IN_PEOPLE_BLOCK_DETAILS = ".//a[text()='Подробнее']"
    LOCATOR_ABOUT_WE_WORK_BLOCK = "//div[contains(@class, 'tensor_ru-About__block3') and .//div[contains(@class, 'tensor_ru-About__block-title-block') and .//h2[contains(text(), 'Работаем')]]]"