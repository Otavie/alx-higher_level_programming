#!/usr/bin/env mysql
-- A script that prints the full description of the table first_table from the database hbtn_0c_0 in the MySQL server

SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAUT, EXTRA FROM INFORMATION_SCHEMA.COUMNS WHERE TABLE_NAME = 'first_table' AND TABLE_SCHEMA = 'hbtn_0c_0';
