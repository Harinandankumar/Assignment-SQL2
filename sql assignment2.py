#!/usr/bin/env python
# coding: utf-8

# Q-1. Write an SQL query to print the first three characters of FIRST_NAME from Worker table.
# 
# 
# 
# Ans: SELECT SUBSTRING(FIRST_NAME,1,3) FROM Worker;

# Q-2. Write an SQL query to find the position of the alphabet (‘a’) in the first name column ‘Amitabh’ from Worker table.

# # Apporach 1
# SELECT LOCATE('a',FIRST_NAME) FROM Worker WHERE FIRST_NAME = 'Amitabh';
# # Approach 2
# SELECT POSITION('a' IN FIRST_NAME) FROM Worker WHERE FIRST_NAME = 'Amitabh';

# Q-3. Write an SQL query to print the name of employees having the highest salary in each department.
# 
# 
# 
# 
# Ans: SELECT first_name, last_name, salary, department FROM Worker w WHERE salary = (SELECT MAX(salary) FROM Worker WHERE department = w.department)
