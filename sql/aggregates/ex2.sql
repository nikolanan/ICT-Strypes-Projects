WITH totals AS
    (SELECT 
	    F.facid, 
	    SUM(B.slots) AS total
    FROM cd.facilities AS F
    JOIN cd.bookings AS B ON F.facid = B.facid
    GROUP BY F.facid
    ORDER BY total DESC
    LIMIT 1
)
    SELECT facid,total
    FROM totals
    WHERE total = (SELECT MAX(total) FROM totals);
