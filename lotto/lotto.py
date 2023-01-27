import random

numbers = []

# numbers가 6개가 될 때까지 반복
while len(numbers) < 6:
    # 숫자를 1~45 사이에서 랜덤으로 뽑아.
    num = random.randint(1, 45)

    # 뽑은 숫자가 이미 numbers 안에 있니?
    if num in numbers:
        # 니가 뽑은 숫자가 이미 있다면, 아무 것도 하지 말고 넘어가.
        continue
    # 뽑은 숫자가 numbers 안에 없다면
    else:
        # numbers 배열에 뽑은 숫자를 추가
        numbers.append(num)

# 정렬하기
numbers.sort()
print(numbers)
