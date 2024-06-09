#!/usr/bin/env mysql
-- Displays the average temperature (Fahrenheit) by city ordered by temp in DESC

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
