-- 1
SELECT yr, subject, winner
  FROM nobel
 WHERE yr = 1950
-- 2
SELECT winner
  FROM nobel
 WHERE yr = 1962
   AND subject = 'Literature'

-- 3
select yr, subject
  FROM nobel
where winner = 'Albert Einstein'

-- 4
select winner
  FROM nobel
where subject = 'Peace'
and yr >= 2000

-- 5
select *
  FROM nobel
where yr between 1980 and 1989
and subject = 'Literature'

-- 6
SELECT * FROM nobel
 WHERE winner IN ('Theodore Roosevelt',
                  'Woodrow Wilson',
                  'Jimmy Carter',
                   'Barack Obama')

-- 7
SELECT winner FROM nobel
 WHERE winner like 'John%'

-- 8
SELECT yr, subject, winner FROM nobel
 WHERE subject = 'Physics'
       and yr = 1980
       or subject = 'Chemistry'
       and yr = 1984

-- 9
SELECT yr, subject, winner FROM nobel
 WHERE subject != 'Chemistry'
       and subject != 'Medicine'
       and yr = 1980

-- 10
SELECT yr, subject, winner FROM nobel
 WHERE yr < 1910
       and subject = 'Medicine'
       or yr >= 2004
       and subject = 'Literature'

 -- 11
SELECT * FROM nobel
 WHERE winner = 'PETER GRÜNBERG'

 -- 12
SELECT * FROM nobel
 WHERE winner = 'EUGENE O\'NEILL'

'
-- 13
SELECT winner, yr, subject FROM nobel
 WHERE winner like 'Sir%'

-- 14
SELECT winner, subject from nobel
 WHERE yr=1984
 ORDER BY subject IN ('Physics','Chemistry'),subject, winner asc
