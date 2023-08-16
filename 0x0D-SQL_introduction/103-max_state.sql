--  displays the max temperature of each state
SELECT state, MAX(value) AS maximum FROM temperatures
GROUP BY state ORDER BY state;
