CREATE DATABASE Tablevation;
USE Tablevation;

CREATE TABLE Restaurant(
Restaurant_Email VARCHAR(50) PRIMARY KEY,
Restaurant_Password VARCHAR(50) NOT NULL,
Name VARCHAR(50) NOT NULL,
Address_Line1 VARCHAR(50) NOT NULL,
Area VARCHAR(15) NOT NULL,
City VARCHAR(35) DEFAULT 'Portsmouth',
County VARCHAR(35) DEFAULT 'Hampshire',
PostCode VARCHAR(8) NOT NULL,
Rating INT NULL,
Booked_Seats INT DEFAULT 0,
Contact_Number VARCHAR(15) NOT NULL,
MondayToFriday_OT Time NOT NULL,
MondayToFriday_CT Time NOT NULL,
Sat_OT TIME NOT NULL,
Sat_CT TIME NOT NULL,
Sun_OT TIME NOT NULL,
Sun_CT TIME NOT NULL,
Food_Type VARCHAR(15) NOT NULL,
Total_No_Seats INT NOT NULL
);

CREATE TABLE Customer(
Customer_Email VARCHAR(50) PRIMARY KEY,
Customer_Password VARCHAR(50) NOT NULL,
Forename VARCHAR(50) NOT NULL,
Surname VARCHAR(50) NOT NULL,
Contact_Number VARCHAR(15) NOT NULL
);

CREATE TABLE Reservation(
ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
Restaurant_Name VARCHAR(50) NOT NULL,
Restaurant_Email VARCHAR(50) NOT NULL,
Customer_Email VARCHAR(50) NOT NULL,
Booked_Date TIMESTAMP NOT NULL,
No_Guests INT NOT NULL,
Details VARCHAR(100) NULL,
CONSTRAINT FOREIGN KEY (Customer_Email) REFERENCES Customer(Customer_Email),
CONSTRAINT FOREIGN KEY (Restaurant_Email) REFERENCES Restaurant(Restaurant_Email)
);

/*
Queries:

Creating Accounts- (Create User Account) (Create Restaurant Account)
INSERT INTO Customer VALUES (?,?,?,?,?); ALL FIELDS
INSERT INTO Customer VALUES ("jeanaldread@gmail.com","Aldread123","Jean","Aldread","07578260657");
INSERT INTO Customer  values ('cfernandez0@mozilla.com', 'utG3fgPlq', 'Catherine', 'Fernandez', '07551453898');
INSERT INTO Customer values ('scarroll1@hatena.ne.jp', 'wQ0C1237u', 'Sara', 'Carroll', '07562651291');
INSERT INTO Customer  values ('ahunt2@simplemachines.org', 'OTFNS9QeMiC6', 'Antonio', 'Hunt', '07562420453');
INSERT INTO Customer  values ('rgarcia3@dropbox.com', '3yRcKY73', 'Ruth', 'Garcia', '07562651453');

INSERT INTO Restaurant VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); ALL EXCEPT BOOKED_SEATS
insert into Restaurant values ('jlittle0@flavors.me', 'WhT6Vwo', 'Goyette-Wilkinson', '23 Newland road', 'NorthEnd', 'Portsmouth', 'Hampshire', 'PO59Ik', 4, 0, '02301 234587', '9:00', '22:00', '10:00', '22:00', '10:00', '20:00', 'Indian Cousine', 90);
insert into Restaurant values ('SpicyFlame.co.uk', '7TeAiVk1uj', 'SpicyFlame', '1-3 Rowlands road', 'Southsea', 'Portsmouth', 'Hampshire', 'PO2B12', 3, 0, '02301 23456', '9:00', '22:00', '10:00', '23:00', '10:00', '20:00', 'Vegan', 34);
insert into Restaurant values ('lrose2@examiner.com', 'JXcwpZhhJFcs', 'Hettinger', '96 Queens road', 'GunWarf Quays', 'Portsmouth', 'Hampshire', 'PO1T16', 3, 0, '02301 454458', '9:00', '22:00', '10:00', '22:00', '10:00', '22:00', 'Chinese Buffet', 36);
insert into Restaurant  values ('acarroll3@senate.gov', '3EEqQkJQ', 'Denesik-Rohan', '4 Jessie road', 'Southsea', 'Portsmouth', 'Hampshire', 'PO9H43', 1, 0, '02301 234580', '9:00', '22:00', '10:00', '22:00', '10:00', '20:00', 'Thai', 35);

Making a Reservation- (Book Table)
INSERT INTO Reservation VALUES (?,?,?,?,?,?); ALL EXCEPT ID
INSERT INTO Reservation VALUES(0,`SpicyFlame`,`SpicyFlame.co.uk`,`jeanaldread@gmail.com`,`16:00`,`23-09-2017`,20,`a birthday reservation for Jean Aldread on the 23rd of September and a maximum of 20 seats`)


Edit Accounts/Update of the Reservations- (Edit Account) (Amend Booking) (Update Table Reservation)
UPDATE Customer SET (?,?,?) WHERE Customer_Email=Customer_Email;   forename, surname and Number
UPDATE Reservation SET (?,?,?,?) WHERE Customer_Email=Customer_Email AND Restaurant_Email=Restaurant_Email; Time, Date, No of people, details
UPDATE Restaruant SET (?) WHERE Restaurant_Email=Restaurant_Email; Booked Seats
UPDATE Restaruant SET (?,?,?,?,?,?,?,?,?) WHERE Restaurant_Email=Restaurant_Email; Contact_Number,MondayToFriday_OT, MondayToFriday_CT,Sat_OT,Sat_CT,Sun_OT,Sun_CT,Food_Type,Total_No_Seats

Sort Restaurants by Area- (Select Area)
SELECT Name,Contact_Number,Rating,MondayToFriday_OT, MondayToFriday_CT, Sat_OT, Sat_CT,Sun_OT,Sun_CT,Food_Type FROM Restaurant 
WHERE Area=?;

Sort Restaurants by Food Type- (Select Food Type)
SELECT Name,Contact_Number,Rating,MondayToFriday_OT, MondayToFriday_CT, Sat_OT,Sat_CT,Sun_OT,Sun_CT FROM Restaurant 
WHERE Food_Type=?;

Sort Restaurants by Food Type and Area-
SELECT Name,Contact_Number,Rating,MondayToFriday_OT, MondayToFriday_CT,Sat_OT,Sat_CT,Sun_OT,Sun_CT FROM Restaurant 
WHERE Food_Type=? AND Area=?;

Show all of the Reservations made by the Customer- (View Reservation)
SELECT Restaurant_Name,Restaurant_Email,Customer_Email,Booked_Time,Booked_Date,No_Guests,Details FROM Reservation
WHERE Customer_Email=?;

Show all of the Reservations held by the Restuarant- (View Reservation)
SELECT Restaurant_Name,Restaurant_Email,Customer_Email,Booked_Time,Booked_Date,No_Guests,Details FROM Reservation
WHERE Restaurant_Email=?;

Restuarant Login-
SELECT Restaurant_Email, Restaurant_Password FROM Restaurant
WHERE Restaurant_Email=? AND Restaurant_Password=?;

Customer Login-
SELECT Customer_Email, Customer_Password FROM Customer
WHERE Customer_Email=? AND Customer_Password=?;

Rate Restaurant-
INSERT INTO Restaurant VALUES (?); Rating 

UPDATE Restaruant SET (?) WHERE Restaurant_Email=Restaurant_Email; Updating the rating
SELECT Name,Contact_Number,Rating,MondayToFriday_OT, MondayToFriday_CT, Sat_OT, Sat_CT,Sun_OT,Sun_CT,Food_Type FROM Restaurant 
WHERE Rating=5; sorting the restaurants by certain ratings

*/
