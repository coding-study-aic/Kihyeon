WITH RECURSIVE hours  AS (      ## TIMETABLE 이름의 임시 테이블 생성
        SELECT 0 AS HOUR                ## 0으로 HOUR 컬럼의 초기값 설정
        UNION ALL                       ## 밑의 문 수행
        SELECT HOUR + 1 FROM hours  ## 테이블의 HOUR 컬럼을 1씩 증가
        WHERE HOUR < 23                 ## HOUR가 23 이전까지
    )    

select a.HOUR, count(hour(b.DATETIME)) as COUNT
from hours a left join ANIMAL_OUTS b on a.HOUR = hour(b.DATETIME)
group by a.HOUR
order by a.HOUR;