import smtplib
from email.message import EmailMessage
import re
import requests
import json
import schedule
import time
import datetime
import sys

SMTP_SEVER = "smtp.gmail.com"
SMTP_PORT = 465

city = "Seoul"
apikey = "f364fe04309916af0a2d56f4d0908ab2"
lang = "kr"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric" #f-string

# MIME
message = EmailMessage()
message["Subject"] = "테스트"
message["From"] = "gesal03@hansung.ac.kr"
#message["To"] = "wlgus7040@naver.com"
message["To"] = "gesal03@naver.com"

def mail():

    result = requests.get(api)
    data = json.loads(result.text)
    now = datetime.datetime.now()

    with open("text.txt", "w") as text:
        text.write("====================" + str(now) + "기준 ==========================\n")
        text.write(data["name"] + "의 날씨입니다.\n")
        text.write("날씨는 " + data["weather"][0]["description"] + "입니다.\n")
        text.write("온도는 " + str(data["main"]["temp"]) + "입니다.\n")
        text.write("체감온도는 " + str(data["main"]["feels_like"]) + "입니다.\n")
        text.write("최저 기온은 " + str(data["main"]["temp_min"]) + "입니다.\n")
        text.write("최고 기온은 " + str(data["main"]["temp_max"]) + "입니다.\n")
        text.write("습도는 " + str(data["main"]["humidity"]) + "입니다.\n")
        text.write("기압은 " + str(data["main"]["pressure"]) + "입니다.\n")
        text.write("풍향은 " + str(data["wind"]["deg"]) + "입니다.\n")
        text.write("풍속은 " + str(data["wind"]["speed"]) + "입니다.\n")

    # 본문 내용 txt 파일에서 가져오기
    with open("text.txt", "r") as text:
        data = text.read()
    message.set_content(data)

    # 유효성 검사
    def sendEmail(addr):
        reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
        if bool(re.match(reg, addr)):
            smtp.send_message(message)
            print("정상적으로 메일이 발송되었습니다.")
        else:
            print("유효한 이메일 주소가 아닙니다.")

    # 메일 전송(SMTP)
    smtp = smtplib.SMTP_SSL(SMTP_SEVER, SMTP_PORT)
    smtp.login("gesal03@hansung.ac.kr", "hs175459!")
    sendEmail(message["To"])
    smtp.quit()

def exit():
    print("function exit")
    sys.exit()

schedule.every().day.at("16:59").do(mail)
schedule.every().day.at("17:00").do(exit)
while True:
    schedule.run_pending()
    time.sleep(1)