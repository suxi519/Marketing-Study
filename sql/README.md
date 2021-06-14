SQL 기본
SQL(Structured Query Language)은 크게 3가지로 구분할 수 있다.  
![image](https://user-images.githubusercontent.com/55868306/121714262-a2728580-cb18-11eb-8944-12f330c46e9b.png)  
1. DDL (Data Definition Language)  
데이터를 **정의**하기 위한 언어    
(데이터베이스, 테이블, 뷰, 인덱스 등을 생성(정의) 및 삭제하기 위함)  
ex) CREATE, ALTER, DROP  

2. DML (Data Manipulation Language)  
데이터를 조작하기 위한 언어 (CRUD 연산이 해당한다고 이해하면 쉽다.)  
(테이블 안의 데이터를 조작하기 위한, DDL보다 좁은 범위에 속함.)  
(숫자에 사칙연산이 있듯, 데이터에는 CRUD(Create, Read, Update, Delete)연산이 있다.)  
ex) SELECT, INSERT, UPDATE, DELETE  

3. DCL (Data Control Language)  
데이터를 제어하기 위한 언어  
(사용자에게 권한 부여 및 해제)  
ex) GRANT, REVOKE, DENY  

# SELECT문  
DB 내의 테이블에서 원하는 정보를 추출하는 명령  
기본구조   
select 열 이름 from 테이블 이름 where 조건  
ex) select * from memberTBL  

* where절  
조회하는 결과에 특정한 조건을 줘서 원하는 데이터만 보고 싶을 때 사용  

* create table ... select 구문  
테이블을 복사해서 사용할 경우 사용  

* group by  
지정된 열을 그룹으로 묶어주는 역할, 집계 함수와 함께 사용  
 
