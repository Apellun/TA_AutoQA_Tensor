
from sbis_bage import SbiSPage
from utils.const import (TENSOR_ABOUT_PAGE_URL, YAROSLAVSKAYA_OBL_REGION_TITLE,
                         YAROSLAVSKAYA_OBL_CONTACTS_PAGE_TITLE,
                         YAROSLAVSKAYA_OBL_CONTACTS_TITLE,
                         KAMCHATSKIY_KRAI_CONTACTS_TITLE,
                         KAMCHATSKIY_KRAI_CONTACTS_URL_SUBSTR,
                         KAMCHATSKIY_KRAI_REGION_TITLE,
                         KAMCHATSKIY_KRAI_CONTACTS_PAGE_TITLE
)
from utils.check_image_sizes import check_images_have_same_sizes


class Test:
    def test_first_scenario(self, py):
        #1) Перейти на https://sbis.ru/ в раздел "Контакты"
        page = SbiSPage(py)
        page.start()
        page.sbis_go_to_contacts()
        
        #2) Найти баннер Тензор, кликнуть по нему
        #3) Перейти на https://tensor.ru/
        page.contacts_click_tensor_banner()

        #4) Проверить, что есть блок "Сила в людях"
        assert page.tensor_about_power_in_people_block_exists()
        
        #5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
        page.follow_tensor_about_power_in_people_block_link()
        assert page.get_current_url() == TENSOR_ABOUT_PAGE_URL

        #6) Находим раздел Работаем и проверяем, что у всех фотографии хронологии одинаковые высота (height) и ширина (width)
        assert check_images_have_same_sizes(page.tensor_about_we_work_block_get_images())

    def test_second_scenario(self, py):
        #1) Перейти на https://sbis.ru/ в раздел "Контакты"
        page = SbiSPage(py)
        page.start()
        page.sbis_go_to_contacts()
        
        #2) Проверить, что определился ваш регион (в нашем примере Ярославская обл.) и есть список партнеров.
        assert page.contacts_check_region(YAROSLAVSKAYA_OBL_REGION_TITLE)
        assert page.contacts_check_partners_region_title(YAROSLAVSKAYA_OBL_CONTACTS_TITLE)
        
        #3) Изменить регион на Камчатский край
        page.contacts_change_region(KAMCHATSKIY_KRAI_REGION_TITLE)
        
        #4) Проверить, что подставился выбранный регион, список партнеров изменился,
        # url и title содержат информацию выбранного региона
        assert page.contacts_check_region(KAMCHATSKIY_KRAI_REGION_TITLE)
        assert page.contacts_check_partners_region_title(KAMCHATSKIY_KRAI_CONTACTS_TITLE)
        assert page.current_url_contains(KAMCHATSKIY_KRAI_CONTACTS_URL_SUBSTR)
        assert page.get_page_title() == KAMCHATSKIY_KRAI_CONTACTS_PAGE_TITLE