# """
# # 0. type 함수
# print(type(3))
# print(type(3.0))
# print(type("3"))
# print(type("True"))
# print(type(True))
#
#
# def hello():
#     print("hello suxi")
#
#
# print(type(hello))
# print(type(print))
# print(int(2.5) + int(3.8) > int(str(1) + str(2)))
#
# print(type(4 / 2))
# print(type("True"))
# print(type(10 <= 7))
# print(type(2 ** 3.0))
# print(type(2 * 3 == 6))
# """
#
# """
# # 3-1. 숫자형
# # 주의 (숫자형끼리 계산 가능)
# print(10 / (10 % 6))
# print(4.0 + 7)
# print(2 ** 3.0)
# print(7.0 - 3)
#
# # 덧셈
# print(4 + 7)
# print(4.0 + 7.0)
#
# # 뺄셈
# print(2 - 4)
# print(2.0 - 4.0)
#
# # 곱셉
# print(5 * 3)
# print(5.0 * 3.0)
#
# # 나눗셈
# print(2 / 3)
#
# # 나머지
# print(7.0 % 3.0)
#
# # 거듭제곱
# print(2.0 ** 3.0)
#
# # 사칙연산
# print(2 * 3 + 2)
# print(2 * (3 + 2))
#
# # 버림 나눗셈 (floor division)
# print(7 // 2)
# print(7 / 2)
# print(7.0 // 2.0)
#
# # 반올림 (round)
# print(round(3.141592, 5))
# """
#
# """
# # 3-2. 문자열
# # '코드잇', "코드잇"
# print("i'm student")
# print("I\'m \"excited\" to learn Python!")
# print('hello' * 3)
# print('30' + '5')
# """
#
# """
# # 3-3. 형 변환(Type Conversion)
# print(int(3.8))
# print(float(3))
# print(int("2") + int("5"))
# print(float("1.1") + float("2.5"))
# print(str(2) + str(5))
# age = 7
# print("제 나이는 " + str(age) + "살입니다.")
# """
#
# """
# # 3-4. format method
# # 오늘은 2019년 10월 29일 입니다.
# year = 2019
# month = 10
# day = 29
# print("오늘은 " + str(year) + "년 " + str(10) + "월 " + str(29) + "일 " + "입니다.")
# print("오늘은 {}년 {}월 {}일 입니다.".format(year, month, day))
# date_string = "오늘은 {}년 {}월 {}일 입니다."
# print(date_string.format(year, month, day + 1))
# print("저는 {}, {}, {}를 좋아합니다!".format("사과", "배", "딸기"))
# print("저는 {2}, {1}, {0}를 좋아합니다!".format("사과", "배", "딸기"))
# num_1 = 1
# num_2 = 3
# print("{0} 나누기 {1}은 {2:.3f}입니다.".format(num_1, num_2, num_1 * num_2))
#
# name = "한수시"
# age = 10
# # 가장 오래된 방식 (% 기호)
# # %s, %d는 '포맷 스트링'
# print("제 이름은 %s이고 %d살입니다." % (name, age))
# # 요즘 많이 쓰는 방식 (format 메소드)
# print("제 이름은 {}이고 {}살입니다.".format(name, age))
# # 새로운 방식(f-string)
# print(f"제 이름은 {name}이고 {age}살입니다.")
#
# # f-string 변형
# num_1 = 4
# num_2 = 2
# num_3 = 2
# print(f'{num_1} 나누기 {num_2}은 {num_3}입니다.')
#
# # print(5710.8 / 5)
# h = 1
# wage = 5
# exchange_rate = 1142.16
# print('{}시간에 {}달러 벌었습니다.'.format(1, wage))
# print(f'{h * 5}시간에 {wage * 5}달러 벌었습니다.')
# print(f'{h}시간에 {exchange_rate * 5}달러 벌었습니다.')
# print(f'{h * 5}시간에 {exchange_rate * 5 * 5}달러 벌었습니다.')
# """
#
# """
# # 3-5. 불린(Boolean)
# print(True)
# print(False)
# print(2 > 1)
# print(2 < 1)
# print(3 >= 2)
# print(3 <= 3)
# print(2 == 2)
# print(2 != 2)
# print(2 > 1 and "hello" == "Hello")
# print(not not True)
# print(not not False)
# print(7 == 7 or (4 < 3 and 12 > 10))
# x: int = 3
# print(x > 4 or not (x < 2 or x == 3))
# """
#
# """
# # 4-1. 지정연산자
# x = 7
# x = x + 1
# print(x)
# """
#
# """
# # 4-2. 함수의 실행 순서
# def hello():
#     print("hello")
#     print("welcome to code it!")
#
#
# print("함수 호출 전")
# hello()  # 함수 호출
# print("함수 호출 후")
# """
#
# """
# # 4-5. 옵셔널 파라미터(optional parameter)
# def myself(name, age, nationality="한국"):
#     print("내 이름은 {}" .format(name))
#     print("나이는 {}살" .format(age))
#     print("국적은 {}" .format(nationality))
#
#
# myself("코드잇", 1, "미국")
# myself("코드잇", 1)
# """
#
# """
# # 4-6. return 문
# def square(x):
#     print("함수 시작")
#     return x * x
#     # print("함수 끝") # dead code
#
#
# print(square(3))
# print("hello world!")
#
#
# def hello(name):
#     print(f"안녕하세요. {name}입니다.")
#     return "만나서 반갑습니다."
#
#
# print(hello("영훈"))
#
#
# def print_odd(x: int):
#     if x % 2 == 0:
#         return x
#     print(x)
#
# # return 과 print 의 차이
# # print 는 호출될 때마다 계산되고, 리턴은 값만 호출된다.
#
#
# def print_square():
#     print(x * x)
#
#
# def return_square():
#     return x * x
#
#
# # def print_sqr(y, n):
# # return y ** n
#
# print_square()
# answer = return_square()
# print(answer)
# print(3)
# """
#
# """
# # 4-7. Syntactic Sugar
# '''
# # +=
# x = x + 1
# x += 1
#
# # *=
# x = x * 2
# x *= 2
#
# # -=
# x = x - 3
# x -= 3
#
# # /=
# x = x / 2
# x /= 2
#
# # %=
# x = x % 7
# x %= 7
# '''
# """

# 4-8. scope(범위)
# def my_function():
#     x = 3 # 로컬변수
#     print(x)
#
#
# my_function()
# print(x)

# x = 2 # 전역변수

# def my_function():
#     print(x)
#
#
# my_function()
# print(x)

# x = 2
#
#
# def my_function():
#     x = 3
#     print(x)
#
#
# my_function()
# print(x)
#
#
# def square(x):
#     return x * x
#
#
# print(square(3))

# 4-9. 상수(constant)
# PI = 3.14
#
#
# def calculate_area(r):
#     return PI * r * r
#
#
# radius = 4
# print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))


# 실습
# def is_evenly_divisible(number):
#     if number % 2 == 0:
#         return True
#
#     else:
#         return False
#
#
# # 테스트
# print(is_evenly_divisible(3))
# print(is_evenly_divisible(7))
# print(is_evenly_divisible(8))
# print(is_evenly_divisible(218))
# print(is_evenly_divisible(317))

# 5-1. while 반복문
# while 조건 부분:  # 불린 값으로 계산되는 식 ex) x < 3, name == '유재석'
#    수행 부분  # 반복적으로 실행하고 싶은 명령 ex) print("나는 예쁘다"), i = i + 1

# while 문법 연습
# i = 1
# while i <= 50:
#     print(i * 2)
#     i += 1

# 5-2. if 문
# temperature = 12
# if temperature <= 10:
#     print("자켓을 입는다")
# else:
# print("자켓을 입지 않는다.")

# if, while 문 연습 1
# i = 1
# total = 0
#
# while i < 1000:
#     if i % 2 == 0 or i % 3 == 0:
#         total += i
#     i = i + 1
#
# print(total)

# if, while 문 연습 2
# N = 120
# i = 1
# count = 0
# while i <= N:
#     if N % i == 0:
#         print(i)
#         count += 1
#     i = i + 1
#
# print()
# print(f"{N}의 약수는 총 {count}개입니다.")

# 상수
# INTEREST_RATE = 0.12
# APT_PRICE_2016 = 111100000000
# # 변수
# year = 1988
# money = 50000000
#
# while year < 2016:
#     money = money * (1 + INTEREST_RATE)
#     year += 1
#
# if money > APT_PRICE_2016:
#     print(f"{money - APT_PRICE_2016}원 차이로 동일 아저씨 말씀이 맞습니다.")
# else:
#     print(f"{APT_PRICE_2016 - money}원 차이로 미란 아줌마 말씀이 맞습니다.")


# previous = 0
# current = 1
# i = 1
#
# while i <= 50:
#     print(current)
#     temp = previous
#     previous = current
#     current = current + temp
#     i += 1
# break문 사용
# i = 100
# while True:
#     if i % 23 == 0:
#         break
#     i = i + 1
#
# print(i)

# continue 문 사용
# i = 0
#
# while i < 15:
#     i += 1
#
#     if i % 2 == 1:
#         continue
#     print(i)




