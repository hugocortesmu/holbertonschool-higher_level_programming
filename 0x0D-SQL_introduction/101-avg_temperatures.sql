-- and finds first 3 cities with average depending on month
SELECT city, AVG(value) AS avg_temp FROM `temperatures`
WHERE month BETWEEN 7 AND 8
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;