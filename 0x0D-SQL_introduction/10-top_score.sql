#!/usr/bin/env mysql
-- Lists all records of second_table. Displays both the scores and the name ordered by score in DESC

SELECT score, name FROM second_table ORDER BY score DESC;
