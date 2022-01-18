import componant.webDriver as wd
import componant.naver as naver
import time

driver = ''

try:
    driver = wd.get_driver(False)

    main_url = 'https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsell.smartstore.naver.com%2F%23%2FnaverLoginCallback%3Furl%3Dhttps%253A%252F%252Fsell.smartstore.naver.com%252F%2523'
    driver.get(main_url)

    naver.naver_login(driver)
    time.sleep(3)

    driver.get('https://sell.smartstore.naver.com/o/v3/n/sale/delivery?summaryInfoType=DELIVERY_READY')
    time.sleep(3)

    while True:
        try:

            check_box_elem = '//*[@id="__app_root__"]/div/div[2]/div[4]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/table/tbody/tr/th[1]/div/label/span'
            elem = driver.find_element_by_xpath(check_box_elem)
            elem.click()

            driver.find_element_by_xpath('//*[@id="__app_root__"]/div/div[2]/div[4]/div[4]/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr')

            elem_lst = driver.find_element_by_xpath('//*[@id="__app_root__"]/div/div[2]/div[4]/div[4]/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]/table/tbody').find_elements_by_tag_name('tr')

            mail_id_lst = []
            mail_content_lst = []
            for i, elem in enumerate(elem_lst):
                mail_id_lst.append(elem.find_elements_by_tag_name('td')[8].text + '@naver.com')
                mail_content_lst.append(elem.find_elements_by_tag_name('td')[15].text)

            subject = """ 스마트 스토어 kimsland 메일 """

            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="__app_root__"]/div/div[2]/div[4]/div[2]/button[2]/span').click()
            time.sleep(3)
            wd.escape_alert_message(driver)
            time.sleep(3)

            for data in range(0, len(mail_id_lst)):
                text = """{0}을구매해 주셔서 감사합니다 \n자주 들어와 주세요 \nhttps://smartstore.naver.com/kimsland""".format(mail_content_lst[data])
                naver.sand_naver_email('converse3519@naver.com', '(123Asdzxc)', mail_id_lst[data], subject, text)

            driver.switch_to_window(driver.window_handles[0])
            driver.refresh()
            time.sleep(10)

        except Exception as e:
            print(e)
            time.sleep(10)
            driver.refresh()

except Exception as e:
    driver.quit()


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


