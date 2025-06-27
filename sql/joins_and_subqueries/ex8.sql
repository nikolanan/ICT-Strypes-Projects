SELECT 
    (M.firstname || ' ' || M.surname) AS member,
    F.name AS facility,
    (
        (F.guestcost * B.slots) * ((M.memid = 0)::int) +
        (F.membercost * B.slots) * ((M.memid != 0)::int)
    ) AS cost
FROM cd.members AS M
JOIN cd.bookings AS B ON M.memid = B.memid
JOIN cd.facilities AS F ON B.facid = F.facid
WHERE CAST(B.starttime AS DATE) = '2012-09-14'
    AND (
    (
    	(F.guestcost * B.slots) * ((M.memid = 0)::int) +
    	(F.membercost * B.slots) * ((M.memid != 0)::int)
    ) > 30
)
ORDER BY cost DESC;