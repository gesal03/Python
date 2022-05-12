import smtplib
from email.message import EmailMessage
import imghdr # 이미지 확장자명 알아서 체크해줌
import re #유효성 검사

SMTP_SEVER = "smtp.gmail.com"
SMTP_PORT = 465

# 유효성 검사
def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

# MIME
message = EmailMessage()
message["Subject"] = "테스트"
message["From"] = "gesal03@hansung.ac.kr"
#message["To"] = "wlgus7040@naver.com"
message["To"] = "gesal03@naver.com"

# 본문 내용 txt 파일에서 가져오기
with open("text.txt", "r") as text:
    data = text.read()
message.set_content(data)

# 이미지 파일 첨부
with open("jihyun.JPG", "rb") as img:
    img_file = img.read()
img_type = imghdr.what("jihyun",img_file)
message.add_attachment(img_file,maintype = 'image', subtype = img_type)

# 메일 전송(SMTP)
smtp = smtplib.SMTP_SSL(SMTP_SEVER, SMTP_PORT)
smtp.login("gesal03@hansung.ac.kr", "hs175459!")
sendEmail(message["To"])
smtp.quit()