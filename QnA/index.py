
total_list = []

while True:
    ques = input("질문을 입력해주세요: ")
    if ques == 'q':
        break
    total_list.append({"질문": ques, "답변": ""})

print("\n======================================================\n")

for i in total_list:
    print(i["질문"])
    ans = input(">> 답변을 입력해주세요: ")
    if ans == 'q':
        break
    i["답변"] = ans

print("결과: ", total_list)