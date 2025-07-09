WITH revenue_facility AS(
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
),


classified AS (
  SELECT *,
        NTILE(3) OVER (ORDER BY revenue DESC) AS group_rank
    FROM revenue_facility

)

SELECT
	name,
	(
	    CASE
	  	    WHEN group_rank = 1
	  	    THEN 'high'
	  	    WHEN group_rank = 2
	  	    THEN 'average'
	  	    WHEN group_rank = 3
	  	    THEN 'low'
	    END 
	 ) AS revenue
	  
FROM classified
ORDER BY group_rank, revenue, name