# 0x0D. SQL - Introduction

This repository contains SQL scripts to perform various tasks related to database management using MySQL server. Below is a brief overview of each script along with its purpose and filename:

## Scripts Overview

### 0-list_databases.sql
This script lists all databases of the MySQL server.

### 1-create_database_if_missing.sql
Creates the database `hbtn_0c_0` in the MySQL server. If the database already exists, the script does not fail.

### 2-remove_database.sql
Deletes the database `hbtn_0c_0` from the MySQL server. If the database doesn’t exist, the script does not fail.

### 3-list_tables.sql
Lists all the tables of a specified database in the MySQL server.

### 4-first_table.sql
Creates a table called `first_table` with specified columns (`id INT`, `name VARCHAR(256)`) in the current database. If the table already exists, the script does not fail.

### 5-full_table.sql
Prints the full description of the table `first_table` from the database `hbtn_0c_0`.

### 6-list_values.sql
Lists all rows of the table `first_table` from the database `hbtn_0c_0`.

### 7-insert_value.sql
Inserts a new row in the table `first_table` (database `hbtn_0c_0`) with specified values.

### 8-count_89.sql
Displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0`.

### 9-full_creation.sql
Creates a table `second_table` in the database `hbtn_0c_0` and adds multiple rows.

### 10-top_score.sql
Lists all records of the table `second_table` of the database `hbtn_0c_0`, ordered by score (top first).

### 11-best_score.sql
Lists all records with a score >= 10 in the table `second_table` of the database `hbtn_0c_0`, ordered by score (top first).

### 12-no_cheating.sql
Updates the score of Bob to 10 in the table `second_table` without using Bob’s id value.

### 13-change_class.sql
Removes all records with a score <= 5 in the table `second_table` of the database `hbtn_0c_0`.

### 14-average.sql
Computes the score average of all records in the table `second_table` of the database `hbtn_0c_0`.

### 15-groups.sql
Lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0`, sorted by the number of records (descending).

### 16-no_link.sql
Lists all records of the table `second_table` of the database `hbtn_0c_0` without rows without a name value, ordered by descending score.

### 100-move_to_utf8.sql
Converts the database `hbtn_0c_0` and its tables/fields to UTF8 format.

### 101-avg_temperatures.sql
Displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

### 102-top_city.sql
Displays the top 3 cities' temperatures during July and August ordered by temperature (descending).

### 103-max_state.sql
Displays the max temperature of each state ordered by state name.

