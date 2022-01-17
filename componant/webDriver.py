import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


def load_chrome_driver():
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  # 크롬드라이버 버전 확인
    try:
        driver = webdriver.Chrome(f'./rsc/{chrome_ver}/chromedriver.exe')
    except:
        chromedriver_autoinstaller.install(path='./rsc')
        driver = webdriver.Chrome(f'../rsc/{chrome_ver}/chromedriver.exe')

    driver.implicitly_wait(3)
    driver.set_page_load_timeout(3)



    return driver

def alert_accept_free(driver):
    try:
        da = Alert(driver)
        da.accept()

    except Exception as e:
        print("no alert", e)



if __name__ == '__main__':
    load_chrome_driver()