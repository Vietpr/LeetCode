# Write your MySQL query statement below

SELECT name FROM customer WHERE id IN (SELECT id FROM customer WHERE referee_id !=2 OR referee_id IS null )

