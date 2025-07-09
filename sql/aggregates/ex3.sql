WITH member_by_hours AS (
	SELECT firstname, 
			surname, 
			((((SUM(B.slots)/2)+5)/10)*10) AS hours
	FROM cd.members AS M
	JOIN cd.bookings AS B
	ON M.memid = B.memid
	GROUP BY M.memid
)

SELECT
	MH.firstname,
	MH.surname,
	MH.hours,
	(
	    SELECT COUNT(*)
	    FROM member_by_hours AS MH2
	    WHERE MH2.hours > MH.hours
	) + 1 AS rank

FROM member_by_hours AS MH
ORDER BY rank ASC, MH.surname ASC, MH.firstname ASC
