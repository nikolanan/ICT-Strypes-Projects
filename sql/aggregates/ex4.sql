WITH result AS(
	SELECT
		F.name,
		SUM(
			CASE
				WHEN B.memid = 0
				THEN B.slots*F.guestcost
				ELSE
					B.slots*F.membercost
			END 
		)AS revenue
	FROM cd.facilities AS F
	JOIN cd.bookings AS B
	ON B.facid = F.facid
	GROUP BY F.name
	ORDER BY revenue DESC
)

SELECT
		R.name,
		(
		    SELECT COUNT(*)
		    FROM result AS R2
		    WHERE R2.revenue > R.revenue
		) + 1 AS rank
FROM result AS R
LIMIT 3

