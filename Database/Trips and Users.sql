SELECT DISTINCT
    t.request_at AS Day,
    ROUND(SUM(CASE WHEN t.status = 'cancelled_by_client' OR t.status = 'cancelled_by_driver' THEN 1 ELSE 0 END) OVER (PARTITION BY t.request_at) /
        COUNT(*) OVER (PARTITION BY t.request_at), 2) AS 'Cancellation Rate'
FROM
    Trips t
JOIN
    Users u1 ON t.client_id = u1.users_id AND u1.banned = 'No'
JOIN
    Users u2 ON t.driver_id = u2.users_id AND u2.banned = 'No'
WHERE
    t.request_at BETWEEN '2013-10-01' AND '2013-10-03';