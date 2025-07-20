SELECT 
    F.name,
    F.initialoutlay / (
        (SUM(
            CASE 
                WHEN B.memid = 0 THEN B.slots * F.guestcost
                ELSE B.slots * F.membercost
            END
        ) / 3) - F.monthlymaintenance
    ) AS months
FROM cd.facilities AS F
JOIN cd.bookings AS B
    ON F.facid = B.facid
GROUP BY F.name, F.initialoutlay, F.monthlymaintenance
ORDER BY F.name;
