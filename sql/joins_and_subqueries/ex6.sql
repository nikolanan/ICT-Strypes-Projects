SELECT 
	(M.firstname || ' ' || M.surname) AS member,
	F.name AS facility,
	CASE
		WHEN M.memid = 0 THEN
			F.guestcost * B.slots
		ELSE
			F.membercost * B.slots
	END AS cost
FROM cd.members AS M
JOIN cd.bookings AS B
ON M.memid = B.memid
JOIN cd.facilities AS F
ON B.facid = F.facid
WHERE CAST(B.starttime AS DATE) = '2012-09-14' 
		AND ((M.memid = 0 AND (F.guestcost * B.slots) > 30)
            OR (M.memid != 0 AND (F.membercost * B.slots) > 30))
ORDER BY cost DESC
