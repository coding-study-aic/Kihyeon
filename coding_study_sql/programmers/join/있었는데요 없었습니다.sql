select a.ANIMAL_ID, a.NAME
from ANIMAL_OUTS a
left outer join ANIMAL_INS b
on a.ANIMAL_ID = b.ANIMAL_ID
where a.DATETIME < b.DATETIME
order by b.DATETIME;