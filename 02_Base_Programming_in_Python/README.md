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
##### 5-3-1. continue 문
* 현재 진행되고 있는 수행 부분을 중단하고 바로 조건 부분을 확인하고 싶으면 continue문 씀.  
```python
i = 0

while i < 15:
    i += 1
    
    if i % 2 == 1:
        continue
    print(i)
```

### 6. 리스트(list)  
* 변수에 여러가지 값을 저장  

