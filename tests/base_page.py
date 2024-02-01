from utils.locators import BaseLocators
from pylenium.element import Element
from typing import List


class BasePage:
    def __init__(self, py):
        self.py = py
        
    def open_url(self, url: str) -> None:
        """
        Запускает браузер и переходит по переданному адресу.
        """
        self.py.log.this(f"Открытие страницы {url}")
        try:
            self.py.visit(url)
            self.py.log.this(f"Успешно")
        except Exception as e:
            self.py.log.this((f"Ошибка при открытии страницы {url}: {e}"))
            
    def switch_to_next_tab(self) -> None:
        """
        Переключается на последнюю открытую вкладку.
        """
        self.py.log.this((f"Переход на новую вкладку"))
        try:
            self.py.switch_to.window(index=1)
            self.py.log.this(f"Успешно")
        except Exception as e:
            self.py.log.this((f"Ошибка перехода на новую вкладку: {e}"))
            
    def get_current_url(self) -> str:
        """
        Возвращает url текущей страницы.
        """
        self.py.log.this((f"Получение текущего url"))
        try:
            url = self.py.url()
            self.py.log.this((f"Tекущий url: {url}"))
            return url
        except Exception as e:
            self.py.log.this((f"Ошибка получения текущего url: {e}"))
            
    def get_page_title(self) -> str:
        """
        Возвращает title текущей страницы.
        """
        self.py.log.this(f"Получение заголовка текущей страницы")
        try:
            title = self.py.title()
            self.py.log.this(f"Заголовок текущей страницы: {title}")
            return title
        except Exception as e:
            self.py.log.this(f"Ошибка получения заголовка текущей страницы: {e}")
            
    def click_element(self, element: Element, element_name: str = "(название не указано)") -> None:
        """
        Кликает на переданный элемент.
        """
        self.py.log.this(f"Клик на '{element_name}'")
        try:
            element.click()
            self.py.log.this(f"Успешно")
        except Exception as e:
            self.py.log.this((f"Ошибка клика на '{element_name}': {e}"))
            
    def by_xpath_get_element(self, element_xpath: str, element_name: str = "(название не указано)") -> Element:
        """
        Возвращает элемент страницы по Xpath.
        """
        self.py.log.this(f"Поиск элемента '{element_name}'")
        try:
            element = self.py.getx(element_xpath)
            self.py.log.this(f"Успешно")
            return element
        except Exception as e:
            self.py.log.this((f"Ошибка поиска '{element_name}': {e}"))
            
    def by_xpath_get_nested_element(self, parent_element_xpath: str, nested_element_xpath: str, element_name: str = "(название не указано)") -> Element:
        """
        Возвращает вложенный злемент по локатору родительского элемента на странице
        и локатору вложенного элемента внутри родительского.
        """
        self.py.log.this(f"Поиск вложенного элемента в '{element_name}'")
        try:
            nested_element = self.py.getx(parent_element_xpath).getx(nested_element_xpath)
            self.py.log.this(f"Успешно")
            return nested_element
        except Exception as e:
            self.py.log.this((f"Ошибка поиска вложенного элемента в '{element_name}': {e}"))
        
    def by_xpath_element_exists(self, element_xpath: str, element_name: str = "(название не указано)") -> bool:
        """
        Проверяет наличие элемента на странице по Xpath.
        """
        self.py.log.this(f"Проверка наличия элемента '{element_name}' на странице")
        try:
            self.py.getx(element_xpath).should().be_visible()
            self.py.log.this(f"Успешно")
            return True
        except Exception as e:
            self.py.log.this((f"Ошибка проверки наличия элемента '{element_name}' на странице: {e}"))
            return False
    
    def element_has_text(self, element: Element, expected_text: str, element_name: str = "(название не указано)") -> bool:
        """
        Проверяет что в элементе присутствует заданный текст.
        """
        self.py.log.this(f"Проверка наличия подстроки '{expected_text}' в элементе '{element_name}'")
        try:
            element.should().contain_text(expected_text)
            self.py.log.this(f"Успешно")
            return True
        except Exception as e:
            self.py.log.this((f"Ошибка проверки наличия подстроки '{expected_text}' в элементе '{element_name}': {e}"))
            return False
    
    def current_url_contains(self, expected_text: str) -> bool:
        """
        Проверяет наличие переданной подстроки в url текущей страницы.
        """
        self.py.log.this(f"Проверка наличия подстроки '{expected_text}' в адресе текущей страницы")
        try:
            expected_text in self.py.url()
            self.py.log.this(f"Успешно")
            return True
        except Exception as e:
            self.py.log.this((f"Ошибка проверки наличия подстроки '{expected_text}' в адресе текущей страницы: {e}"))
            return False
            
    def by_xpath_get_nested_images(self, parent_element_xpath: str, element_name: str = "(название не указано)") -> List[Element]:
        """
        Возвращает изображения из вложенного элемента по локатору родительского элемента на странице
        и локатору вложенного элемента внутри родительского.
        """
        self.py.log.this(f"Поиск изображений в элементе '{element_name}'")
        try:
            images = self.py.getx(parent_element_xpath).findx(BaseLocators.LOCATOR_IMAGES)
            self.py.log.this(f"Успешно")
            return images
        except Exception as e:
            self.py.log.this((f"Ошибка поиска изображений в элементе '{element_name}': {e}"))
    
    def get_element_link(self, element: Element, element_name: str = "(название не указано)") -> str:
        """
        Возвращает ссылку из элемента.
        """
        self.py.log.this(f"Поиск ссылки в элементе '{element_name}'")
        try:
            link = element.get_attribute('href')
            self.py.log.this(f"Успешно")
            return link
        except Exception as e:
            self.py.log.this((f"Ошибка поиска ссылки в элементе '{element_name}': {e}"))
        