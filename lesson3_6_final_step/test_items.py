import time

def test_add2basket_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(30)  #для визуальной проверки смены языка расскоментировать эту строку
    button_add_to_basket = len(browser.find_elements_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert button_add_to_basket == 1, "Кнопка добавления в корзину есть!" 
