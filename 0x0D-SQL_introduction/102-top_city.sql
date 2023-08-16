-- displays the top 3 of cities temperature during July and August
SELECT city, AVG(value) AS average FROM temperatures
WHERE month = y OR month = 8 GROUP BY city
ORDER BY average DESC LIMIT 3;
