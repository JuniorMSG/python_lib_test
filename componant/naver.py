import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from email.mime.text import MIMEText
import smtplib
import componant.keyboard_event as key_event
import time

sendEmail = "converse3519@naver.com"
recvEmail = "milk6645@naver.com"
password = "(123Asdzxc)"
subject = """ 스마트 스토어 kimsland 메일 """
text = """
    구매해 주셔서 감사합니다
    자주 들어와 주세요
    https://smartstore.naver.com/kimsland " <- 이렇게 만 해주세용
"""


def naver_login(driver):
    user_id = 'converse3519@naver.com'
    password = '(123Asdzxc)'
    key_event.elem_push_text(driver.find_element_by_xpath('//*[@id="id"]'), user_id)
    key_event.elem_push_text(driver.find_element_by_xpath('//*[@id="pw"]'), password)

    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/ul/li/div/div[7]').click()

    time.sleep(3)


def sand_naver_email(sendEmail, password, recvEmail,  subject, text):

    smtp_name = "smtp.naver.com" #smtp 서버 주소
    smtp_port = 587 #smtp 포트 번호
    msg = MIMEText(text) #MIMEText(text , _charset = "utf8")

    msg['Subject'] = subject
    msg['From'] = sendEmail
    msg['To'] = recvEmail
    print(msg.as_string())

    s = smtplib.SMTP(smtp_name, smtp_port ) #메일 서버 연결
    s.starttls() # TLS 보안 처리
    s.login( sendEmail , password ) #로그인
    s.sendmail( sendEmail, recvEmail, msg.as_string() ) #메일 전송, 문자열로 변환하여 보냅니다.
    s.close() #smtp 서버 연결을 종료합니다.

    time.sleep(1)


if __name__ == "__main__":
    print(__name__)
    sand_naver_email(sendEmail, password, recvEmail,  subject, text)