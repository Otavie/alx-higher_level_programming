#!/usr/bin/env mysql
-- Script to display the max temperature of each state ordered by state name

SELECT state, MAX(value) FROM temperatures ORDER BY state DESC;
