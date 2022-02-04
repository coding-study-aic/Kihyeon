-- 1
SELECT SUM(population)
FROM world

-- 2
SELECT distinct continent
FROM world

-- 3
SELECT sum(gdp)
FROM world
where continent = 'Africa'

-- 4
SELECT count(*)
FROM world
where area >= 1000000

-- 5
SELECT sum(population)
FROM world
where name in ('Estonia', 'Latvia', 'Lithuania')

-- 6
SELECT continent, count(name)
FROM world
group by continent

-- 7
SELECT continent, count(name)
FROM world
where population >= 10000000
group by continent

-- 8
SELECT continent
FROM world
group by continent
having sum(population) >= 100000000
