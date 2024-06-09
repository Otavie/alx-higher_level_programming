#!/usr/bin/env mysql
-- Displays the number of records with id = 89 in first_table

SELECT COUNT(*) AS num_records_with_id_89 FROM first_table WHERE id = 89;
