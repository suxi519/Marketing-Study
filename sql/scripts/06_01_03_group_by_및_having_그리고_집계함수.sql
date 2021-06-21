-- 6.1.3 group by 및 having 그리고 집계 함수
-- group by절


use sqldb; -- 
show table status; -- 테이블의 정보 조회
desc buytbl; -- 테이블에 열이 무엇이 있는지 확인  
alter table buytbl change amout amount smallint; -- 테이블 이름 수정
select userID, amount from buytbl order by userID;
select userID as '사용자 아이디', sum(amount) as '총 구매 개수' from buytbl group by userID; -- 구매갯수
select userID as '사용자 아이디', sum(price*amount) as '총 구매 개수' from buytbl group by userID; -- 구매액

-- 집계 함수(또는 집합 함수)
-- 평균(average)
use sqldb;
select avg(amount) as '평균 구매 개수' from buytbl;
select userID, AVG(amount) as '평균 구매 개수' from buytbl group by userID;

-- 최소, 최대값 (min, max)
select name, height from usertbl where height = (select max(height)from usertbl)
or height = (select min(height) from usertbl);

-- 갯수(count)
select count(mobile1) as '휴대폰이 있는 사람' from usertbl;

-- having절
use sqldb;
select userID as '사용자', sum(price*amount) as '총구매액'
from buytbl
group by userID
having sum(price*amount) >1000
order by sum(price*amount);

-- rollup
-- 분류별 합계와 그 총합
select num, groupname, sum(price*amount) as'비용'
from buytbl
group by groupName, num
with rollup;


