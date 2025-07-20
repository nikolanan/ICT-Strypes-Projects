SELECT 	extract(month FROM cal.month) AS month,
	(cal.month + interval '1 month') - cal.month AS length
	FROM
	(
		SELECT generate_series(timestamp '2012-01-01', timestamp '2012-12-01', interval '1 month') AS month
	) cal
ORDER BY month;          