# num = input("숫자를 입력하세요")

# # 짝수면 0, 홀수면 1
# nameoji = int(num) % 2

# # 같으면 참(True), 다르면 거짓(False)
# if nameoji == 0:
#     print(str(num) + "은(는) 2의 배수입니다.")
# else:
#     print(str(num) + "은(는) 2의 배수가 아닙니다.")


num = input("숫자를 입력하세요: ")
divide = input("나눌 값을 입력하세요: ")

# int: 숫자로 바꿔준다.
# str: 문자로 바꿔준다.
nameoji = int(num) % int(divide)
print("나머지 값은 " + str(nameoji) + " 입니다.")