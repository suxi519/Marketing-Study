README.md

# 1. 데이터베이스란?  
* '일정한 체계 속에 저장된' '데이터의' '집합'    

## 1-1. Table(표)이란?  
* '표 형식으로' '저장된' '데이터의 집합'  
![image](https://user-images.githubusercontent.com/55868306/115326936-12bff300-a1c9-11eb-9059-0d6e5b7a740f.png)

### 1-1-1. Table의 row  
* row(행)   
* 레코드(record) 혹은 튜플(tuple) 형태의 하나의 개체      
![image](https://user-images.githubusercontent.com/55868306/115327704-5bc47700-a1ca-11eb-95b1-8e3151887806.png)

### 1-1-2. Table의 column  
* column(열)  
* 테이블 속 하나의 개체가 가지는 속성    
![image](https://user-images.githubusercontent.com/55868306/115328113-09378a80-a1cb-11eb-98f1-1b18db42a57e.png)

## 1-2. DBMS(Data Base Management System)  
* DB를 관리하기 위해 사용하는 프로그램  
![image](https://user-images.githubusercontent.com/55868306/115328690-fbced000-a1cb-11eb-88af-4fdca9695bd5.png)

### 1-2-1. DBMS의 주요 구성요소 - client(클라이언트 프로그램)      
* 사용자가 server에 접속해서 원하는 데이터베이스 관련 작업을 할 수 있도록, SQL을 입력할 수 있는 화면 제공 프로그램  
* 예시 - MySQL은 CLI 환경에서 사용     

CLI(command line interface) 특성 <-> GUI(Graphic user interface)  
* 성능 - 그래픽이 필요 없기 때문에 더 빠르게 실행됨.  
* 명확성 - 명령어(command)를 사용해 실수가 적음.  

### 1-2-2. DBMS의 주요 구성요소 - server(서버 프로그램)    
client로부터 SQL문 등을 전달받아 데이터베이스 관련 작업을 직접 처리하는 프로그램  
![image](https://user-images.githubusercontent.com/55868306/115340824-68ed6000-a1e2-11eb-861c-63e454724450.png)

### 1-2-3. SQL(Structured Query Language)    
* DBMS에 명령을 내리기 위해 사용하는 언어  


  