SELECT starttime, 
	   starttime + (30 * slots) * INTERVAL '1 minute' AS endtime
FROM cd.bookings
ORDER BY endtime DESC, starttime DESC
LIMIT 10