import requests
import datetime

def file_create(req_data, option):
    # 내용
    jsonStr = req_data['jsonStr']

    # 파일경로
    reqFilePath = req_data['filePath']

    # 파일명
    reqFileNm = req_data['fileName']

    if option == 'week':
        today = datetime.date.today()
        today = today + datetime.timedelta(days=-today.weekday(), weeks=0)
        # file_name = today.strftime('%Y-%m-%d') + '(' + str(datetime.datetime.now().isocalendar()[1]) + '주차)' +'_NGCC.txt'
        reqFileNm = '/' + today.strftime('%Y-%m-%d') + '_NGCC.txt'

    f = open(reqFilePath+reqFileNm, mode='w')
    f.write(jsonStr)
    f.close()


def week_kisa_api_data():
    reqKisa = requests.get('http://localhost:5080/cnns/api2/kisaApi.do')
    file_create(reqKisa.json(), 'week')


def month_kisa_api_data():
    # kisa API 호출
    reqKisa = requests.get('http://localhost:5080/cnns/api2/kisaApiMon.do')
    file_create(reqKisa.json(), '')






if __name__ == '__main__':
    week_kisa_api_data()
    month_kisa_api_data()
