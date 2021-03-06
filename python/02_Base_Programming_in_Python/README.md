## 자료형  
### 0. type 함수  
코딩 시 쓰고 있는 자료형의 종류를 알 수 없을 때 알려주는 함수  

### 1. 프린트(print)  
* print() 함수는 출력 함수로 사용.  
* print(3*4)  

### 2. 코멘트(comment)  
* "코멘트 중요하다!"  

### 3. 자료형(data type)  

#### 3-1. 숫자(number)  
* 정수(integer) 2  
* 소수(floating point) 2.0    

#### 3-2. 문자열(string)  
* 키보드로 쓸 수 있는 문자들을 표현하는 자료형  
* "2" or '2'  

#### 3-3. 형 변환(Type Conversion)   
값을 한 자료형에서 다른 자료형으로 바꾸는 것       

정수 7 -> 소수 7.0      
문자열 "7" -> 정수 7    
````python
print(int(3.8))  
````
#### 3-4. 문자열 format    
print("저는 {}, {}, {}를 좋아합니다!".format("사과", "배", "딸기"))


#### 3-5. 불린(Boolean)  
* 참, 거짓을 표현하는 자료형    
* 명제 - 참 또는 거짓이 확실한 문장  
* 불 대수 - 일상적인 논리를 수학적으로 표현하는 것  
* 진리값(불 대수의 값) - true or false  
* 불 대수의 연산 - and, or, not  

### 4.추상화(abstraction)   
#### 4-1. 변수(variable)  
* 지정연산자 - 오른쪽 값을 왼쪽 변수에 지정해주는 것  
* 데이터를 저장할 수 있는 메모리 공간, 저장된 값은 변경 가능  
* oreo = 990  

#### 4-2. 함수(function)  
* 하나의 특별한 목적의 작업을 수행하기 위해 독립적으로 설계된 프로그램 코드의 집합    
* 장점
1. 반복적인 프로그래밍을 피할 수 있음.  
2. 모듈화는 전체적인 코드의 가독성을 높임.  
3. 유지보수가 용이함.  
```python
def hello():
    print("hello")
    print("welcome to korea")

hello()
```

#### 4-3. 파라미터(parameter)  
* 함수의 정의에서 전달받은 인수를 함수 내부로 전달하기 위해 사용하는 변수.  
* 인수(argument)란 함수가 호출될 때 함수로 값을 전달해주는 값.  

```python
def hello(name):
    print("hello")
    print(name)
    print(welcome to korea)

hello("sohee")
```

#### 4-4. 여러 개의 파라미터  
```python
def print_sum(a, b, c):
    print(a + b + c)

print_sum(7, 3, 1)

```
#### 4-5. 옵셔널 파라미터(optional parameter)  
* 파라미터에 '기본값(default value)'을 설정하면 함수 호출할 때 꼭 파라미터에 값을 안 념겨 줘도 됨.  
* 옵셔널 파라미터는 모두 마지막에 있어야 함.  

#### 4-6. return  
##### 4-6-1. return 문의 역할  
* 값 돌려주기  
* 함수 즉시 종료하기  
##### 4-6-2. return 과 print 의 차이    
* print 는 호출될 때마다 계산되고, 리턴은 값만 호출된다.    

#### 4-7. Syntactic Sugar  
* 문법 기능은 그대로인데 직관적으로 쉽게 읽을 수 있는 코드     

#### 4-8. scope(범위)  
* scope : 변수가 사용 가능한 범위  
* 로컬변수 : 변수를 정의한 함수 내에서만 사용 가능  
* 글로벌 변수 : 모든 곳에서 사용 가능  
* 함수에서 변수를 사용하면, 로컬 변수를 면저 찾고 나서 글로벌 변수를 찾음  

#### 4-9. 상수(constant)  
* 값이 고정되어 변경할 수 없는 메모리 공간  
* 대문자로 표기 - 일반변수와 상수를 쉽게 구분짓기 위해  

#### 5-0. 스타일(style)  
* 파이썬 스타일 가이드 PEP 8  
* 스타일 가이드를 잘 따라야 읽기 쉬운 코드가 됨.  

##### 5-0-1. 이름 규칙  
* 모든 변수와 함수 이름은 소문자로 쓰고, 여러 단어일 경우 _로 나눔.  
```python
some_variable_name = 1


def some_function_name():
    print("hello")
```

* 모든 상수 이름은 대문자로 써주시고, 여러 단어일 경우 _로 나눔.  
```python
SOME_CONSTANT = 3.14
```

##### 5-0-2. 의미 있는 이름  
```python
radius = 2
pi = 3.14
print(pi * radius * radius)


def say_hello():
    print("hello, world!")


print(say_hello())
```

##### 5-0-3. 들여쓰기    
* 들여쓰기는 무조건 스페이스 4번  

```python
def say_hello():
    print("Hi")
```

##### 5-0-4. 함수 정의  
* 함수 정의 위아래로 빈 줄이 두 개씩 있어야 함. 하지만 파일의 첫 줄이 함수 정의인 경우 해당 함수 위에는 빈줄 없어도 됨.  
```python
def a():
    print('a')


def b():
    print('b')


def c():
    print('c')
```

##### 5-0-5. 괄호 안  
* 괄호 바로 안에는 띄어쓰기를 하지 않음.  
```python
spam(ham[1], {eggs: 2})
```

##### 5-0-6. 함수 괄호  
* 함수를 정의하거나 호출할 때, 함수 이름과 괄호 사이에 띄어쓰기 하지 않음.  
```python
def spam(x):  # 함수 정의할 때
    print(x + 2)

spam(2)  # 호출할 때
```

##### 5-0-7. 쉼표  
* 쉼표 앞에는 띄어쓰기를 하지 않음.  
```python
print(x, y)
``` 

##### 5-0-8. 지정 연산자, 연산자    
* 지정 연산자 앞뒤로 띄어쓰기 하나씩만  
* 연산자도 마찬가지로 앞뒤로 띄어쓰기 하나씩  
***하지만*** 연산의 "우선순위" 강조할 땐, 앞뒤 붙여 씀.    
```python
# 지정 연산자
x = 1

# 연산자  
i = i + 1
submitted += 1

# 연산자 우선순위 강조
x = x*2 - 1
hypot2 = x*x + y*y 
c = (a+b) * (a-b)
```
##### 5-0-9. 코멘트  
* 코드와 같은 줄에 코멘트를 쓸 경우, 코멘트 앞에 띄어쓰기 최소 2개  

### 5. 제어문  
#### 5-1. while 반복문  
```python
while 조건부분:  # 명령 실행을 위한 조건 
    수행부분  # 반복적으로 실행하고 싶은 명령
```
#### 5-2. if문  
 ```python
if 조건부분:
    수행부분
elif 조건부분:
    수행부분
```

#### 5-3. 제어문 꿑팁
##### 5-3-1. break 문 
* 만약 while 문의 조건 부분과 상관 없이 반복문에서 나오고 싶으면,break 문을 사용함.  
````python
i = 100
while True:
    if i % 23 == 0:
        break
    i = i + 1

print(i)
````
##### 5-3-2. continue 문
* 현재 진행되고 있는 수행 부분을 중단하고 바로 조건 부분을 확인하고 싶으면 continue문 씀.  
```python
i = 0

while i < 15:
    i += 1
    
    if i % 2 == 1:
        continue
    print(i)
```
#### 5-4. for 반복문  
```python
my_list = [2, 3, 4, 5, 6]

for number in my_list:
    print(number)
```
 
 #### 5-6. range 함수
 * 간편함, 깔끔함, 메모리 효율성 놓음.  
```python
# range() / 한 개 쓰는 버전
for i in range(10):
    print(i)
# range( ,  ) / 두 개 쓰는 버전
for i in range(3, 11):
    print(i)
# range( ,  ,  ) / 세 개 쓰는 버전
for i in range(3, 17, 3):
    print(i)
```

### 6. 리스트(list)  
* 변수에 여러가지 값을 저장  
```python
numbers = [2, 3, 4, 5]
names = ["윤수", "혜린", "소희"]   
```
* 각각의 변수를 "요소"라고 말함.  
* '인덱스(index)' - 인덱스에서 요소의 위치  
* '인덱싱(indexing)' - 인덱스를 통해 요소를 받아오는 것.    
```python
names = ["윤수", "혜린", "소희"]  
print(names[0])

numbers = [2, 3, 4, 5]
print(numbers[0] + numbers[1])
``` 
* 리스트 슬라이싱(list slicing)   
* slice는 원본 리스트는 그대로 존재, 원하는 범위만큼 출력 후 새로운 리스트 생성  
```python
print(numbers[2:])
print(numbers[:3])
```
* 리스트의 인자를 바꿀 수 있음.  
```python
numbers = [2, 3, 4, 5]
numbers[0] = numbers[0] + numbers[1]
print(numbers)
``` 
#### 6-1. 리스트 함수  
* 리스트 안에 인자 갯수 파악.    
```python
numbers = []
len(numbers)
``` 
* 리스트 끝에 인자 추가.  
```python
numbers.append(8)  # 항상 끝에 추가
```
* 리스트 원하는 위치에 인자 추가.  
```python
numbers.insert(1, 100)  # 원하는 자리에
```
* 리스트 인자 제거  
* remove()  
* 지우고자 하는 인덱스가 아닌 값을 입력하는 방식  
* 지우고자 하는 값이 리스트 내에 2개 이상이면 순서상 가장 앞에 있는 값을 지우게 되고, 값 삭제 후 리스트 재조정.  
```python
a = [1, 2, 1, 3, 4, 5, 1]
a.remove(1)
```

* pop(), del()  
* 지우고자 하는 리스트의 인덱스를 받아 지우는 방식  
* pop()은 지워진 인덱스의 값을 반환, del은 안 반환  
* 특정 인덱스를 삭제한 다음, 리스트 재조정  
* del()은 리스트의 범위를 지정해 삭제 가능  

```python
a = [1, 2, 1, 3, 4, 5, 1]
removed = a.pop(1)

print(a)
print(removed)
print(a[0])

a = [1, 2, 3, 4, 5, 6]
del a[1]
 
print(a)
print(a[1])

a = [1, 2, 3, 4, 5, 6]
del a[:3]

print(a)
```

#### 6-2. 리스트 정렬  
* "sorted" 는 기존 리스트 건드리지 않고, 정렬된 새 리스트 리턴  
```python
num = [1, 2, 3, 9, 7, 5, 5, 4]
new_list = sorted(num)
num.sorted()
# new_list = sorted(num, reverse=True)  # 반전
# print(new_list)
```
* "sort" 는 아무것도 리턴하지 않고, 기존 리스트를 정렬  
```python
num = [1, 2, 3, 9, 7, 5, 5, 4]
num.sort()
# reverse는 원소들을 뒤집어진 순서로 배치
# num.sort(reverse=True)  # 반전
# print(num)
```

#### 6-2. 리스트 팁  
##### 6-2-1. 리스트에서 값을 존재 확인하기  
* 확인 기능이 파이썬 자체에 내장되어 있음  
```python
# 값이 안에 있는지 확인 "in"
print(7 in primes)
print(12 in primes)
# 값이 안에 없는지 확인 "not in"
print(7 not in primes)
print(12 not in primes)
```  

```python
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        if some_list[i] == value:
            return True
        i += 1

    return False

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 7))
```
##### 6-2-2. 리스트 안의 리스트 (Nested List)  
* 리스트 안에 또 다른 리스트가 있을 수 있음.  
```python
# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])

# 첫 번째 시험의 평균
print(grades[0][0] + grades[1][0] + grades[2][0] / 3)
```

##### 6-2-3. index 메소드  
* 리스트 인자의 인덱스를 리턴  
```python
members = ["수시", "뱁새", "구구쓰", "복근"]
print(members.index("뱁새"))
print(members.index("복근"))
```

#### 6-3. 사전(dictionary)  
* key-value pair (키-값 쌍)  
```python
my_dic = {
    5: 25,
    2: 4,
    3: 9
}
```
* 순서라는 개념이 없음.  
* 사전의 키는 정수형일 필요가 없음.  
```python
my_family = {
    '엄마' : '김공주',
    '아빠' : '이용왕',
    '아들' : '이왕자',
    '딸' : '이거지'
}
```
#### 6-4. aliasing  
```python
x = [2, 3, 5, 7, 11]
y = list(x)  #리스트 복사
y[2] = 4
print(x)
print(y)
``` 
#### 6-5. 리스트와 문자열    
6-5-1. 공통점  
* 인덱싱 가능/ for문에서도 사용가능  
* 슬라이싱 가능  
* 덧셈 연산 가능  
* len 함수 사용 가능  
6-5-2. 차이점  
* 리스트는 인자를 바꿀 수 있음(mutable)  
* 숫자, 불린, 문자열 인자 바꿀 수 없음(immutable)  

#### 6-5. 모듈  
* 코드와 재활용성을 높이고, 유지보수르 쉽게하는 기능들을 정리해둔 프로그램    
```python
import calculator as calc

print(calc.add(2,5))
print(calc.multiply(3,4))

from calculator import add, multiply
print(add(2,5))
print(multiply(3,4))

# 권장하지 않음, 함수의 출처가 불분명해짐.
from calculator import * 
```
##### 6-5-1. math 모듈    
```python
import math
print(math.log10(100))

import os
print(os.getlogin())
print(os.getcwd())  #현재 파일의 경로를 불러올 수 있음.
``` 

##### 6-5-2. random 모듈
* 랜덤한 숫자를 생성하기 위한 다양한 함수 제공.  
* randint 함수 = 두 수 사이의 어떤 랜덤한 정수를 리턴하는 함수.  
* uniform 함수 - 두 수 사이의 랜덤한 소수를 리턴하는 함수.  
```python
import random
print(random.random())
# randint(a, b)는, a =< N =< b 정수 N 리턴  
print(random.randint(1, 20))
# uniform 함수 - 두 수 사이의 랜덤한 소수를 리턴하는 함수.  
print(random.uniform(0, 1))
```

##### 6-5-3. datetime 모듈  
* '날짜'와 '시간'을 다루기 위한 다양한 '클래스'가 있음.  
```python
import datetime

pi_day = datetime.datetime(2020, 3, 14, 16, 50, 00)
print(pi_day)
print(type(pi_day))

# 지금 이 순간의 날짜와 시간을 받아오고 싶을 때
today = datetime.datetime.now()
print(today)
print(type(today))

# 두 datetime 값 사이의 기간을 알고 싶으면, 숫자 뺄셈 하듯 빼면 됨.
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 16, 50, 00)
print(today - pi_day)

# timedelta는 날짜 간의 차이를 나타내는 타입
print(type(today - pi_day))

# timedelta를 생성해서 datetime 값에 더해 줄 수 있음.
today = datetime.datetime.now()
my_timedelta = datetime.timedelta(day=5, hour=3, minutes=10, seconds=50)
print(today)
print(today + my_timedelta)

#datetime 값에서 '연도'나 '월' 같은 값을 추출하려면?
today = datetime.datetime.now()
print(today)
print(today.year) #연도
print(today.month) # 월
print(today.day) # 일
print(today.hour) # 시
print(today.minute) # 분
print(today.second) #초
print(today.microsecond)

#strftime 출력
today = datetime.datetime.now()
print(today)
print(today.strftime("%a, %b %dth %y"))
```
![image](https://user-images.githubusercontent.com/55868306/115842356-b3781200-a458-11eb-840f-bf39e432dc4c.png)

#### 6-5. input 함수  
* 사용자가 어떤 값을 입력하게 하고, 그 값을 변수에 저장
```python
name = input("이름을 입력하세요: ")  #설명용도
print(name)

#input의 입력값은 str 형태
x = int(input("숫자를 입력하세요: "))
print(x + 5)
```
#### 6-6. 파일 읽기  

```python
# f라는 파일을 읽어들임.
with open('chicken.txt', 'r') as f:
# print(type(f))
    for line in f:
    print(line)
```
#### 6-7. strip  
* 화이트 스페이스("","\t","\n")를 제거해줌.  
```python
print("   abc   def   ".strip())
```
#### 6-8. split   
* 문자열을 공백 혹은 어떠한 기준으로 나눌 때 사용하는 함수  
* split()은 요소들을 문자열로 만듦.  
```python
my_string = "1, 2, 3, 4, 5, 6"
print(my_string.split(","))
```
#### 6-9. 파일쓰기  
* 'a' append는 파일을 쓸 때 마지막에 텍스트를 추가.  
```python
with open('codes/new_file.txt', 'w') as f:
    f.write("hello!")
    f.write("I'm suxi")
```









 