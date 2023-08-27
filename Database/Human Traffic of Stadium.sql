WITH q1 AS (
    SELECT *,
           COUNT(*) OVER (ORDER BY id RANGE BETWEEN CURRENT ROW AND 2 FOLLOWING) AS following_cnt,
           COUNT(*) OVER (ORDER BY id RANGE BETWEEN 2 PRECEDING AND CURRENT ROW) AS preceding_cnt,
           COUNT(*) OVER (ORDER BY id RANGE BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS current_cnt
    FROM Stadium
    WHERE people >= 100
)
SELECT id, visit_date, people
FROM q1
WHERE following_cnt >= 3 OR preceding_cnt >= 3 OR current_cnt >= 3
ORDER BY visit_date;