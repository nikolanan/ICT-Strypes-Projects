SELECT 
	(SELECT COUNT(*)
	    FROM cd.members AS M2
	    WHERE M2.joindate <= M1.joindate) AS row_number, 
	M1.firstname, 
	M1.surname
FROM cd.members AS M1
ORDER BY M1.joindate