WITH RECURSIVE recs(recommender) AS (
	SELECT recommendedby
	FROM cd.members
	WHERE memid = 27

	UNION ALL

	SELECT m.recommendedby
	FROM cd.members m
	JOIN recs r ON m.memid = r.recommender
)
SELECT r.recommender, m.firstname, m.surname
FROM recs r
JOIN cd.members m ON r.recommender = m.memid
ORDER BY r.recommender DESC;
