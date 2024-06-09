#!/usr/bin/env mysql
-- Scripts that lists all records of the second_table excluding rows without a name

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
