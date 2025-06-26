SELECT 
	(M.firstname || ' ' || M.surname) as member,
	F.name as facility,
	CASE
		WHEN M.memid = 0 THEN
			F.guestcost * B.slots
		ELSE
			F.membercost * B.slots
	END AS cost
FROM cd.members as M
JOIN cd.bookings as B
ON M.memid = B.memid
JOIN cd.facilities as F
ON B.facid = F.facid
WHERE CAST(B.starttime AS DATE) = '2012-09-14' 
		and ((M.memid = 0 and (F.guestcost * B.slots) > 30)
            or(M.memid != 0 and (F.membercost * B.slots) > 30))
ORDER BY cost DESC
