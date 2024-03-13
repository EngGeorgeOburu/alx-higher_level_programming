-- Displaying the top 3 cities temperature
SELECT city, temperature
FROM temperatures
WHERE month IN ('July', 'August')
ORDER BY temperature DESC
LIMIT 3;
