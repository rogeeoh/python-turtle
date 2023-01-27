# 사칙연산 + - / *

# 두 개의 숫자를 더해준 값을 리턴
def add(num1, num2):
    return num1 + num2

# 숫자는 0으로 나눌 수 없어.
# 만약 0으로 나눈다면? 0으로 나눌 수 없다는 걸 사용자에게 안내


x = 3
y = 5

result = add(x, y)
print(f"두 숫자를 더한 결과는 {result} 입니다.")