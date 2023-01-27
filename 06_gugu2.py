num = input("몇 단을 출력할까요?: ")
count = input("몇 개 출력할까요?: ")

for i in range(1, int(count)):
    print(f"{num} * {i} = {int(num) * i}")