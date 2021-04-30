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

# 4-5. 옵셔널 파라미터(optional parameter)
def myself(name, age, nationality="한국"):
    print("내 이름은 {}" .format(name))
    print("나이는 {}살" .format(age))
    print("국적은 {}" .format(nationality))


myself("코드잇", 1, "미국")
myself("코드잇", 1)

# 4-6. return 문
def square(x):
    print("함수 시작")
    return x * x
    # print("함수 끝") # dead code


print(square(3))
print("hello world!")


def hello(name):
    print(f"안녕하세요. {name}입니다.")
    return "만나서 반갑습니다."


print(hello("영훈"))


def print_odd(x: int):
    if x % 2 == 0:
        return x
    print(x)

# return 과 print 의 차이
# print 는 호출될 때마다 계산되고, 리턴은 값만 호출된다.


def print_square():
    print(x * x)


def return_square():
    return x * x


# def print_sqr(y, n):
# return y ** n

print_square()
answer = return_square()
print(answer)
print(3)

# 4-7. Syntactic Sugar
# +=
x = x + 1
x += 1

# *=
x = x * 2
x *= 2

# -=
x = x - 3
x -= 3

# /=
x = x / 2
x /= 2

# %=
x = x % 7
x %= 7

4-8. scope(범위)
def my_function():
    x = 3 # 로컬변수
    print(x)


my_function()
print(x)

x = 2 # 전역변수

def my_function():
    print(x)


my_function()
print(x)

x = 2


def my_function():
    x = 3
    print(x)


my_function()
print(x)


def square(x):
    return x * x


print(square(3))

4-9. 상수(constant)
PI = 3.14


def calculate_area(r):
    return PI * r * r


radius = 4
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))


실습
def is_evenly_divisible(number):
    if number % 2 == 0:
        return True

    else:
        return False


# 테스트
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))