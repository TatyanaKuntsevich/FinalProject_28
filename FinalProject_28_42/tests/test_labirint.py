from pages.auth_page import AuthPage
from tests.test_base import BaseTest
from config import TestData
from pages.locators import Locators

# ****************** ТЕСТЫ ПОИСКА **************************

class TestSearch(BaseTest):

   #1
   def test_1_text(self):
      """поиск произвольного текста, только символы"""
      self.authPage = AuthPage(self.driver)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.text_text)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      search_url = self.authPage.get_url()
      assert TestData.text_search in search_url
      assert self.authPage.text_are_present_in_element(Locators.loc_title_search_result, TestData.text_text)
      earch_books = self.authPage.all_elements_are_presents(Locators.loc_search_books)
      assert len(earch_books) > 0

   #2
   def test_1_2_search(self):
      """удаление предыдущего поиска и ввод нового"""
      self.authPage = AuthPage(self.driver)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.text_1)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      assert self.authPage.text_are_present_in_element(Locators.loc_title_search_result, TestData.text_1)
      search_books_1 = self.authPage.all_elements_are_presents(Locators.loc_search_books)
      assert len(search_books_1) > 0
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.text_2)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      assert self.authPage.text_are_present_in_element(Locators.loc_title_search_result, TestData.text_2)
      search_books_2 = self.authPage.all_elements_are_presents(Locators.loc_search_books)
      assert len(search_books_2) > 0

   #3
   def test_not_field(self):
      """по пустоу полю поиска нет"""
      self.authPage = AuthPage(self.driver)
      self.authPage.clear_field(Locators.loc_search_field)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      search_url = self.authPage.get_url()
      assert search_url == TestData.start_page

   #4
   def test_symbols_long(self):
      """большое количество символов"""
      self.authPage = AuthPage(self.driver)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.symbol_long)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      search_url = self.authPage.get_url()
      assert TestData.text_search in search_url

   #5
   def test_symbol_special(self):
      """спец.символы"""
      self.authPage = AuthPage(self.driver)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.symbol_special)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      search_url = self.authPage.get_url()
      assert TestData.text_search in search_url

   #6
   def test_author_1(self):
      """автор на русском языке, определенная книга по ID"""
      self.authPage = AuthPage(self.driver)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.name_rus)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      assert self.authPage.text_are_present_in_element(Locators.loc_title_search_result, TestData.name_rus)
      search_books = self.authPage.all_elements_are_presents(Locators.loc_search_books)
      total_number_search_books = int((self.authPage.element_are_present(Locators.loc_total_number_search_books).text).replace(" ", ""))
      if int(total_number_search_books) % len(search_books) > 0:
         total_pages_search_books = int(int(total_number_search_books) / len(search_books)) + 1
      else:
         total_pages_search_books = int(int(total_number_search_books) / len(search_books))
      for i in range(total_pages_search_books):
         if self.authPage.elements_find_true(Locators.loc_my_book):
            break
         else:
            self.authPage.click_element(Locators.loc_search_btn_next_page)
      assert self.authPage.elements_find(Locators.loc_my_book), 'Поиск не находит книгу'.format(TestData.name_rus)
      my_book = self.authPage.element_are_present(Locators.loc_my_book)
      assert my_book.is_displayed()

   #7
   def test_author_2(self):
      """автор на русском языке, любая книга"""
      self.authPage = AuthPage(self.driver)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.name_rus)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      assert self.authPage.text_are_present_in_element(Locators.loc_title_search_result, TestData.name_rus)

   #8
   def test_author_3(self):
      """автор на английском языке, определенная книга по ID"""
      self.authPage = AuthPage(self.driver)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.name_eng)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      assert self.authPage.text_are_present_in_element(Locators.loc_title_search_result, TestData.name_eng)
      search_books = self.authPage.all_elements_are_presents(Locators.loc_search_books)
      TOTAL_NUMBER_SEARCH_BOOKS = int(
         (self.authPage.element_are_present(Locators.loc_total_number_search_books).text).replace(" ", ""))
      if int(TOTAL_NUMBER_SEARCH_BOOKS) % len(search_books) > 0:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books)) + 1
      else:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books))
      for i in range(total_pages_search_books):
         if self.authPage.elements_find_true(Locators.loc_my_book):
            break
         else:
            self.authPage.click_element(Locators.loc_search_btn_next_page)
      assert self.authPage.elements_find(Locators.loc_my_book), 'Поиск не находит книгу'.format(TestData.name_eng)
      my_book = self.authPage.element_are_present(Locators.loc_my_book)
      assert my_book.is_displayed()

   #9
   def test_author_4(self):
      """автор на английском языке, любая книга"""
      self.authPage = AuthPage(self.driver)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.name_eng)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      assert self.authPage.text_are_present_in_element(Locators.loc_title_search_result, TestData.name_eng)

   #10
   def test_book_1(self):
      """название книги на русском языке"""
      self.authPage = AuthPage(self.driver)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.book_rus)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      assert self.authPage.text_are_present_in_element(Locators.loc_title_search_result, TestData.book_rus)

   #11
   def test_book_2(self):
      """названию книги на английском языке"""
      self.authPage = AuthPage(self.driver)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.book_eng)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      assert self.authPage.text_are_present_in_element(Locators.loc_title_search_result, TestData.book_eng)

   #12
   def test_history(self):
      """история поиска"""
      self.authPage = AuthPage(self.driver)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.name_rus)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.book_rus)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      self.authPage.hover_cursor_click(Locators.loc_logo)
      assert self.authPage.element_invisibility(Locators.loc_pop_up_search_field_3)
      self.authPage.hover_cursor_click(Locators.loc_search_field)
      assert self.authPage.element_are_present(Locators.loc_pop_up_search_field_3)
      history = self.authPage.element_are_present(Locators.loc_pop_up_search_field_3)
      assert history.is_displayed()

   #13
   def test_2_text(self):
      """поиск произвольного текста, символы и цифры"""
      self.authPage = AuthPage(self.driver)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.text_text_2)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      search_url = self.authPage.get_url()
      assert TestData.text_search in search_url
      assert self.authPage.text_are_present_in_element(Locators.loc_title_search_result, TestData.text_text)
      earch_books = self.authPage.all_elements_are_presents(Locators.loc_search_books)
      assert len(earch_books) > 0

   # 14
   def test_3_text(self):
      """поиск по ID """
      self.authPage = AuthPage(self.driver)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.text_ID)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      assert self.authPage.text_are_present_in_element(Locators.loc_title_search_result, TestData.text_ID)

   # 15
   def test_4_text(self):
      """поиск по ISBN """
      self.authPage = AuthPage(self.driver)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.text_ISBN)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      assert self.authPage.text_are_present_in_element(Locators.loc_title_search_result, TestData.text_ISBN)

   # 16
   def test_5_text(self):
      """поиск по жанру """
      self.authPage = AuthPage(self.driver)
      self.authPage.click_clear_send_text(Locators.loc_search_field, TestData.text_long)
      self.authPage.hover_cursor_click(Locators.loc_icon_search_field)
      assert self.authPage.text_are_present_in_element(Locators.loc_title_search_result, TestData.text_long)


# ****************** ТЕСТЫ ВХОДА ***************************

class TestAuthor(BaseTest):

   #1
   def test_email_correct(self):
      self.authPage = AuthPage(self.driver)
      self.authPage.hover_cursor_click(Locators.loc_header_button_my_labirint)
      assert self.authPage.element_visibility(Locators.loc_authorization_window)
      btn_login = self.authPage.element_find(Locators.loc_access_btn_login)
      assert  btn_login.is_enabled() == False
      self.authPage.clear_field(Locators.loc_access_input_field)
      self.authPage.send_text_1(Locators.loc_access_input_field, TestData.email)
      assert btn_login.is_enabled

   #2
   def test_email_failed(self):
      self.authPage = AuthPage(self.driver)
      self.authPage.hover_cursor_click(Locators.loc_header_button_my_labirint)
      assert self.authPage.element_visibility(Locators.loc_authorization_window)
      btn_login = self.authPage.element_find(Locators.loc_access_btn_login)
      assert  btn_login.is_enabled() == False
      self.authPage.clear_field(Locators.loc_access_input_field)
      self.authPage.send_text_1(Locators.loc_access_input_field, TestData.email_incorrect)
      assert btn_login.is_enabled

   #3
   def test_symbol_special(self):
      self.authPage = AuthPage(self.driver)
      self.authPage.hover_cursor_click(Locators.loc_header_button_my_labirint)
      assert self.authPage.element_visibility(Locators.loc_authorization_window)
      self.authPage.clear_field(Locators.loc_access_input_field)
      self.authPage.send_text_1(Locators.loc_access_input_field, TestData.symbol_special)
      access_input_field_comment = self.authPage.get_element_text(Locators.loc_access_input_field_comment)
      assert TestData.com_symbol in access_input_field_comment

   #4
   def test_min_str(self):
      self.authPage = AuthPage(self.driver)
      self.authPage.hover_cursor_click(Locators.loc_header_button_my_labirint)
      assert self.authPage.element_visibility(Locators.loc_authorization_window)
      btn_login = self.authPage.element_find(Locators.loc_access_btn_login)
      assert btn_login.is_enabled() == False
      self.authPage.clear_field(Locators.loc_access_input_field)
      assert btn_login.is_enabled() == False
      i = 0
      while btn_login.is_enabled() == False:
         self.authPage.send_text_1(Locators.loc_access_input_field, TestData.number)
         i += 1
      assert btn_login.is_enabled
      assert i == TestData.min_str

   #5
   def test_str_eng(self):
      self.authPage = AuthPage(self.driver)
      self.authPage.hover_cursor_click(Locators.loc_header_button_my_labirint)
      assert self.authPage.element_visibility(Locators.loc_authorization_window)
      btn_login = self.authPage.element_find(Locators.loc_access_btn_login)
      assert btn_login.is_enabled() == False
      self.authPage.clear_field(Locators.loc_access_input_field)
      assert btn_login.is_enabled() == False
      i = 0
      while btn_login.is_enabled() == False:
         self.authPage.send_text_1(Locators.loc_access_input_field, TestData.str_eng)
         i += 1
      assert btn_login.is_enabled
      assert i == TestData.min_letters

   #6
   def test_str_rus(self):
     self.authPage = AuthPage(self.driver)
     self.authPage.hover_cursor_click(Locators.loc_header_button_my_labirint)
     assert self.authPage.element_visibility(Locators.loc_authorization_window)
     btn_login = self.authPage.element_find(Locators.loc_access_btn_login)
     assert btn_login.is_enabled() == False
     self.authPage.clear_field(Locators.loc_access_input_field)
     assert btn_login.is_enabled() == False
     j = 0
     while btn_login.is_enabled() == False:
        self.authPage.send_text_1(Locators.loc_access_input_field, TestData.str_rus)
        j += 1
     assert BTN_LOGIN.is_enabled
     assert j == TestData.min_letters

 #7
   def test_none(self):
      self.authPage = AuthPage(self.driver)
      self.authPage.hover_cursor_click(Locators.loc_header_button_my_labirint)
      assert self.authPage.element_visibility(Locators.loc_authorization_window)
      btn_login = self.authPage.element_find(Locators.loc_access_btn_login)
      assert btn_login.is_enabled() == False
      self.authPage.clear_field(Locators.loc_access_input_field)
      self.authPage.send_text_1(Locators.loc_access_input_field, TestData.email_none)
      assert btn_login.is_enabled

# ****************** ТЕСТЫ ГЛАВНОЙ СТРАНИЦЫ **************

class TestStart(BaseTest):

   #1
   def test_btn_labirint_1(self):
      """нажатие на ЛАБИРИНТ из разных страниц"""
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(Locators.loc_logo)
      logo = self.authPage.element_are_present(Locators.loc_logo)
      assert logo.is_displayed()
      self.authPage.hover_cursor_click(Locators.loc_logo)
      logo_page = self.authPage.get_url()
      assert logo_page == TestData.start_page
      self.authPage.hover_cursor_click(Locators.loc_header_button_putorder)
      putorder_page = self.authPage.get_url()
      assert putorder_page == TestData.putorder_page
      self.authPage.hover_cursor_click(Locators.loc_logo)
      logo_page = self.authPage.get_url()
      assert logo_page == TestData.start_page
      self.authPage.hover_cursor_click(Locators.loc_header_button_cart)
      cart_page = self.authPage.get_url()
      assert cart_page == TestData.cart_page
      self.authPage.hover_cursor_click(Locators.loc_logo)
      logo_page = self.authPage.get_url()
      assert logo_page == TestData.start_page
      self.authPage.hover_cursor_click(Locators.loc_logo)
      logo_page = self.authPage.get_url()
      assert logo_page == TestData.start_page
      self.authPage.hover_cursor_click(Locators.loc_header_button_rating)
      rating = self.authPage.get_url()
      assert rating == TestData.rating_page
      self.authPage.hover_cursor_click(Locators.loc_logo)
      logo_page = self.authPage.get_url()
      assert logo_page == TestData.start_page
      self.authPage.hover_cursor_click(Locators.loc_top_toread)
      toread = self.authPage.get_url()
      assert toread == TestData.top_page
      self.authPage.hover_cursor_click(Locators.loc_logo)
      logo_page = self.authPage.get_url()
      assert logo_page == TestData.start_page

   # 2
   def test_btn_my_labirint_vid(self):
      """видимость кнопки "Мой лабиринт"""
      self.authPage = AuthPage(self.driver)
      my_labirint = self.authPage.element_are_present(Locators.loc_header_button_my_labirint)
      assert my_labirint.is_displayed(), "Элемент не виден при заданной ширине"

   # 3
   def test_btn_my_labirint(self):
      """нажатие кнопки "Мой лабиринт"""
      self.authPage = AuthPage(self.driver)
      my_labirint = self.authPage.element_are_present(Locators.loc_header_button_my_labirint)
      self.authPage.hover_cursor_click(Locators.loc_header_button_my_labirint)
      registration = self.authPage.element_are_present(Locators.loc_registration_form_my_labirint)
      assert registration.is_displayed(), "Элемент не виден"
      assert self.authPage.text_are_present_in_element(Locators.loc_registration_form_my_labirint,"Полный доступ к Лабиринту")

   # 4
   def test_btn_1(self):
      """кнопка "Корзина"""
      self.authPage = AuthPage(self.driver)
      check_out = self.authPage.element_are_present(Locators.loc_pop_up_window_check_out)
      assert check_out.is_displayed() == False

   # 5
   def test_btn_2(self):
      """видимость кнопки "Корзина" """
      self.authPage = AuthPage(self.driver)
      header_button_cart = self.authPage.element_are_present(Locators.loc_header_button_cart)
      assert header_button_cart.is_displayed(), "Элемент не виден при заданной ширине"

   # 6
   def test_btn_3(self):
      """кнопка "Сообщения" открывает 'Полный доступ к Лабиринту'"""
      self.authPage = AuthPage(self.driver)
      button_messages = self.authPage.element_are_present(Locators.loc_header_button_messages)
      assert button_messages.is_displayed(), "Элемент не виден при заданной ширине"
      self.authPage.hover_cursor_click(Locators.loc_header_button_messages)
      form_my_labirint = self.authPage.element_are_present(Locators.loc_registration_form_my_labirint)
      assert form_my_labirint.is_displayed(), "Элемент не виден"
      assert self.authPage.text_are_present_in_element(Locators.loc_registration_form_my_labirint, "Полный доступ к Лабиринту")

   # 7
   def test_btn_4(self):
      """видимость кнопки "Отложено"""
      self.authPage = AuthPage(self.driver)
      putorder = self.authPage.element_are_present(Locators.loc_header_button_putorder)
      assert putorder.is_displayed(), "Элемент не виден при заданной ширине"

   # 8
   def test_btn_5(self):
      """избранное"""
      self.authPage = AuthPage(self.driver)
      favourites = self.authPage.all_elements_are_presents(Locators.loc_start_page_books_favourites)
      self.authPage.scroll_to_element(favourites[0])
      self.authPage.hover_cursor_click(Locators.loc_start_page_books_favourites)
      putorder = self.authPage.element_are_present(Locators.loc_header_button_putorder)
      self.authPage.scroll_to_element(putorder)
      self.authPage.hover_cursor_click(Locators.loc_header_button_putorder)
      putorder_page = self.authPage.get_url()
      assert putorder_page == TestData.putorder_page

   # 9
   def test_btn_img_1(self):
      """кнопка и иконка "Мой Лабиринт"""
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(Locators.loc_header_button_my_labirint), "Элемент отсутствует"
      assert self.authPage.element_are_present(Locators.loc_header_button_icons_my_labirint), "Иконка отсутствует"
      my_labirint = self.authPage.element_are_present(Locators.loc_header_button_my_labirint)
      icons_my_labirint = self.authPage.element_are_present(Locators.loc_header_button_icons_my_labirint)
      assert my_labirint.is_displayed(), "Элемент не виден на дисплее при заданной ширине"
      assert icons_my_labirint.is_displayed(), "Элемент не виден на дисплее при заданной ширине"

   # 10
   def test_btn_img_2(self):
      """кнопка и иконока "Позвонить" """
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(Locators.loc_header_button_call), "Элемент отсутствует"
      assert self.authPage.element_are_present(Locators.loc_header_button_icons_call), "Иконка отсутствует"

   #11
   def test_btn_img_3(self):
      """кнопка и иконка "Отложено"""
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(Locators.loc_header_button_putorder), "Элемент отсутствует"
      assert self.authPage.element_are_present(Locators.loc_header_button_icons_putorder), "Иконка отсутствует"
      button_putorder = self.authPage.element_are_present(Locators.loc_header_button_putorder)
      icons_putorder = self.authPage.element_are_present(Locators.loc_header_button_icons_putorder)
      assert button_putorder.is_displayed(), "Элемент не виден при заданной ширине"
      assert icons_putorder.is_displayed(), "Элемент не виден при заданной ширине"

   # 12
   def test_btn_img_4(self):
      """кнопка и иконка "Корзина" """
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(Locators.loc_header_button_cart), "Элемент отсутствует"
      assert self.authPage.element_are_present(Locators.loc_header_button_icons_cart), "Иконка отсутствует"
      button_cart = self.authPage.element_are_present(Locators.loc_header_button_cart)
      icons_cart = self.authPage.element_are_present(Locators.loc_header_button_icons_cart)
      assert button_cart.is_displayed(), "Элемент не виден при заданной ширине"
      assert icons_cart.is_displayed(), "Элемент не виден при заданной ширине"

   # 13
   def test_btn_img_5(self):
      """кнопка и иконка "Сообщения" """
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(Locators.loc_header_button_messages), "Элемент отсутствует"
      assert self.authPage.element_are_present(Locators.loc_header_button_icons_messages), "Элемент отсутствует"
      button_messages = self.authPage.element_are_present(Locators.loc_header_button_messages)
      icons_messages = self.authPage.element_are_present(Locators.loc_header_button_icons_messages)
      assert button_messages.is_displayed(), "Элемент не виден при заданной ширине"
      assert icons_messages.is_displayed(), "Элемент не виден при заданной ширине"

   # 14
   def test_w_1(self):
      """всплывающее окно для СООБЩЕНИЯ"""
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(Locators.loc_pop_up_window_messages)
      window_messages = self.authPage.element_are_present(Locators.loc_pop_up_window_messages)
      assert window_messages.is_displayed() == False
      self.authPage.hover_cursor(Locators.loc_header_button_messages)
      assert window_messages.is_displayed()

   #15
   def test_w_2(self):
      """всплывающее окно для ПОЗВОНИТЬ"""
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(Locators.loc_pop_up_window_call)
      POP_UP_WIcallNDOW_CALL = self.authPage.element_are_present(Locators.loc_pop_up_window_call)
      assert call.is_displayed() == False

   #16
   def test_w_3(self):
      """всплывающее окно для ОТЛОЖЕНО"""
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(Locators.loc_pop_up_window_putorder)
      window_putorder = self.authPage.element_are_present(Locators.loc_pop_up_window_putorder)
      assert window_putorder.is_displayed() == False
      self.authPage.hover_cursor(Locators.loc_pop_up_window_putorder)
      assert window_putorder.is_displayed()

   # 17
   def test_w_4(self):
      """всплывающее окно для КОРЗИНЫ"""
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(Locators.loc_pop_up_window_cart)
      cart = self.authPage.element_are_present(Locators.loc_pop_up_window_cart)
      assert cart.is_displayed() == False
      self.authPage.hover_cursor(Locators.loc_header_button_cart),
      assert cart.is_displayed()

   # 18
   def test_w_5(self):
      """всплывающее окно для МОЙ ЛАБИРИНТ"""
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(Locators.loc_pop_up_window_my_labirint)
      my_labirint = self.authPage.element_are_present(Locators.loc_pop_up_window_my_labirint)
      assert my_labirint.is_displayed() == False
      self.authPage.hover_cursor(Locators.loc_header_button_my_labirint)
      assert my_labirint.is_displayed()

   #19
   def test_start_page_books(self):
      """на главной странице есть товары """
      self.authPage = AuthPage(self.driver)
      start_books = self.authPage.all_elements_are_presents(Locators.loc_start_books)
      assert len(start_books) > 0

   # 20
   def test_btn_tel(self):
      """кнопка "Позвонить" """
      self.authPage = AuthPage(self.driver)
      button_call = self.authPage.element_are_present(Locators.loc_header_button_call)
      assert button_call.is_displayed(), "Элемент не виден при заданной ширине"
      self.authPage.hover_cursor_click(Locators.loc_header_button_call)
      call_page = self.authPage.get_url()
      assert call_page == TestData.call_page

   # 21
   def test_menu_books(self):
      """пункт меню КНИГИ """
      self.authPage = AuthPage(self.driver)
      menu_books = self.authPage.element_are_present(Locators.loc_menu_books)
      assert menu_books.is_displayed(), "Элемент не виден при заданной ширине"
      self.authPage.hover_cursor_click(Locators.loc_menu_books)
      menu_books_click = self.authPage.get_url()
      assert menu_books_click == TestData.menu_books_click

   # 22
   def test_menu_office(self):
      """пункт меню КАНЦТОВАРЫ """
      self.authPage = AuthPage(self.driver)
      menu_office = self.authPage.element_are_present(Locators.loc_menu_office)
      assert menu_office.is_displayed(), "Элемент не виден при заданной ширине"
      self.authPage.hover_cursor_click(Locators.loc_menu_office)
      menu_office_click = self.authPage.get_url()
      assert menu_office_click == TestData.menu_office_click

   # 23
   def test_menu_certificates(self):
      """пункт меню СЕРТИФИКАТЫ """
      self.authPage = AuthPage(self.driver)
      self.authPage.hover_cursor_click(Locators.loc_menu_certificates)
      menu_certificates = self.authPage.get_url()
      assert menu_certificates == TestData.menu_certificates_click

   #24
   def test_social(self):
      """виден пункт в соцсетях """
      self.authPage = AuthPage(self.driver)
      social = self.authPage.element_are_present(Locators.loc_social)
      assert social.is_displayed(), "Элемент не виден при заданной ширине"

   # 25
   def test_left(self):
      """кнопка ВЛЕВО в разделе ЛУЧШАЯ ПОКУПКА ДНЯ  """
      self.authPage = AuthPage(self.driver)
      btn_left = self.authPage.element_are_present(Locators.loc_btn_left)
      assert btn_left.is_displayed(), "Элемент не виден при заданной ширине"
      self.authPage.hover_cursor_click(Locators.loc_btn_left)
      btn_lefе_click = self.authPage.get_url()
      assert btn_lefе_click == TestData.start_page

   # 26
   def test_right(self):
      """кнопка ВПРАВО в разделе ЛУЧШАЯ ПОКУПКА ДНЯ  """
      self.authPage = AuthPage(self.driver)
      btn_right = self.authPage.element_are_present(Locators.loc_btn_right)
      assert btn_right.is_displayed(), "Элемент не виден при заданной ширине"
      self.authPage.hover_cursor_click(Locators.loc_btn_right)
      btn_right_click = self.authPage.get_url()
      assert btn_right_click == TestData.start_page

 # 27
   def test_maps(self):
      """ пункты самовывоза"""
      self.authPage = AuthPage(self.driver)
      btn_maps = self.authPage.element_are_present(Locators.loc_maps)
      assert btn_maps.is_displayed(), "Элемент не виден при заданной ширине"
      self.authPage.hover_cursor_click(Locators.loc_maps)
      btn_maps_click = self.authPage.get_url()
      assert btn_maps_click == TestData.maps