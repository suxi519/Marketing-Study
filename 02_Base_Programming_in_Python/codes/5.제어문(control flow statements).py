# 5-1. while 반복문
while 조건 부분:  # 불린 값으로 계산되는 식 ex) x < 3, name == '유재석'
   수행 부분  # 반복적으로 실행하고 싶은 명령 ex) print("나는 예쁘다"), i = i + 1

while 문법 연습
i = 1
while i <= 50:
    print(i * 2)
    i += 1

# 5-2. if 문
temperature = 12
if temperature <= 10:
    print("자켓을 입는다")
else:
print("자켓을 입지 않는다.")

if, while 문 연습 1
i = 1
total = 0

while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        total += i
    i = i + 1

print(total)

# if, while 문 연습 2
N = 120
i = 1
count = 0
while i <= N:
    if N % i == 0:
        print(i)
        count += 1
    i = i + 1

print()
print(f"{N}의 약수는 총 {count}개입니다.")

# if, while 문 연습 3
상수
INTEREST_RATE = 0.12
APT_PRICE_2016 = 111100000000
# 변수
year = 1988
money = 50000000

while year < 2016:
    money = money * (1 + INTEREST_RATE)
    year += 1

if money > APT_PRICE_2016:
    print(f"{money - APT_PRICE_2016}원 차이로 동일 아저씨 말씀이 맞습니다.")
else:
    print(f"{APT_PRICE_2016 - money}원 차이로 미란 아줌마 말씀이 맞습니다.")

# if, while 문 연습 4(피보나치의 수열)
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous
    previous = current
    current = current + temp
    i += 1

if, while 문 연습 5
i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(f"{i} * {j} = {i * j}")
        j += 1
    i += 1

# break문 사용
i = 100
while True:
    if i % 23 == 0:
        break
    i = i + 1

print(i)

# continue 문 사용
i = 0

while i < 15:
    i += 1

    if i % 2 == 1:
        continue
    print(i)