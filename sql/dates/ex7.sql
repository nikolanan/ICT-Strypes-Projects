SELECT (date_trunc('month',ts.testts) + interval '1 month') 
		- date_trunc('day', ts.testts) AS remaining
	FROM (SELECT timestamp '2012-02-11 01:00:00' AS testts) ts  