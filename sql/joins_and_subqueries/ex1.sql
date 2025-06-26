SELECT starttime
FROM cd.bookings AS B
JOIN cd.members AS M
ON B.memid = M.memid
WHERE M.firstname = 'David' AND M.surname = 'Farrell'