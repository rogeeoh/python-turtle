import time

input("엔터를 누르고 20초를 셉니다.")
start = time.time()

input("20초 후에 다시 엔터를 누릅니다.")
end = time.time()

print(f"{end} - {start}의 차이는 {round(end - start)}초 입니다")