SELECT M.firstname, M.surname
FROM cd.members AS M
WHERE 
    M.memid IN (SELECT DISTINCT recommendedby 
				FROM cd.members 
				WHERE 
                    recommendedby IS NOT NULL)
ORDER BY M.surname, M.firstname