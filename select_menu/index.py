import random
import time

menu = ["된장찌개", "피자", "제육볶음", "짜장면"]


while True:
    print("\n점심 메뉴 후보: ", menu)
    want_menu = input("음식을 추가 해주세요(끝내기 : q): ")
    if want_menu == 'q':
        break
    menu.append(want_menu)

while True:
    print("\n점심 메뉴 후보: ", menu)
    del_menu = input("음식을 삭제해주세요(끝내기 : q): ")
    if del_menu == 'q':
        break
    menu.remove(del_menu)

print("=============================================================")
print(menu, "중에서 선택합니다 !!\n")
for i in range(1,6):
    print(6-i)
    time.sleep(1)
lunch = random.choice(menu)
print("오늟의 메뉴는", lunch, "이다!\n")



