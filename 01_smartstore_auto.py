from selenium import webdriver
import componant.webDriver as wd
import componant.keyboard_event as key_event

import time

driver = ''


def naver_login(driver):
    user_id = ''
    password = ''

    key_event.elem_push_text(driver.find_element_by_xpath('//*[@id="id"]'), user_id)
    key_event.elem_push_text(driver.find_element_by_xpath('//*[@id="pw"]'), password)

    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/ul/li/div/div[7]').click()

    time.sleep(3)

try:
    driver = wd.load_chrome_driver()

    main_url = 'https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsell.smartstore.naver.com%2F%23%2FnaverLoginCallback%3Furl%3Dhttps%253A%252F%252Fsell.smartstore.naver.com%252F%2523'
    driver.get(main_url)

    naver_login(driver)
    time.sleep(3)

    driver.get('https://sell.smartstore.naver.com/o/v3/n/sale/delivery?summaryInfoType=DELIVERY_READY')
    time.sleep(3)

    while True:
        try:

            check_box_elem = '//*[@id="__app_root__"]/div/div[2]/div[4]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/table/tbody/tr/th[1]/div/label/span'
            elem = driver.find_element_by_xpath(check_box_elem)
            elem.click()

            time.sleep(3)
            sand_push = driver.find_element_by_xpath('//*[@id="__app_root__"]/div/div[2]/div[4]/div[2]/button[2]/span')
            time.sleep(3)
            sand_push.click()
            time.sleep(3)

            wd.alert_accept_free(driver)
            time.sleep(3)

            driver.switch_to_window(driver.window_handles[0])
            driver.refresh()
            time.sleep(10)
        except:
            time.sleep(10)
            driver.refresh()

    # driver.back()
    # driver.forward()
    # driver.refresh()

    # handles = driver.window_handles
    # size = len(handles)
    # main_handle = driver.current_window_handle
    # for x in range(size):
    #     if handles[x] != main_handle:
    #         driver.switch_to_window(handles[x])
    #         driver.close()

    """
    driver.navegate().to("URL")

	해당 URL로 이동
        driver.switch_to.window(window_handle)

	해당 윈도우 핸들로 이동
driver.current_window_handle

	현재 페이지의 윈도우 핸들을 얻는다
len(driver.window_handles)

	현재 활성화되어있는 탭 또는 창
driver.find_element_by_link_text("new window").click()

	"new window"라는 링크 텍스트를 클릭
    """


except Exception as e:
    driver.quit()