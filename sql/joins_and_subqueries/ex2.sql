SELECT B.starttime, C.name
FROM cd.bookings AS B
JOIN cd.facilities AS C
ON B.facid = C.facid
WHERE CAST(B.starttime as DATE) = '2012-09-21' AND C.name LIKE 'Tennis%'
ORDER BY B.starttime