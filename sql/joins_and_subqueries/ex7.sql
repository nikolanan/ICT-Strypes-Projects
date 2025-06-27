SELECT DISTINCT
	(M1.firstname || ' ' || M1.surname) AS member,
	(SELECT M2.firstname || ' ' || M2.surname FROM cd.members AS M2
	WHERE M1.recommendedby = M2.memid) AS recommender
FROM cd.members AS M1
ORDER BY member