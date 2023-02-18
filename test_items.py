from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

def test_user_see_button(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements(By.CSS-SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"), 'button is not found'

