# 0. type 함수
print(type(3))
print(type(3.0))
print(type("3"))
print(type("True"))
print(type(True))


def hello():
    print("hello suxi")


print(type(hello))
print(type(print))
print(int(2.5) + int(3.8) > int(str(1) + str(2)))

print(type(4 / 2))
print(type("True"))
print(type(10 <= 7))
print(type(2 ** 3.0))
print(type(2 * 3 == 6))
# 3-1. 숫자형
# 주의 (숫자형끼리 계산 가능)
print(10 / (10 % 6))
print(4.0 + 7)
print(2 ** 3.0)
print(7.0 - 3)

# 덧셈
print(4 + 7)
print(4.0 + 7.0)

# 뺄셈
print(2 - 4)
print(2.0 - 4.0)

# 곱셉
print(5 * 3)
print(5.0 * 3.0)

# 나눗셈
print(2 / 3)

# 나머지
print(7.0 % 3.0)

# 거듭제곱
print(2.0 ** 3.0)

# 사칙연산
print(2 * 3 + 2)
print(2 * (3 + 2))

# 버림 나눗셈 (floor division)
print(7 // 2)
print(7 / 2)
print(7.0 // 2.0)

# 반올림 (round)
print(round(3.141592, 5))

# 3-2. 문자열
# '코드잇', "코드잇"
print("i'm student")
print("I\'m \"excited\" to learn Python!")
print('hello' * 3)
print('30' + '5')

# 3-3. 형 변환(Type Conversion)
print(int(3.8))
print(float(3))
print(int("2") + int("5"))
print(float("1.1") + float("2.5"))
print(str(2) + str(5))
age = 7
print("제 나이는 " + str(age) + "살입니다.")

# 3-4. format method
# 오늘은 2019년 10월 29일 입니다.
year = 2019
month = 10
day = 29
print("오늘은 " + str(year) + "년 " + str(10) + "월 " + str(29) + "일 " + "입니다.")
print("오늘은 {}년 {}월 {}일 입니다.".format(year, month, day))
date_string = "오늘은 {}년 {}월 {}일 입니다."
print(date_string.format(year, month, day + 1))
print("저는 {}, {}, {}를 좋아합니다!".format("사과", "배", "딸기"))
print("저는 {2}, {1}, {0}를 좋아합니다!".format("사과", "배", "딸기"))
num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2:.3f}입니다.".format(num_1, num_2, num_1 * num_2))

name = "한수시"
age = 10
# 가장 오래된 방식 (% 기호)
# %s, %d는 '포맷 스트링'
print("제 이름은 %s이고 %d살입니다." % (name, age))
# 요즘 많이 쓰는 방식 (format 메소드)
print("제 이름은 {}이고 {}살입니다.".format(name, age))
# 새로운 방식(f-string)
print(f"제 이름은 {name}이고 {age}살입니다.")

# f-string 변형
num_1 = 4
num_2 = 2
num_3 = 2
print(f'{num_1} 나누기 {num_2}은 {num_3}입니다.')

# print(5710.8 / 5)
h = 1
wage = 5
exchange_rate = 1142.16
print('{}시간에 {}달러 벌었습니다.'.format(1, wage))
print(f'{h * 5}시간에 {wage * 5}달러 벌었습니다.')
print(f'{h}시간에 {exchange_rate * 5}달러 벌었습니다.')
print(f'{h * 5}시간에 {exchange_rate * 5 * 5}달러 벌었습니다.')

# 3-5. 불린(Boolean)
print(True)
print(False)
print(2 > 1)
print(2 < 1)
print(3 >= 2)
print(3 <= 3)
print(2 == 2)
print(2 != 2)
print(2 > 1 and "hello" == "Hello")
print(not not True)
print(not not False)
print(7 == 7 or (4 < 3 and 12 > 10))
x: int = 3
print(x > 4 or not (x < 2 or x == 3))

# 4-1. 지정연산자
x = 7
x = x + 1
print(x)


# 4-2. 함수의 실행 순서
def hello():
    print("hello")
    print("welcome to code it!")


print("함수 호출 전")
hello()  # 함수 호출
print("함수 호출 후")


# 4-5. return 문
def square(x):
    print("함수 시작")
    return x * x
    # print("함수 끝") # dead code


print(square(3))
print("hello world!")


def print_odd(x: int):
    if x % 2 == 0:
        return x
    print(x)
