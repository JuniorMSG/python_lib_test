import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

import random
import re
import time

# User-Agent 설정
def get_random_ua():
    all_user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
    ]
    random_ua_index = random.randint(0, len(all_user_agents) - 1)
    ua = re.sub(r"(\s)$", "", all_user_agents[random_ua_index])
    return ua


# 크롬드라이버 환경 설정
def get_driver(open_browser):

    options = webdriver.ChromeOptions()

    if open_browser:
        options.add_argument('headless')

    options.add_argument('window-size=1920x1080')
    options.add_argument('lang=ko_KR')

    # 시크릿모드드
    options.add_argument('--incognito')
    options.add_argument('--no-sandbox')
    # options.add_argument('--disable-setuid-sandbox')

    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('acceptInsecureCerts')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--able-popup-blocking')
    options.add_argument('--log-level=3')
    options.add_argument("disable-gpu")
    options.add_argument("user-agent=" + get_random_ua())

    # enable-automation 자동화 막대 비활성, load-extension 개발자 모드 확장 사용 비활성
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging", "load-extension" ])
    options.add_experimental_option('useAutomationExtension', False)

    # 로그인시 비밀번호창 비활성
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    # 크롬드라이버 버전 확인

    try:
        driver = webdriver.Chrome(f'./rsc/{chrome_ver}/chromedriver.exe')
    except:
        chromedriver_autoinstaller.install(path='./rsc')
        driver = webdriver.Chrome(f'./rsc/{chrome_ver}/chromedriver.exe')

    driver.set_page_load_timeout(30)
    driver.create_options()
    driver.maximize_window()

    return driver


# alert message 탈출
def escape_alert_message(driver):
    try:
        da = Alert(driver)
        da.accept()
        time.sleep(2)
    except Exception as e:
        print("-- alert창 없음 -- ")


# 공용 팝업 닫기
def popup_close(driver):
    # JS View Task
    """
        https://stackoverflow.com/questions/19669786/check-if-element-is-visible-in-dom
    """
    pop_close_script = []

    includes_tag_lst = ["button", "label", "span", "b", 'div']
    includes_text_lst = ["열람하지 않습니다", "열지 않기", "열지않기", "닫기", "close", "Close"]
    text_script = "Array.from(document.querySelectorAll('{0}')).find(elem => elem.textContent.includes('{1}') ? elem.click() : '')"

    for includes_tag in includes_tag_lst:
        for includes_text in includes_text_lst:
            pop_close_script.append(text_script.format(includes_tag, includes_text))

    text_script_attr = "Array.from(document.querySelectorAll('[{0}*={1}]')).find(elem =>!!(elem.offsetWidth || elem.offsetHeight || elem.getClientRects().length) ? elem.click() : '')"
    view_attr_lst = ['data-toggle', 'class', 'id', 'onclick', ]
    view_attr_text_lst = ['close', "Close", "check", "SetCookie", "pop-close"]

    for includes_tag in view_attr_lst:
        for includes_text in view_attr_text_lst:
            pop_close_script.append(text_script_attr.format(includes_tag, includes_text))

    pop_close_script.append("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")
    pop_close_script.append("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})")
    pop_close_script.append("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")

    for script in pop_close_script:
        try:
            driver.execute_script(script)
        except:
            pass


if __name__ == '__main__':
    driver = get_driver(False)
    driver.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B3%B5%EC%9D%B8ip")



