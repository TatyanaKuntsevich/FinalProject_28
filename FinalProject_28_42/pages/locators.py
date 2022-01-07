from selenium.webdriver.common.by import By

#class AuthLocators:
class Locators:
# стартовая страница
    # логотип
    loc_logo = (By.CLASS_NAME, "b-header-b-logo-e-logo")
    # книги на стартовой на странице
    loc_start_books = (By.CLASS_NAME, "product-padding")
    # фото книг на стартовой странице
    loc_start_page_books_img = (By.XPATH, '//div/a/span/img[@class="book-img-cover"]')
    # названия книг на стартовой странице
    loc_start_page_books_name = (By.CLASS_NAME, "product-title")
    # цены книг на стартовой странице
    loc_start_page_books_price = (By.CLASS_NAME, "price-val")
    # избранное на стартовой на странице
    loc_start_page_books_favourites = (By.XPATH, '//a[@data-tooltip_title="Отложить"]/span[@class="header-sprite"]')
    loc_start_page_books_favourites_end = (By.XPATH, '//a[@data-tooltip_title="Отложить"]/span[@class="header-sprite"]')
    # В Корзину
    loc_start_page_books_btn_cart = (By.CLASS_NAME, "buy-avaliable")
# поиск
    # строка поиска
    loc_search_field = (By.ID, "search-field")
    # иконка поиска
    loc_icon_search_field = (By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]')
    # всплывающее окно "ВЫ ИСКАЛИ"
    loc_pop_up_search_field = (By.XPATH, '//span[text()="ВЫ ИСКАЛИ"]')
    loc_pop_up_search_field_1 = (By.XPATH, '//div[@class="b-suggests-thumbs-outer b-header-b-tinyscrollbar"]')
    loc_pop_up_search_field_2 = (By.XPATH, '//div[@class="b-suggests-thumbs-outer b-header-b-tinyscrollbar"]/div')
    loc_pop_up_search_field_3 = (By.XPATH, '//div[@class="b-suggests-block b-suggests-block-m-nopadding"]')
    # кнопка "Очистить всю историю поиска"
    loc_clear_history = (By.XPATH, '//span[@class="b-suggests-item pointer js-suggests-del"]')
    loc_clear_history_1 = (By.XPATH, '//span[text()="Очистить всю историю поиска"]')
    # всплывающее окно "ЧТО ИЩУТ"
    loc_search_what = (By.XPATH, '//span[text()="ЧТО ИЩУТ"]')
    # заголовок с результатом поиска
    loc_title_search_result = (By.CLASS_NAME, "index-top-title")
    # найденные книги
    loc_search_books = (By.XPATH, '//div[@class="product need-watch watched"]')

    # локатор книги "Приключения Шерлока Холмса"
    loc_my_book = (By.XPATH, '//div[@data-product-id="706880"]')

    # кнопка "Следующая"
    loc_search_btn_next_page = (By.XPATH, '//div[@class="pagination-next"]/a[text()="Следующая"]')
    loc_search_btn_next_page_1 = (By.XPATH, '//div[@class="pagination pushstate"]')
    loc_search_btn_next_page_2 = (By.XPATH, '//div[@class="products-row "]')
    loc_search_btn_next_page_3 = (By.XPATH, '//div[@class="pagination-next"]/a[@class="pagination-next__text"]')
    # всего найдено книг
    loc_total_number_search_books = (By.XPATH, '//li[@class="b-stab-e-slider-item b-stab-e-slider-item-m-active "]/a/span[@class="b-stab-e-slider-item-e-txt-m-small js-search-tab-count"]')
    loc_total_number_search_books_1 = (By.XPATH,'//li[@class="b-stab-e-slider-item b-stab-e-slider-item-m-active b-stab-e-slider-item-m-last"]/a/span[@class="b-stab-e-slider-item-e-txt-m-small js-search-tab-count"]')
# иконки
    # иконок в заголовке "Позвонить", "Мой Лабиринт", "Отложено", "Корзина"
    loc_header_button_icons = (By.CLASS_NAME, "b-header-b-personal-e-wrapper-m-closed")
    # иконка в заголовке "Позвонить"
    loc_header_button_icons_call = (By.CLASS_NAME, "b-header-b-personal-e-icon-m-call")
    # иконка в заголовке "Мой Лабиринт"
    loc_header_button_icons_my_labirint = (By.CLASS_NAME, "b-header-b-personal-e-icon-m-profile")
    # иконка в заголовке "Отложено"
    loc_header_button_icons_putorder = (By.CLASS_NAME, "b-header-b-personal-e-icon-m-putorder")
    # иконка в заголовке "Корзина"
    loc_header_button_icons_cart = (By.CLASS_NAME, "b-header-b-personal-e-icon-count-m-cart")
    # икнонка числа в "Корзине"
    loc_header_button_icons_cart_number  = (By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')
    # иконка в заголовке "Сообщения"
    loc_header_button_icons_messages = (By.CLASS_NAME, "b-header-b-personal-e-icon-m-news")
# кнопки
    # кнопка "В Корзину"
    loc_start_page_books_btn_cart = (By.CLASS_NAME, "buy-avaliable")
    # кнопки "Позвонить", "Сообщения", "Мой Лабиринт", "Отложено", "Корзина"
    loc_header_buttons = (By.CLASS_NAME, "b-header-b-personal-e-list-item")
    # кнопка "Отложено"
    loc_header_button_putorder = (By.XPATH, '//a/span[text()="Отложено"]')
    # кнопка"Корзина"
    loc_header_button_cart = (By.XPATH, '//a/span[text()="Корзина"]')
    # кнопка "Мой Лабиринт"
    loc_header_button_my_labirint = (By.XPATH, '//span[@style="white-space: normal;"]')
    # кнопка "Позвонить"
    loc_header_button_call = (By.XPATH, '//a/span[text()="Позвонить"]')
    # кнопка "Сообщения"
    loc_header_button_messages = (By.XPATH, '//a/span[text()="Сообщения"]')
    # кнопка "Главное 2021"
    loc_header_button_best = (By.XPATH, '//span[@class="b-header-b-menu-e-link"]/a[text()="Главное 2021"]')
    # кнопка "Рейтинг"
    loc_header_button_rating = (By.XPATH, '//a[text()="Рейтинги"]')
    # кнопка "Что почитать"
    loc_top_toread = (By.XPATH, '//a[text()="Что почитать: выбор редакции"]')
    # кнопка "Принять"
    loc_accept_cookies_btn = (By.CLASS_NAME, 'cookie-policy__button')
# всплывающие окна
    # "Отложено"
    loc_pop_up_window_putorder = (By.XPATH, '//div[@class="b-menu-list-title font_regular tac"]')
    # "Мой лабиринт"
    loc_pop_up_window_my_labirint = (By.CLASS_NAME, "b-header-login-action-logo-e-wrap")
    # "Корзина"
    loc_pop_up_window_cart = (By.XPATH, '//li//div[@class="b-basket-popinfo-e-block b-basket-empty"]')
    # "Сообщения"
    loc_pop_up_window_messages = (By.XPATH, '//div[@class="b-header-login-e-enter"]/div[@class="b-menu-list-title font_regular"]')
    # "Позвонить"
    loc_pop_up_window_call = (By.XPATH, '//li[@class="b-header-b-personal-e-list-item b-header-b-personal-e-list-item-m-sm first-child have-dropdown"]/div/div[@class="popup-window-content b-basket-popinfo"]')
    # "Оформить"
    loc_pop_up_window_check_out = (By.XPATH, '//div[@class="popup-window top-block-popup basket-popup b-basket-info-popup"]')
    # "Оформить"
    loc_pop_up_window_btn_check_out = (By.XPATH, '//div[@class="b-basket-popinfo-e-text-row"]/a[text()="Оформить"]')
#верхнее меню
    # пункт КНИГИ
    loc_menu_books = (By.XPATH, '/html/body/div[1]/div[5]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[1]/span/a')
    # пункт КАНЦТОВАРЫ
    loc_menu_office = (By.XPATH, '/html/body/div[1]/div[5]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[5]/span/a')
    # пункт СЕРТИФИКАТЫ
    loc_menu_certificates = (By.XPATH, '/html/body/div[1]/div[5]/div[5]/div/div[2]/div/ul/li[2]/a')
#иконка соцсетей
    loc_social = (By.CLASS_NAME, "b-header-b-social-e-icon")
#другие локаторы
    # регистрация
    loc_registration_form_my_labirint = (By.CLASS_NAME, "lab-modal-content")
    # фото книг в "Корзине"
    loc_cart_page_books_img = (By.XPATH, '//span[@class="relative"]/img')
    # авторизация
    loc_authorization_window = (By.CLASS_NAME, 'lab-modal-content')
    # email или телефон
    loc_access_input_field = (By.XPATH, '//input[@autocomplete="code tel email phone phones telephone mail"]')
    # кнопка "Войти"
    loc_access_btn_login = (By.ID, 'g-recap-0-btn')
    # комментарий
    loc_access_input_field_comment = (By.XPATH, '//span[@data-default-text="Найдем вас в Лабиринте или зарегистрируем"]')
    # комментарий
    loc_access_input_field_comment_enter = (By.XPATH, '//small[text()="Введенного кода не существует"]')
    # комментарий
    loc_access_btn_login_comment_call = (By.XPATH, '//small[text()="В течение 1 минуты на "]/span[@class="js-replace-phone"]')
    # кнопка ВЛЕВО в разделе ЛУЧШАЯ ПОКУПКА ДНЯ
    loc_btn_left = (By.CLASS_NAME, "swipe-arrow-left")
    # кнопка ВПРВО в разделе ЛУЧШАЯ ПОКУПКА ДНЯ
    loc_btn_right = (By.CLASS_NAME, "swipe-arrow-right")
    #пункты самовывоза
    loc_maps = (By.XPATH, '/html/body/div[1]/div[5]/div[4]/div/div[2]/div/ul/li[11]/a')




