from base_page import BasePage
from utils.locators import SbisLocators, TensorLocators
from utils.const import SBIS_URL
from typing import List
from pylenium.element import Element


class SbiSPage(BasePage):
    def __init__(self, py):
        super().__init__(py)
        self.starting_url = SBIS_URL
        
    def start(self) -> None:
        """
        Запускает браузер и открывает стартовую страницу.
        """
        self.py.log.this(f"СТАРТ")
        self.open_url(self.starting_url)
        
    def contacts_change_region(self, new_region: str) -> None:
        """
        Меняет регион на странице "Контакты".
        """
        region_panel_link = self.by_xpath_get_element(SbisLocators.LOCATOR_SBIS_CONTACTS_REGION, "Регион")
        self.click_element(region_panel_link, "Панель выбора региона")
        region_button = self.by_xpath_get_element(SbisLocators.LOCATOR_SBIS_REGION_SELECTION_PANEL_REGION.replace("new_region", new_region), "Кнопка смены региона")
        self.click_element(region_button, "Кнопка смены региона")
        
    def contacts_check_region(self, expected_region: str) -> bool:
        """
        Проверяет регион на странице "Контакты" на соовтествие переданной строке.
        """
        region_element = self.by_xpath_get_element(SbisLocators.LOCATOR_SBIS_CONTACTS_REGION, "Регион")
        return self.element_has_text(region_element, expected_region, "Регион")
        
    def contacts_check_region_title(self, expected_title: str) -> bool:
        """
        Проверяет что заголовок блока "Партнеры" на странице "Контакты" соответствует
        переданной строке.
        """
        region_contacts_title = self.by_xpath_get_nested_element(SbisLocators.LOCATOR_SBIS_CONTACTS_PARTNERS, SbisLocators.LOCATOR_SBIS_CONTACTS_PARTNERS_CITY, "Партнеры")
        return self.element_has_text(region_contacts_title, expected_title, "Партнеры, заголовок")
        
    def sbis_go_to_contacts(self) -> None:
        """
        Переходит на страницу "Контакты" с главной СБИС.
        """
        element = self.by_xpath_get_element(SbisLocators.LOCATOR_SBIS_CONTACTS, "Контакты")
        self.click_element(element, "Контакты")
        
    def contacts_click_tensor_banner(self) -> None:
        """
        Переходит на сайт Тензор со страницы СБИС "Контакты" через баннер.
        """
        element = self.by_xpath_get_element(SbisLocators.LOCATOR_TENSOR_BANNER, "баннер Тензор")
        self.click_element(element, "баннер Тензор")
        self.switch_to_next_tab()
        
    def tensor_about_power_in_people_block_exists(self) -> bool:
        """
        Проверяет наличие блока с заголовком "Сила в людях" на сайте Тензор.
        """
        return self.by_xpath_element_exists(TensorLocators.LOCATOR_ABOUT_POWER_IN_PEOPLE_BLOCK, "Сила в людях")
        
    def go_to_tensor_about_power_in_people_block_link(self) -> None:
        """
        Переходит по ссылке "Подробнее" в блоке "Сила в людях" на сайте Тензор.
        """
        about_power_in_people_details_link = self.by_xpath_get_nested_element(
            TensorLocators.LOCATOR_ABOUT_POWER_IN_PEOPLE_BLOCK,
            TensorLocators.LOCATOR_ABOUT_POWER_IN_PEOPLE_BLOCK_DETAILS,
            "Сила в людях")
        link = self.get_element_link(about_power_in_people_details_link, "Сила в людях, подробнее")
        self.open_url(link)
        
    def tensor_about_we_work_block_get_images(self) -> List[Element]:
        """
        Проверяет размер изображений в блоке "Работаем" на странице Тензор
        "О компании".
        """
        images = self.by_xpath_get_nested_images(TensorLocators.LOCATOR_ABOUT_WE_WORK_BLOCK, "Работаем")
        return images
        
    