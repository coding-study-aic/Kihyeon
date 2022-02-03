<GROUP BY 입양시각 구하기(2)>
WITH RECURSIVE TIMETABLE  AS (      ## TIMETABLE 이름의 임시 테이블 생성
    SELECT 0 AS HOUR                ## 0으로 HOUR 컬럼의 초기값 설정
    UNION ALL                       ## 밑의 문 수행
    SELECT HOUR + 1 FROM TIMETABLE  ## 테이블의 HOUR 컬럼을 1씩 증가
    WHERE HOUR < 23                 ## HOUR가 23 이전까지
)

SELECT T.HOUR, count(hour(A.datetime)) as COUNT
from TIMETABLE as T
left join ANIMAL_OUTS as A
on hour(A.datetime) = T.HOUR
group by T.HOUR
order by T.HOUR;

### 0으로 채워진 임시 테이블을 만들고 싶을 때 with 이용. 
### recursive 이용해서 반복문처럼 사용 가능

<NULL 처리하기>
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') as NAME, SEX_UPON_INTAKE 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC

## IFNULL은 만약 그 값이 NAME이라면 'No name'으로 바꾼다는 의미

<중복 제거>
distinct(name)

<if 문>
select ANIMAL_ID, NAME, if(SEX_UPON_INTAKE like 'Intact%', 'X', 'O') as 중성화
from ANIMAL_INS
order by ANIMAL_ID

<case 문>
SELECT ANIMAL_ID, NAME, 
    CASE WHEN SEX_UPON_INTAKE LIKE 'Intact%' THEN 'X' 
    ELSE 'O' END as 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

<date>
DATE_FORMAT(날짜 , 형식) : 날짜를 지정한 형식으로 출력
%Y '4자리 년도'
%m '숫자 월 ( 두자리 )'
%y '2자리 년도'
%c '숫자 월(한자리는 한자리)'
%M '긴 월(영문)'
%d '일자 (두자리)'
%b '짧은 월(영문)'
%e '일자(한자리는 한자리)'
%W '긴 요일 이름(영문)'
%I '시간 (12시간)'
%a '짧은 요일 이름(영문)'
%H '시간(24시간)'
%i '분'
%r 'hh:mm:ss AM,PM'
%T 'hh:mm:SS'
%S '초'