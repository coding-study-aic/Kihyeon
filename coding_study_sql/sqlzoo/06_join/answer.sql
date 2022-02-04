-- 1
SELECt matchid, player FROM goal
  WHERE teamid = 'GER'

-- 2
SELECT id,stadium,team1,team2
  FROM game
where id = 1012

-- 3
SELECT player, teamid, stadium, mdate
  FROM game JOIN goal ON (id=matchid)
where teamid = 'GER'

-- 4
SELECT team1, team2, player
  FROM game JOIN goal ON (id=matchid)
where player LIKE 'Mario%'

-- 5
SELECT player, teamid, coach , gtime
  FROM goal a join eteam b on a. teamid = b. id
 WHERE gtime<=10

-- 6
 SELECT mdate, teamname
  FROM game a JOIN eteam b ON (a.team1=b.id)
where b.coach = 'Fernando Santos'

-- 7
SELECT b.player
  FROM game a JOIN goal b ON (a.id=b.matchid)
where a.stadium = 'National Stadium, Warsaw'

-- 8
SELECT distinct player
  FROM game JOIN goal ON matchid = id 
    WHERE (team1='GER' or team2='GER')
    and goal.teamid != 'GER'

-- 9
SELECT teamname, COUNT(*)
  FROM eteam JOIN goal ON id=teamid
group by teamname
 ORDER BY teamname

 -- 10
 SELECT stadium, COUNT(*)
  FROM game JOIN goal ON id= matchid
group by stadium

-- 11
SELECT matchid, mdate,COUNT(teamid)
  FROM game JOIN goal ON matchid = id 
 WHERE (team1 = 'POL' OR team2 = 'POL')
 group by matchid, mdate

 --12
 SELECT matchid, mdate,COUNT(teamid)
  FROM game JOIN goal ON matchid = id 
 WHERE (team1 = 'GER' OR team2 = 'GER')
 and teamid = 'GER'
 group by matchid, mdate

 --13
 SELECT mdate,team1,
  sum(CASE WHEN teamid=team1 THEN 1 ELSE 0 END) score1,
  team2,
  sum(CASE WHEN teamid=team2 THEN 1 ELSE 0 END) score2
  FROM game left JOIN goal ON matchid = id
  group by mdate, team1, team2
  ORDER BY mdate, matchid, team1, team2