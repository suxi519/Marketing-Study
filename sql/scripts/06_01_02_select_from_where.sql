-- 6.1.2 특정한 조건의 데이터만 조회하는 <select...from...where> 
use sqldb;

-- select 열 이름 from 테이블 이름 where 조건식;
select * from usertbl where addr = '경남';

-- 조건 연산자(=, <, >, <=, >=, <>, != 등)와 관계 연산자 (not, or, and 등) 
select userID, Name from usertbl where birthYear >= 1970 or height >= 182;

-- between...and / 연속적인 값
select height, Name from usertbl where height between 180 and 183;

-- in() / 이산적인 값
select name, addr from usertbl where addr='경남' or addr='전남' or addr='경북';
select Name, addr from usertbl where addr in ('경남', '전남', '경북');

-- like / 문자열 내용 검색
select height, Name from usertbl where name like '김%';
select height, Name from usertbl where name like '_종신';

-- any(합집합)
select name, height from usertbl
where height >= any (select height from usertbl where addr = '경남');

-- all(교집합)
select height, name from usertbl
where height >= all (select height from usertbl where addr = '경남');

-- (in, =any) 동일 
select height, name from usertbl
where height = any (select height from usertbl where addr = '경남');

select height, name from usertbl
where height in (select height from usertbl where addr = '경남');

-- 원하는 순서대로 정렬하여 출력 : order by
select name, mDate from usertbl order by mDate; -- 오름차순(자동)
select name, mDate from usertbl order by mDate desc; -- 내립차순
select name, height from usertbl order by height desc, name asc;

-- distinct(중복제거)
select addr from usertbl;
select addr from usertbl order by addr;
select distinct addr from usertbl;

-- 출력하는 개수를 제한하는 limit
use employees;
select emp_no, hire_date from employees
order by hire_date asc
limit 0,5; -- limit 시작, 개수
/* limit 5 offset 0; -- limit 개수 offset 시작 */

-- 테이블을 복사하는 create table...select
-- create table 새로운 테이블 (select 복사할 열 from 기존테이블)
-- primary key, foreign key는 복사 안됨!!
use sqldb;
-- 테이블 복사
create table buytbl2 (select * from buytbl);
select * from buytbl2;
-- 원하는 열만 복사 가능
create table buytbl3 (select userID, prodName from buytbl);
select * from buytbl3;