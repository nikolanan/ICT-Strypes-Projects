SELECT 
    M1.firstname AS memfname, 
	M1.surname AS memsname,
	M2.firstname AS recfname,
	M2.surname AS rescname
FROM cd.members AS M1
LEFT JOIN cd.members AS M2
ON M1.recommendedby = M2.memid
ORDER BY M1.surname, M1.firstname
