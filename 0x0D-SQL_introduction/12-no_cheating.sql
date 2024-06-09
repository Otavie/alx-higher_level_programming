#!/usr/bin/env mysql
-- Script that updates the score of Bob to 10 in the table second_table

UPDATE score FROM second_table WHERE name = "Bob" WITH score = 10;
