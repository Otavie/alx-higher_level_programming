#!/usr/bin/env mysql
-- Lists all records of second_table with socre >= 10. Displays both scores and the name ordered by score in DESC

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
