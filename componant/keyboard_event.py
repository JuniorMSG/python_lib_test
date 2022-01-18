from selenium.webdriver.common.keys import Keys
import time
import pyperclip


def elem_push_text(elem, text):
    elem.click()
    pyperclip.copy(text)
    elem.send_keys(Keys.CONTROL, 'v')
    time.sleep(2)
