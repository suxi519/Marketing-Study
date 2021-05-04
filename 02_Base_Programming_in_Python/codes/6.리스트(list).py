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

# list del
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

# 입력받은 단어가 dict형태로 정리되어야함.
# with open('vocabulary.txt', 'w', encoding='UTF8' ) as f:
#      while True:
#           english_word = input('영어 단어를 입력하세요: ')
#           if english_word == 'q':
#                break
#
#           korean_word = input('한국어 뜻을 입력하세요: ')
#           if korean_word == 'q':
#                break
#
#           f.write('{}: {}\n'.format(english_word, korean_word))

# class FileReader:
#     def __init__(self, file_name: str):
#         self._file_name = file_name
#         self._encoding = 'UTF8'
#
#     @property
#     def file_name(self):
#         return self._file_name
#
#     def yield_by_row(self):
#         with open(self.file_name, 'r', encoding=self._encoding) as f:
#             for row in f:
#                 yield row
#
#
# class Splitter:
#     @staticmethod
#     def split_by_colon(row: str):
#         return row.strip().split(': ')
#
#
# class Validator:
#     @staticmethod
#     def validate(english: str, korean: str):
#         user_input = input(f'{korean} : ')
#         if user_input == english:
#             print('맞습니다.')
#         else:
#             print(f'정답은 {english} 입니다.')
#
#
# reader = FileReader(file_name='vocabulary.txt')
# for row in reader.yield_by_row():
#     english, korean = Splitter.split_by_colon(row)
#     Validator.validate(english, korean)


import random

with open('vocabulary.txt', 'r', encoding='UTF8') as f:
    for line in f:
        data = line.strip().split(": ")
        # english, korean = data
        english = data[0]
        korean = data[1]
        random.choice(korean)

        user_input = input(f'{korean} : ')

        if user_input == english:
            print("맞습니다.")

        else:
            print(f"아쉽습니다. 정담은 {english} 입니다")

        # is_correct = user_input == english
        # if is_correct:
        #        print("맞습니다.")
        #        continue
        # print(f"아쉽습니다. 정담은 {english} 입니다")

def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True
# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))