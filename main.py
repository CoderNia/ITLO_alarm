import telegram, requests, time, os
from datetime import datetime
from bs4 import BeautifulSoup

Token = "1287373770:AAEJ9eaESQE2rXc_Q9smmpojdxSXhZ1ggio"
bot = telegram.Bot(token=Token)
chat_id="894538311"
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    # 제일 최신 게시글의 번호 저장
    latest_num = 0
    while True:
        now_time = datetime.now()
        now_time_str = str("{}-{}-{} {}:{}:{}".format(now_time.year, now_time.month, now_time.day, now_time.hour, now_time.minute, now_time.second))
        req = requests.get('http://www.itlo.org/booking')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find("div", {"class" : "col-xs-12 col-md-6 col-lg-3 cropbkiddata"}) #최신 게시글의 번호를 저장하자
        post_num = posts.attrs['data-bkid']


        # 제일 최신 게시글 번호와 30초 마다 크롤링한 첫번째 게시글의 번호 비교
        # 비교 후 같지 않으면 최신 게시글 업데이트 된 것으로 텔레그램 봇으로 업데이트 메시지 전송
        if latest_num != post_num :
            latest_num = post_num
            link = 'http://www.itlo.org/bookingd?id='+post_num
            title = posts.find("font").text
            text = '<ITLO 점자도서관 업데이트>'+'\n'+now_time_str+'\n'+post_num+'\n'+title+'\n'+link
            bot.sendMessage(chat_id, text)
            # 프롬프트 로그
        time.sleep(30) # 30초 간격으로 크롤링
        print("Scrapped time : {}-{}-{} {}:{}:{}".format(now_time.year, now_time.month, now_time.day, now_time.hour, now_time.minute, now_time.second))
        print('Activating : current_number = ' + latest_num)