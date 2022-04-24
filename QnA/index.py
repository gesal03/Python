
ques =[]
while True:
    item = input("질문을 입력해주세요: ")
    if item == 'q':
        break
    ques.append(item)
    
print("\n======================================================\n")

dic={}
for key in ques:
    print(key)
    ans = input(">> 답변을 입력해주세요: ")
    if ans == 'q':
        break
    dic[key] = ans

print("결과: ", dic)