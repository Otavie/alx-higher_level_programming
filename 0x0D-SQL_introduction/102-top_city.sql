#!/usr/bin/env mysql
-- Script to display the top 3 cities

SELECT city, AVG(value) AS max_temp FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY max_temp DESC LIMIT 3;
