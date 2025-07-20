SELECT name, month, 
	round((100*slots)/
		cast(
			25*(cast((month + interval '1 month') AS date)
			- cast (month AS date)) AS numeric),1) AS utilisation
	FROM  (
		SELECT facs.name AS name, date_trunc('month', starttime) AS month, sum(slots) as slots
			FROM cd.bookings bks
			inner JOIN cd.facilities facs
				ON bks.facid = facs.facid
			group BY facs.facid, month
	) AS inn
ORDER BY name, month   