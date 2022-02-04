-- 1
SELECT name FROM world
  WHERE population >
     (SELECT population FROM world
      WHERE name='Russia')

-- 2
SELECT name FROM world
  WHERE gdp/population >
     (SELECT gdp/population FROM world
      WHERE name='United Kingdom')
  and continent = 'Europe'

-- 3
SELECT name, continent FROM world
  WHERE continent in
     (SELECT continent FROM world
      WHERE name='Argentina' or name='Australia')
order by name

-- 4
SELECT name, population FROM world
  WHERE population >
     (SELECT population FROM world
      WHERE name='Canada')
     and population < 
     (SELECT population FROM world
      WHERE name='Poland')

-- 5
SELECT name, round(population/(select population from world where name = 'Germany') * 100) || '%' FROM world
  WHERE continent = 'Europe'

-- 6
SELECT name FROM world
  WHERE gdp >= ALL(select gdp from world where continent = 'Europe')

-- 7
SELECT continent , name, area FROM world x
  WHERE area >= all
    (SELECT area FROM world y
        WHERE y.continent=x.continent)

-- 8
SELECT continent , name FROM world x
  WHERE name <= all
    (SELECT name FROM world y
        WHERE y.continent=x.continent)

-- 9
SELECT name, continent , population FROM world x
  WHERE 25000000 >= all
    (SELECT population FROM world y
        WHERE y.continent=x.continent)

-- 10
SELECT name, continent FROM world x
  WHERE population >= all
    (SELECT population*3 FROM world y
        WHERE y.continent=x.continent
and y.name!=x.name)
