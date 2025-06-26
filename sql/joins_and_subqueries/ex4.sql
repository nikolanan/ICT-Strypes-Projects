SELECT 
    M1.firstname as memfname, 
	M1.surname as memsname,
	M2.firstname as recfname,
	M2.surname as rescname
FROM cd.members as M1
LEFT JOIN cd.members AS M2
ON M1.recommendedby = M2.memid
ORDER BY M1.surname, M1.firstname
