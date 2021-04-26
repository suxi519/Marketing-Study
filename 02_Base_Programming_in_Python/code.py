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

# if, while 문 연습 3
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

# if, while 문 연습 4(피보나치의 수열)
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

# if, while 문 연습 5
# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(f"{i} * {j} = {i * j}")
#         j += 1
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

# names = ["윤수", "혜린", "소희"]
# print(names[0])
#
# numbers = [2, 3, 4, 5]
# print(numbers[0] + numbers[1])

# numbers = []
# print(len(numbers))
# numbers.append(5)
# numbers.append(8)  # 항상 끝에 추가
# print(numbers)
# print(len(numbers))
# del numbers[1]
# print(numbers)
# numbers.insert(1, 100)  # 원하는 자리에
# print(numbers)
# num = [1, 2, 3, 9, 7, 5, 5, 4]
# new_list = sorted(num, reverse=True)
# print(new_list)

# 리스트 실습 1
# greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
#
# i = 0
# while i < len(greetings):
#     print(greetings[i])
#     i += 1


# 리스트 실습 2
# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5 / 9
#
#
# temperature_list = [40, 15, 32, 64, -4, 11]  # 화씨 온도
# print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력
#
# i = 0
# while i < len(temperature_list):
#     temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]) ,1)
#     i += 1
#
#
# print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력

# 리스트 연습 3
# 원화(￦)에서 달러($)로 변환하는 함수
# def krw_to_usd(krw):
#     return krw / 1000


# 달러($)에서 엔화(￥)로 변환하는 함수
# def usd_to_jpy(usd):
#     return usd * 125


# 원화(￦)으로 각각 얼마인가요?
# prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
# print("한국 화폐: " + str(prices))
#
# i = 0
# while i < len(prices):
#     prices[i] = krw_to_usd(prices[i])
#     i += 1
#
# # 달러($)로 각각 얼마인가요?
# print("미국 화폐: " + str(prices))
#
# i = 0
# while i < len(prices):
#     prices[i] = usd_to_jpy(prices[i])
#     i += 1
#
# # 엔화(￥)으로 각각 얼마인가요?


# print("일본 화폐: " + str(prices))

# 리스트 연습 4
# 빈 리스트 만들기
# numbers = []
# print(numbers)
#
# numbers.append(1)
# numbers.append(7)
# numbers.append(3)
# numbers.append(6)
# numbers.append(5)
# numbers.append(2)
# numbers.append(13)
# numbers.append(14)
# numbers.sort()
# print(numbers)
#
# i = 0
# while i < len(numbers):
#     # 홀수면 제거
#     if numbers[i] % 2 == 1:
#         del numbers[i]
#     else:
#         i += 1
#
# del numbers[:2]
# numbers.insert(0, 6)
# numbers.insert(1, 2)
# print(numbers)
#
# numbers.insert(0, 20)
# print(numbers)
#
# new_num = sorted(numbers)

# print(new_num)

# def in_list(some_list, value):
#     i = 0
#     while i < len(some_list):
#         if some_list[i] == value:
#             return True
#         i += 1
#
#     return False
#
#
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
# print(in_list(primes, 7))
# print(in_list(primes, 12))
# print(7 in primes)
# print(12 in primes)
# print(7 not in primes)
# print(12 not in primes)

# # 세 번의 시험을 보는 수업
# grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]
#
# # 첫 번째 학생의 성적
# print(grades[0])
#
# # 첫 번째 학생의 첫 번째 시험 성적
# print(grades[0][0])
#
# # 첫 번째 시험의 평균

# print(grades[0][0] + grades[1][0] + grades[2][0] / 3)

# list remove
# a = [1, 2, 1, 3, 4, 5, 1]
# a.remove(1)
#
#
# print(a)
# print(a[0])

# list pop
# a = [1, 2, 1, 3, 4, 5, 1]
# removed = a.pop(1)
#
# print(a)
# print(removed)
# print(a[0])

#list del
# a = [1, 2, 3, 4, 5, 6]
# del a[1]
#
# print(a)
# print(a[1])

# a = [1, 2, 3, 4, 5, 6]
# del a[:3]
#
# print(a)

# members = ["수시", "뱁새", "구구쓰", "복근"]
# print(members.index("뱁새"))
# print(members.index("복근"))

# my_list = [2, 3, 4, 5, 6]
#
# for numbers in my_list:
# print(numbers)
#
# my_dic = {
#     5: 25,
#     2: 4,
#     3: 9
# }
# print(my_dic)
# print(type(my_dic))
# print(my_dic[5])
# my_dic[7] = 49
# print(my_dic)
#
# my_family = {
#     '엄마' : '김공주',
#     '아빠' : '이용왕',
#     '아들' : '이왕자',
#     '딸' : '이거지'
# }
# print(my_family['엄마'])

# my_family = {
#      '엄마' : '김공주',
#      '아빠' : '이용왕',
#      '아들' : '이왕자',
#      '딸' : '이거지'
# }
#
# print('이거지' in my_family.values())
#
# for value in my_family.values():
#     print(value)
#
# print('아들' in my_family.keys())
#
# for value in my_family.keys():
#     print(value)
#
# for key in my_family.keys():
#     value = my_family[key]
#     print(key, value)
#
# for key, value in my_family.items():
#     print(key, value)
#

# x = 5
# y = x
# y = 3
# print(x)
# print(y)
#
# x = [2, 3, 5, 7, 11]
# y = x
# y[2] = 4
# print(x)
# print(y)
#
# x = [2, 3, 5, 7, 11]
# y = list(x)
# y[2] = 4
# print(x)
# print(y)

# x = [2, 3, 5, 7, 9]
# y = x
# print(y)
#
# y[2] = 11
# x[4] = 13
#
# print(y)

# eng_list = ['a', 'b', 'c', 'd', 'e']
# eng_str = 'abcde'
#
# print(eng_str[0])
# print(eng_str[1])
# print(eng_str[2])
# print(eng_str[-1])
# print(eng_list[0])
# print(eng_list[1])
# print(eng_list[2])
# print(eng_list[-1])
# print(eng_list[0:3])
# print(eng_list[3:])
# print(eng_list[:4])
# print(eng_str[0:3])
# print(eng_str[3:])
# print(eng_str[:4])
# print(len(eng_list))
# print(len(eng_str))
#
# str_1 = 'hello'
# str_2 = 'world'
# str_3 = str_1 + str_2
# print(str_3)
#
# list_1 = [1, 2, 3, 4]
# list_2 = [5, 6, 7, 8]
# list_3 = list_1 + list_2
# print(list_3)
#
# num = [1, 2, 3, 4]
# num[0] = 5
# print(num)
#
# num = '1234'
# num[0] = 5
# print(num)

# 자리수 합 리턴
# def sum_digit(num):
#     total = 0
#     str_num = str(num)
#
#     for i in range(len(str_num)):
#         digit = str_num[i]
#         total += int(digit)
#
#     return total
#
# digit_total = 0
# for i in range(1, 1001):
#     digit_total += sum_digit(i)

# print(digit_total)

# def mask_security_number(security_number):
#
#     num_list = []
#     for i in range(len(security_number)):
#         num_list.append(security_number[i])
#
#     for i in range(len(num_list) - 4, len(num_list)):
#         num_list[i] = '*'
#
#     total_str = ""
#     for i in range(len(num_list)):
#         total_str += num_list[i]
#
#     return total_str
#
# print(mask_security_number("880720-1234567"))



# 테스트
# print(mask_security_number("880720-1234567"))
# print(mask_security_number("8807201234567"))
# print(mask_security_number("930124-7654321"))
# print(mask_security_number("9301247654321"))
# print(mask_security_number("761214-2357111"))
# print(mask_security_number("7612142357111"))

#
# def sum_digit(num):
#     total = 0
# s
#     for num in len(sum_digit):
#         print += len(sum_digit)
#
#     print(sum_digit)
#
# print(sum_digit(486))

# def mask_security_number(security_number):
#     return security_number [:-4] + '*****'
#
# print(mask_security_number("880720-1234567"))
# print(mask_security_number("8807201234567"))
# print(mask_security_number("930124-7654321"))
# print(mask_security_number("9301247654321"))
# print(mask_security_number("761214-2357111"))
# print(mask_security_number("7612142357111"))
#
# list_1 = [1, 2, 3, 4]
# list_2 = [5, 6, 7, 8]
# list_3 = list_1 + list_2
# print(list_3)

# def is_palindrome(word):
#     for left in range(len(word) // 2):
#         # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
#         right = len(word) - left - 1
#         if word[left] != word[right]:
#             return False
#
#     # for문에서 나왔다면 모든 쌍이 일치
#     return True
#
#
# # 테스트
# print(is_palindrome("racecar"))
# print(is_palindrome("stars"))
# print(is_palindrome("토마토"))
# print(is_palindrome("kayak"))
# print(is_palindrome("hello"))
# print(is_palindrome("hello"))
#
# print(7//2)

# 바뀌지 않을 상수 정의 - 게임의 정답, 총 기회 수
# import random
#
# answer = random.randint(1, 20)
# tries_num = 4
#
# guess = -1
# tries = 0
#
# while guess != answer and tries  < tries_num:
#     guess = int(input(f"기회가 {tries_num - tries}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
#     tries += 1
#
#     if answer > guess:
#         print("up")
#     elif answer < guess:
#         print("down")
# if guess == answer:
#     print(f"축하합니다. {tries_num - tries}번 만에 숫자를 맞히셨습니다.")
# else:
#     print(f"아쉽습니다. 정담은 {answer}입니다.")

# my_string = "1, 2, 3, 4, 5, 6"
# print(my_string.split(", "))

# full_name = "Hong, Gu"
# name_data = full_name.split(", ")
# last_name = name_data[0]
# first_name = name_data[1]
# print(first_name, last_name)

# print(" \n\n 2 \t 3 \n 5 7 11 \n\n".split())
# numbers = " \n\n 2 \t 3 \n 5 7 11 \n\n".split()
# print(int(numbers[0]) + int(numbers[1]))

# 파일을 연다
# with open('매출.txt', 'r', encoding='UTF8') as f:
#     total_revenue = 0
#     total_days = 0
#     # 숫자만 분리
#     for line in f:
#         data = line.strip().split(": ")
#         revenue = int(data[1])
#         print(revenue)
#     # 매출 계산
#         total_revenue += revenue
#         total_days += 1
#
#         print(total_revenue / total_days)

# with open('new_file.txt', 'w') as f:
#     f.write("hello!\n")
#     f.write("I'm suxi\n")

# 사용자의 입력을 받아야함



# 만약 q를 입력 받으면 프로그램을 종료해야함.

# 입력받은 단어가 dict형태로 정리되어야함.
with open('voca.txt', 'w', encoding='UTF8' ) as f:
     while True:
          english_word = input('영어 단어를 입력하세요: ')
          if english_word == 'q':
               break

          korean_word = input('한국어 뜻을 입력하세요: ')
          if korean_word == 'q':
               break

          print('{}: {}\n'.format(english_word, korean_word))
