-- 1
select count(*)
from stops

-- 2
select id
from stops
where name = 'Craiglockhart'

-- 3
select a.id, a.name
from stops a join route b on a.id = b.stop
where b.num = '4' and b.company = 'LRT'

-- 4
SELECT company, num, COUNT(*)
FROM route WHERE stop=149 OR stop=53
GROUP BY company, num
having COUNT(*) = 2

-- 5
SELECT a.company, a.num, a.stop, b.stop
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
WHERE a.stop = 53 and b.stop = 149

-- 6
SELECT a.company, a.num, stopa.name, stopb.name
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
  JOIN stops stopa ON (a.stop=stopa.id)
  JOIN stops stopb ON (b.stop=stopb.id)
WHERE stopa.name='Craiglockhart'
and stopb.name='London Road'

-- 7
select distinct a.company, a.num
from route a join route b on (a.num = b.num and a.company = b.company)
where a.stop = 115 and b.stop = 137

-- 8
select distinct a.company, a.num
from route a join route b on (a.num = b.num and a.company = b.company)
JOIN stops stopa ON (a.stop=stopa.id)
JOIN stops stopb ON (b.stop=stopb.id)
where stopa.name = 'Craiglockhart' and stopb.name = 'Tollcross'

-- 9
select distinct name, b.company, b.num
from route a join stops on stops.id=a.stop
join route b on a.company=b.company AND a.num=b.num
where b.stop =(select id from stops where name= 'Craiglockhart')

-- 10
select a.num, a.company, name, c.num, c.company
from route a join route b on (a.num = b.num and a.company = b.company) 
join stops on id = a.stop
join route c on stops.id=c.stop
join route d on c.company=d.company AND c.num=d.num
where b.stop =(select id from stops where name= 'Craiglockhart')
and d.stop =(select id from stops where name= 'Lochend')
order by a.num, name, c.num