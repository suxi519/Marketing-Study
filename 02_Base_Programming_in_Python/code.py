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

#거듭제곱
print(2.0 ** 3.0)

#사칙연산
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
print("{0} 나누기 {1}은 {2:.3f}입니다.".format(num_1, num_2, num_1*num_2))
# 가장 오래된 방식 (% 기호)
name = "한수시"
age = "10"

print()




