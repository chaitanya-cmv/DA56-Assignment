create database AI_Integration;
use AI_Integration;

ALTER TABLE car_data
MODIFY Car_Name VARCHAR(100),
MODIFY Min_Price_Lakh DECIMAL(10,2),
MODIFY Max_Price_Lakh DECIMAL(10,2),
MODIFY Range_Kmpl DECIMAL(6,2),
MODIFY CC INT,
MODIFY Seats INT,
MODIFY Variants INT,
MODIFY Car_Type VARCHAR(50),
MODIFY Ex_Showroom_Price INT,
MODIFY RTO INT,
MODIFY Insurance INT,
MODIFY Other_Charges INT,
MODIFY Onroad_Price INT;

drop database AI_Integration;
create database AI_Integration;
select * from car_data;