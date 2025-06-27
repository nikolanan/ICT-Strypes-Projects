SELECT DISTINCT 
        (M.firstname || ' ' ||  M.surname) AS member, 
		F.name AS facility
FROM cd.members AS M
JOIN cd.bookings AS B
ON M.memid = B.memid
JOIN cd.facilities AS F
ON B.facid = F.facid
WHERE F.name LIKE 'Tennis%'
ORDER BY member, facility