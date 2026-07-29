CREATE DATABASE EMPLOYEE;
USE EMPLOYEE;

CREATE TABLE departments( 
department_id int primary key auto_increment,
department_name VARCHAR (100) unique not null);

CREATE TABLE employees(
employee_id int PRIMARY KEY AUTO_INCREMENT,
employee_name varchar(50),
gender enum ('M','F'),
age int,
hire_date date,
designation varchar(100),
department_id int,
location_id int, 
SALARY decimal(10,2),
FOREIGN KEY (department_id) references departments(department_id));

CREATE TABLE location(
location_id int,
location VARCHAR(30),
FOREIGN KEY (location_id) REFERENCES employees(location_id));

ALTER TABLE EMPLOYEES ADD email varchar(50);
ALTER TABLE employees MODIFY designation varchar(100);
ALTER TABLE employees DROP column age;
ALTER TABLE employees rename column hire_date to date_of_joining;

 RENAME table departments to department_info;
 RENAME table location to locations;
 
 TRUNCATE table employees;
 
 DROP table employees;
 DROP database employees;
 
CREATE DATABASE EMPLOYEE;
USE EMPLOYEE;

CREATE TABLE departments( 
department_id int primary key auto_increment,
department_name VARCHAR (100) unique not null);

CREATE TABLE employees(
employee_id int PRIMARY KEY AUTO_INCREMENT,
employee_name varchar(50),
gender enum ('M','F'),
age int,
hire_date date,
designation varchar(100),
department_id int,
location_id int, 
SALARY decimal(10,2),
FOREIGN KEY (department_id) references departments(department_id));

CREATE TABLE location(
location_id int primary key,
location VARCHAR(30),
FOREIGN KEY (location_id) references employees(location_id));

select distinct department_id from department;
select distinct location from location;

ALTER TABLE location MODIFY location VARCHAR(30) UNIQUE NOT NULL;

SELECT distinct employee_name from employees;
SELECT employee_name from employee;

SELECT * FROM employee where gender="F";
SELECT * FROM employee where age>=18;
UPDATE employees set hire_date=curdate() where hire_date is null;
