-------------------CREATE TABLES-------------------
---------------------------------------------------
-- Department
---------------------------------------------------
CREATE TABLE Department(
  Department_Id INT,
  Department_Name VARCHAR(30),
  CONSTRAINT DEPARTMENT_PK PRIMARY KEY (Department_Id)
);

---------------------------------------------------
-- Employee
---------------------------------------------------
CREATE TABLE Employee(
  Employee_Id INT,
  First_Name VARCHAR(25),
  Last_Name VARCHAR(25),
  Hire_Date DATE,
  City VARCHAR(25),
  State VARCHAR(25),
  Department_Id INT,
  CONSTRAINT EMPLOYEE_PK PRIMARY KEY (Employee_Id),
  FOREIGN KEY (Department_Id)
        REFERENCES Department(Department_Id)
);

---------------------------------------------------
-- AccountDetails
---------------------------------------------------
CREATE TABLE AccountDetails(
  Account_Id INT,
  Bank_Name VARCHAR(50),
  Account_INT VARCHAR(50),
  Employee_Id INT,
  CONSTRAINT Account_PK PRIMARY KEY (Account_Id),
  FOREIGN KEY (Employee_Id)
        REFERENCES Employee(Employee_Id)
);

-------------------------------------------------
-- Salary
-------------------------------------------------
CREATE TABLE Salary(
  Salary_Id INT,
  Gross_Salary INT,
  Hourly_Pay INT,
  State_Tax INT,
  Federal_Tax INT,
  Account_Id INT,
  CONSTRAINT SALARY_PK PRIMARY KEY (Salary_Id),
  FOREIGN KEY (Account_Id)
        REFERENCES AccountDetails(Account_Id)
);

--------------------------------------------------
-- Project
--------------------------------------------------
CREATE TABLE Project(
  Project_Id INT,
  Project_Name VARCHAR(50),
  Project_Description VARCHAR(50),
  CONSTRAINT Project_PK PRIMARY KEY (Project_Id)
);

-------------------------------------------------
-- DepartmentProject Bridge
-------------------------------------------------
CREATE TABLE DepartmentProject(
  Department_Id INT,
  Project_Id INT,
  CONSTRAINT DEPTPROJECT_PK PRIMARY KEY (Department_Id,Project_Id),
  FOREIGN KEY (Department_Id)
        REFERENCES Department(Department_Id),
  FOREIGN KEY (Project_Id)
        REFERENCES Project(Project_Id)
);

---------------------------------------------------
-- Education
---------------------------------------------------
CREATE TABLE Education(
  Education_Id INT,
  Employee_Id INT,
  Degree VARCHAR(30),
  Graduation_Year INT,
  CONSTRAINT Location_PK PRIMARY KEY (Education_Id),
  FOREIGN KEY (Employee_Id)
        REFERENCES Employee(Employee_Id)
);

---------------------------------------------------
-- Leave
---------------------------------------------------
CREATE TABLE Leave(
  Leave_Id INT,
  Employee_Id INT,
  Leave_date DATE,
  CONSTRAINT Leave_PK PRIMARY KEY (Leave_Id),
  FOREIGN KEY (Employee_Id)
        REFERENCES Employee(Employee_Id)
);
  
----------------------------------------------------
-- Attendance
----------------------------------------------------
CREATE TABLE Attendance(
  Attendance_Id INT,
  Hours_Worked INT,
  CONSTRAINT Attendance_PK PRIMARY KEY (Attendance_Id)
);
  
----------------------------------------------------
-- EmployeeAttendance Bridge
----------------------------------------------------
CREATE TABLE Employee_Attendance(
  Employee_Id INT,
  Attendance_Id INT,
  CONSTRAINT DEPARTMENTPROJECT_PK PRIMARY KEY (Employee_Id,Attendance_Id),
  FOREIGN KEY (Employee_Id)
        REFERENCES Employee(Employee_Id),
  FOREIGN KEY (Attendance_Id)
        REFERENCES Attendance(Attendance_Id)
);

----------------------------------------------------
-- WorkLocation
----------------------------------------------------
CREATE TABLE Work_Location(
  Location_Id INT,
  Location VARCHAR(25),
  INT_Of_Employees INT,
  City VARCHAR(25),
  State VARCHAR(25),
  Employee_Id INT,
  CONSTRAINT Loc_PK PRIMARY KEY (Location_Id),
  FOREIGN KEY (Employee_Id)
        REFERENCES Employee(Employee_Id)
);



---------------------------------------------------
--INSERT INTO TABLES--
---------------------------------------------------

INSERT INTO Department VALUES (1,'Human Resources');
INSERT INTO Department VALUES (2,'Software Development');
INSERT INTO Department VALUES (3,'Data Analysis');
INSERT INTO Department VALUES (4,'Data Science');
INSERT INTO Department VALUES (5,'Business Intelligence');
INSERT INTO Department VALUES (6,'Data Engineering');
INSERT INTO Department VALUES (7,'Manufacturing');
INSERT INTO Department VALUES (8,'Quality Control');

INSERT INTO Employee VALUES (101,'Ojas','Phansekar',to_date('14-APR-16', 'dd-MON-yy'),'New York City','New York',1);
INSERT INTO Employee VALUES (102,'Vrushali','Patil',to_date('21-JUN-18', 'dd-MON-yy'),'Boston','Massachusetts',2);
INSERT INTO Employee VALUES (103,'Pratik','Parija',to_date('13-SEP-19', 'dd-MON-yy'),'Chicago','Illinois',3);
INSERT INTO Employee VALUES (104,'Chetan','Mistry',to_date('12-APR-11', 'dd-MON-yy'),'Miami','Florida',4);
INSERT INTO Employee VALUES (105,'Anugraha','Varkey',to_date('16-AUG-17', 'dd-MON-yy'),'Atlanta','Georgia',5);
INSERT INTO Employee VALUES (106,'Rasagnya','Reddy',to_date('25-JUL-18', 'dd-MON-yy'),'San Mateo','California',6);
INSERT INTO Employee VALUES (107,'Aishwarya','Boralkar',to_date('18-DEC-10', 'dd-MON-yy'),'San Francisco','California',7);
INSERT INTO Employee VALUES (108,'Shantanu','Savant',to_date('27-NOV-15', 'dd-MON-yy'),'Seattle','Washington',8);
INSERT INTO Employee VALUES (109,'Kalpita','Malvankar',to_date('24-APR-16', 'dd-MON-yy'),'Boston','Massachusetts',8);
INSERT INTO Employee VALUES (110,'Saylee','Bhagat',to_date('21-MAY-14', 'dd-MON-yy'),'San Francisco','California',7);
INSERT INTO Employee VALUES (111,'Priyanka','Jonas',to_date('14-NOV-16', 'dd-MON-yy'),'New York City','New York',1);
INSERT INTO Employee VALUES (112,'John','Vincent',to_date('21-JUN-18', 'dd-MON-yy'),'Boston','Massachusetts',2);
INSERT INTO Employee VALUES (113,'Pratik','Panhale',to_date('13-SEP-19', 'dd-MON-yy'),'Chicago','Illinois',3);

INSERT INTO Project VALUES (21,'Dev','Whatever');
INSERT INTO Project VALUES (22,'Prod','do something');
INSERT INTO Project VALUES (23,'Test','focus');
INSERT INTO Project VALUES (24,'Nothing','do nothing');
INSERT INTO Project VALUES (25,'Research','focus on everything');
INSERT INTO Project VALUES (26,'Next Steps','find some way out');

INSERT INTO AccountDetails VALUES (40,'Santander','S12344',101);
INSERT INTO AccountDetails VALUES (41,'Santander','S12345',102);
INSERT INTO AccountDetails VALUES (42,'Santander','S12346',103);
INSERT INTO AccountDetails VALUES (43,'Santander','S12347',104);
INSERT INTO AccountDetails VALUES (44,'Chase','C12344',105);
INSERT INTO AccountDetails VALUES (45,'Chase','C12345',106);
INSERT INTO AccountDetails VALUES (46,'Chase','C12347',107);
INSERT INTO AccountDetails VALUES (47,'Chase','C12334',108);
INSERT INTO AccountDetails VALUES (48,'BOFA','C12378',109);
INSERT INTO AccountDetails VALUES (49,'BOFA','C12390',110);

INSERT INTO Education VALUES (10,101,'MS',2017);
INSERT INTO Education VALUES (11,102,'MS',2019);
INSERT INTO Education VALUES (12,104,'MS',2011);
INSERT INTO Education VALUES (13,108,'MS',2015);
INSERT INTO Education VALUES (14,109,'Bachelor',2013);
INSERT INTO Education VALUES (15,107,'Bachelor',2008);
INSERT INTO Education VALUES (16,106,'Bachelor',2007);

INSERT INTO Leave VALUES (51,104,to_date('1-DEC-19', 'dd-MON-yy'));
INSERT INTO Leave VALUES (52,108,to_date('2-DEC-19', 'dd-MON-yy'));
INSERT INTO Leave VALUES (53,109,to_date('3-DEC-19', 'dd-MON-yy'));
INSERT INTO Leave VALUES (54,107,to_date('4-DEC-19', 'dd-MON-yy'));
INSERT INTO Leave VALUES (55,106,to_date('5-DEC-19', 'dd-MON-yy'));
INSERT INTO Leave VALUES (56,104,to_date('6-DEC-19', 'dd-MON-yy'));
INSERT INTO Leave VALUES (57,108,to_date('7-DEC-19', 'dd-MON-yy'));
INSERT INTO Leave VALUES (58,109,to_date('7-DEC-19', 'dd-MON-yy'));
INSERT INTO Leave VALUES (59,107,to_date('8-DEC-19', 'dd-MON-yy'));
INSERT INTO Leave VALUES (60,106,to_date('9-DEC-19', 'dd-MON-yy'));

INSERT INTO Attendance VALUES (90,10);
INSERT INTO Attendance VALUES (91,20);
INSERT INTO Attendance VALUES (92,30);
INSERT INTO Attendance VALUES (93,40);
INSERT INTO Attendance VALUES (94,45);
INSERT INTO Attendance VALUES (95,56);
INSERT INTO Attendance VALUES (96,58);

INSERT INTO Work_Location VALUES (71,'North',4,'New York City','New York',101);
INSERT INTO Work_Location VALUES (72,'North',4,'Boston','Massachusetts',102);
INSERT INTO Work_Location VALUES (73,'North',4,'Chicago','Illinois',103);
INSERT INTO Work_Location VALUES (74,'North',89,'Miami','Florida',104);
INSERT INTO Work_Location VALUES (75,'South',90,'Atlanta','Georgia',105);
INSERT INTO Work_Location VALUES (76,'South',100,'San Mateo','California',106);
INSERT INTO Work_Location VALUES (77,'South',4,'San Francisco','California',107);
INSERT INTO Work_Location VALUES (78,'South',2,'Seattle','Washington',108);
INSERT INTO Work_Location VALUES (79,'South',25,'Alpharetta','Georgia',109);
INSERT INTO Work_Location VALUES (80,'South',20,'Keene','New Hampshire',110);
INSERT INTO Work_Location VALUES (81,'South',22,'Hampton','New Hampshire',109);

INSERT INTO Employee_Attendance VALUES (101,90);
INSERT INTO Employee_Attendance VALUES (102,91);
INSERT INTO Employee_Attendance VALUES (103,92);
INSERT INTO Employee_Attendance VALUES (104,93);
INSERT INTO Employee_Attendance VALUES (105,94);
INSERT INTO Employee_Attendance VALUES (106,95);
INSERT INTO Employee_Attendance VALUES (107,96);
INSERT INTO Employee_Attendance VALUES (108,91);
INSERT INTO Employee_Attendance VALUES (109,92);
INSERT INTO Employee_Attendance VALUES (110,93);

INSERT INTO DepartmentProject VALUES (1,21);
INSERT INTO DepartmentProject VALUES (2,22);
INSERT INTO DepartmentProject VALUES (3,23);
INSERT INTO DepartmentProject VALUES (4,24);
INSERT INTO DepartmentProject VALUES (5,25);
INSERT INTO DepartmentProject VALUES (6,26);
INSERT INTO DepartmentProject VALUES (7,21);
INSERT INTO DepartmentProject VALUES (8,24);

INSERT INTO Salary VALUES (1,57600,30,200,1000,40);
INSERT INTO Salary VALUES (2,76800,40,300,1300,41);
INSERT INTO Salary VALUES (3,96000,50,400,1500,42);
INSERT INTO Salary VALUES (4,115200,60,500,1700,43);
INSERT INTO Salary VALUES (5,57600,30,200,1000,44);
INSERT INTO Salary VALUES (6,76800,40,300,1300,45);
INSERT INTO Salary VALUES (7,96000,50,400,1500,46);
INSERT INTO Salary VALUES (8,115200,60,500,1700,47);
INSERT INTO Salary VALUES (9,57600,30,200,1000,48);
INSERT INTO Salary VALUES (10,76800,40,300,1300,49);

-- create table Salary_External (
--   Salary_Id INT,
--   Gross_Salary INT,
--   Hourly_Pay INT,
--   State_Tax INT,
--   Federal_Tax INT,
--   Account_Id INT
-- )
-- organization external (
-- 	type oracle_loader
-- 	default directory ext_Salaries
-- 	access parameters (
-- 		fields terminated by ',' )
-- 	location ('Salary.csv')
-- )
-- reject limit unlimited
-- /


