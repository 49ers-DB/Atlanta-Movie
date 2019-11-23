drop database if exists moviez;
create database moviez;
use moviez;

CREATE TABLE User (
username    VARCHAR(75)    NOT NULL,
password    VARCHAR(75)    NOT NULL,
firstname VARCHAR(75)    NOT NULL,
lastname VARCHAR(75)    NOT NULL,
status  ENUM('Pending', 'Approved', 'Declined') NOT NULL,
PRIMARY KEY(username),
CHECK(LENGTH(password) >= 8)
);

CREATE TABLE Employee (
username VARCHAR(75) NOT NULL,
FOREIGN KEY(username) REFERENCES user(username)
);

CREATE TABLE Customer (
username VARCHAR(75) NOT NULL,
FOREIGN KEY(username) REFERENCES user(username)
ON DELETE CASCADE   ON UPDATE CASCADE
);

CREATE TABLE Admin (
username    VARCHAR(75)        NOT NULL,
PRIMARY KEY(username),
FOREIGN KEY(username) REFERENCES Employee(username)
ON DELETE RESTRICT  ON UPDATE CASCADE
);

CREATE TABLE Company (
comName        VARCHAR(75)    NOT NULL,
PRIMARY KEY(comName)
);

CREATE TABLE Manager (
username    VARCHAR(75)        NOT NULL,
manStreet  VARCHAR(75)        NOT NULL,
manCity        VARCHAR(75)    NOT NULL,
manState       CHAR(2)         NOT NULL,
manZipcode     CHAR(5)         NOT NULL,
comName    VARCHAR(75)        NOT NULL,
PRIMARY KEY(username),
FOREIGN KEY(username) REFERENCES Employee(username)
ON DELETE   CASCADE     ON UPDATE   CASCADE,
FOREIGN KEY(comName) REFERENCES Company(comName)
ON DELETE CASCADE   ON UPDATE CASCADE,
UNIQUE (manStreet, manCity, manState, manZipcode)
);

CREATE TABLE Theater (
thName        VARCHAR(75)    NOT NULL,
comName    VARCHAR(75)    NOT NULL,
manUsername  VARCHAR(75)    NOT NULL,
thStreet  VARCHAR(75)    NOT NULL,
thCity        VARCHAR(75)    NOT NULL,
thState   CHAR(2)         NOT NULL,
thZipcode         CHAR(5)         NOT NULL,
capacity    INT             NOT NULL,
PRIMARY KEY(thName, comName),
FOREIGN KEY(comName) REFERENCES Company(comName)
ON DELETE   CASCADE ON UPDATE   CASCADE,
FOREIGN KEY(manUsername) REFERENCES Manager(username)
ON DELETE RESTRICT  ON UPDATE CASCADE
);


CREATE TABLE CustomerCreditCard (
creditCardNum   CHAR(16)        NOT NULL,
username        VARCHAR(75)    NOT NULL,
PRIMARY KEY(creditCardNum),
FOREIGN KEY(username) REFERENCES customer(username)
ON DELETE   CASCADE ON UPDATE   CASCADE
);

CREATE TABLE Movie (
movName            VARCHAR(75)    NOT NULL,
movReleaseDate    DATE            NOT NULL,
duration        INT         NOT NULL,
PRIMARY KEY(movName , movReleaseDate)
);

CREATE TABLE MoviePlay (
movName  VARCHAR(75)    NOT NULL,
movReleaseDate    DATE            NOT NULL,
thName    VARCHAR(75)    NOT NULL,
comName        VARCHAR(75)    NOT NULL,
movPlayDate     DATE       NOT NULL,
PRIMARY KEY(movName, movReleaseDate, thName, comName, movPlayDate),
FOREIGN KEY(movName,movReleaseDate) REFERENCES Movie(movName,movReleaseDate)
ON DELETE   CASCADE     ON UPDATE CASCADE,
FOREIGN KEY(thName, comName) REFERENCES Theater(thName, comName)
ON DELETE   CASCADE     ON UPDATE CASCADE
);

CREATE TABLE UserVisitTheater (
visitID         VARCHAR(75)    NOT NULL,
username        VARCHAR(75)    NOT NULL,
thName    VARCHAR(75)    NOT NULL,
comName        VARCHAR(75)    NOT NULL,
visitDate            DATE            NOT NULL,
PRIMARY KEY(visitID),
FOREIGN KEY(username) REFERENCES User(username)
ON DELETE CASCADE   ON UPDATE CASCADE,
FOREIGN KEY(thName) REFERENCES Theater(thName)
ON DELETE CASCADE   ON UPDATE CASCADE,
FOREIGN KEY(comName) REFERENCES Company(comName)
ON DELETE CASCADE   ON UPDATE CASCADE
);

CREATE TABLE CustomerViewMovie (
creditCardNum   CHAR(16)        NOT NULL,
movReleaseDate       DATE            NOT NULL,
movName      VARCHAR(75)    NOT NULL,
movPlayDate    DATE            NOT NULL,
thName    VARCHAR(75)    NOT NULL,
comName        VARCHAR(75)    NOT NULL,
PRIMARY KEY(creditCardNum, movPlayDate, movName, movReleaseDate, thName, comName),
FOREIGN KEY(creditCardNum)  REFERENCES CustomerCreditCard(creditCardNum)
ON DELETE CASCADE   ON UPDATE RESTRICT,
FOREIGN KEY(movName, movReleaseDate, thName, comName, movPlayDate) REFERENCES MoviePlay(movName, movReleaseDate, thName, comName, movPlayDate)
ON DELETE CASCADE   ON UPDATE CASCADE
);






use moviez;

Insert into User (username,status,firstname,lastname,password)
Values 
("georgep","Approved","George P.","Burdell",MD5('111111111')),
('calcwizard','Approved','Issac','Newton',MD5('222222222')),
('calcultron','Approved','Dwight','Schrute',MD5('333333333')),
('calcultron2','Approved','Jim','Halpert',MD5('444444444')),
('gdanger','Declined','Gary','Danger',MD5('555555555')),
('imbatman','Approved','Bruce','Wayne',MD5('666666666')),
('imready','Approved','Spongebob','Squarepants',MD5('777777777')),
('isthisthekrustykrab','Approved','Patrick','Star',MD5('888888888')),
('clarinetbeast','Declined','Squidward','Tentacles',MD5('999999999')),
('texasStarKarate','Declined','Sandy','Cheeks',MD5('111111110')),
('fullMetal','Approved','Edward','Elric',MD5('111111100')),
('notFullMetal','Approved','Alphonse','Elric',MD5('111111100')),
('ilikemoney$$','Approved','Eugene','Krabs',MD5('111111110')),
('eeqmcsquare','Approved','Albert','Einstein',MD5('111111110')),
('theScienceGuy','Approved','Bill','Nye',MD5('999999999')),
('entropyRox','Approved','Claude','Shannon',MD5('999999999')),
('fatherAI','Approved','Alan','Turing',MD5('222222222')),
('cool_class4400','Approved','A. TA','Washere',MD5('333333333')),
("thePiGuy3.14",'Approved','Archimedes','Syracuse',MD5('1111111111')),
('does2Much','Approved','Carl','Gauss',MD5('1212121212')),
('programerAAL','Approved','Ada','Lovelace',MD5('3131313131')),
('radioactivePoRa','Approved','Marie','Curie',MD5('1313131313')),
('DNAhelix','Approved','Rosalind','Franklin',MD5('777777777'),
('ghcghc','Approved','Grace','Hopper',MD5('666666666')),
('RitzLover28','Approved','Abby','Normal',MD5('444444444')),
('smith_j','Pending','John','Smith',MD5('333333333')),
('manager1','Approved','Manager',"One",MD5('1122112211')),
('manager2','Approved','Manager','Two',MD5('3131313131')),
('manager3','Approved','Three','Three',MD5('8787878787')),
('manager4','Approved','Four','Four',MD5('5755555555'));

insert into moviez.Employee (username)
values ('georgep'),
('calcultron'),
('imbatman'),
('entropyRox'),
('fatherAI'),
('cool_class4400'),
('radioactivePoRa'),
('ghcghc'),
('manager1'),
('manager2'),
('manager3'),
('manager4');

insert into moviez.Customer (username)
values ('georgep'),
('calcwizard'),
('calcultron'),
('calcultron2'),
('imready'),
('isthisthekrustykrab'),
('clarinetbeast'),
('fullMetal'),
('notFullMetal'),
('ilikemoney$$'),
('eeqmcsquare'),
('theScienceGuy'),
('entropyRox'),
('cool_class4400'),
("thePiGuy3.14"),
('does2Much'),
('programerAAL'),
('DNAhelix'),
('RitzLover28');

insert into moviez.Admin (username)
values ('cool_class4400'
);

insert into moviez.Company (comName)
values ("EZ Theater Company"), ("4400 Theater Company"), ("Awesome Theater Company"), ("AI Theater Company");

insert into moviez.Manager (username, manStreet, manCity, manState, manZipcode, comName)
values('entropyRox',"200 Cool Place","San Francisco",'CA',94016,"4400 Theater Company"),
('fatherAI',"456 Main St","New York",'NY',10001,"EZ Theater Company"),
('georgep',"10 Pearl Dr","Seattle",'WA',98105,"4400 Theater Company"),
('calcultron',"123 Peachtree St",'Atlanta','GA',30308,"EZ Theater Company"),
('imbatman',"800 Color Dr",'Austin','TX',78653,"Awesome Theater Company"),
('ghcghc',"100 Pi St","Pallet Town",'KS',31415,"AI Theater Company"),
('radioactivePoRa',"100 Blu St",'Sunnyvale','CA',94088,"4400 Theater Company"),
('manager1',"123 Ferst Drive",'Atlanta','GA',30332,"4400 Theater Company"),
('manager2',"456 Ferst Drive",'Atlanta','GA',30332,"AI Theater Company"),
('manager3',"789 Ferst Drive",'Atlanta','GA',30332,"4400 Theater Company"),
('manager4',"000 Ferst Drive",'Atlanta','GA',30332,"4400 Theater Company"
);

insert into moviez.Theater (comName,thName,capacity,thStreet,thCity,thState,thZipcode,manUsername)
values 
("EZ Theater Company","Main Movies",3,"123 Main St","New York",'NY',10001,'fatherAI'),
("EZ Theater Company",'Star Movies',2,'745 GT St','Atlanta','GA',30332,'calcultron'),
('4400 Theater Company','Cinema Star',4,'100 Cool Place','San Francisco','CA',94016,'entropyRox'),
('4400 Theater Company','Star Movies',5,'4400 Rocks Ave','Boulder','CA',80301,'radioactivePoRa'),
('4400 Theater Company',"Jonathan's Movies",2,'67 Pearl Dr','Seattle','WA',98101,'georgep'),
('Awesome Theater Company','ABC Theater',5,'880 Color Dr','Austin','TX',73301,'imbatman'),
('AI Theater Company','ML Movies',3,'314 Pi St','Pallet Town','KS',31415,'ghcghc');

insert into moviez.CustomerCreditCard (username,creditCardNum)
values 
('georgep',1111111111111111),
('georgep',1111111111111110),
('georgep',1111111111111100),
('georgep',1111111111111000),
('georgep',1111111111110000),
('calcwizard',1111111111100000),
('calcultron',1111111111000000),
('calcultron2',1111111110000000),
('calcultron2',1111111100000000),
('imready',1111110000000000),
('isthisthekrustykrab',1111100000000000),
('isthisthekrustykrab',1111000000000000),
('isthisthekrustykrab',1110000000000000),
('fullMetal',1100000000000000),
('notFullMetal',1000000000000000),
('ilikemoney$$',9000000000000000),
('ilikemoney$$',2222222222222222),
('ilikemoney$$',2222222222222220),
('eeqmcsquare',2222222222222200),
('theScienceGuy',2222222222222000),
('entropyRox',2222222222220000),
('entropyRox',2222222222200000),
('cool_class4400',2222222222000000),
("thePiGuy3.14",2222222220000000),
('does2Much',2222222200000000),
('programerAAL',2222222000000000),
('DNAhelix',2220000000000000),
('RitzLover28',3333333333333300);


insert into moviez.Movie (movName, movReleaseDate, duration)
values ("How to Train Your Dragon",'2010-03-21',98),
("4400 The Movie",'2019-08-12',130),
("The First Pokemon Movie",'1998-07-19',75),
("The King's Speech",'2010-11-26',119),
("Avengers: Endgame",'2019-04-26',181),
('Spaceballs','1987-06-24',96),
("Spider-Man: Into the Spider-Verse",'2018-12-01',117),
("Georgia Tech The Movie",'1985-08-13',100),
("George P Burdell's Life Story",'1927-08-12',100),
("Calculus Returns: A ML Story",'2019-09-19',314);

insert into moviez.MoviePlay (movName, movReleaseDate, movPlayDate, thName, comName)
values ("4400 The Movie",'2019-08-12','2019-10-12',"ABC Theater","Awesome Theater Company"),
("The First Pokemon Movie",'1998-07-19','2018-07-19',"ABC Theater","Awesome Theater Company"),
('Georgia Tech The Movie','1985-08-13','1985-08-13','ABC Theater','Awesome Theater Company'),
('How to Train Your Dragon','2010-03-21','2010-04-02','Cinema Star','4400 Theater Company'),
("4400 The Movie",'2019-08-12','2019-09-12','Cinema Star','4400 Theater Company'),
("The King's Speech",'2010-11-26','2019-12-20','Cinema Star','4400 Theater Company'),
('Spaceballs','1987-06-24','2000-02-02','Cinema Star','4400 Theater Company'),
('Georgia Tech The Movie','1985-08-13','2019-09-30','Cinema Star','4400 Theater Company'),
("George P Burdell's Life Story",'1927-08-12','2010-05-20','Cinema Star','4400 Theater Company'),
('How to Train Your Dragon','2010-03-21','2010-03-22','Main Movies','EZ Theater Company'),
('How to Train Your Dragon','2010-03-21','2010-03-23','Main Movies','EZ Theater Company'),
('Spaceballs','1987-06-24','1999-06-24','Main Movies','EZ Theater Company'),
("George P Burdell's Life Story",'1927-08-12','2019-10-22','Main Movies','EZ Theater Company'),
("George P Burdell's Life Story",'1927-08-12','2019-07-14','Main Movies','EZ Theater Company'),
("The King's Speech",'2010-11-26','2019-12-20','Main Movies','EZ Theater Company'),
('Spaceballs','1987-06-24','2010-04-02','ML Movies','AI Theater Company'),
('Spaceballs','1987-06-24','2023-01-23','ML Movies','AI Theater Company'),
('Calculus Returns: A ML Story','2019-09-19','2019-10-10','ML Movies','AI Theater Company'),
('Calculus Returns: A ML Story','2019-09-19','2019-12-30','ML Movies','AI Theater Company'),
('Spider-Man: Into the Spider-Verse','2018-12-01','2019-09-30','ML Movies','AI Theater Company'),
('How to Train Your Dragon','2010-03-21','2010-03-25','Star Movies','EZ Theater Company'),
("4400 The Movie",'2019-08-12','2019-08-12','Star Movies','EZ Theater Company');

insert into moviez.UserVisitTheater (username, thName, comName, visitDate, VisitID)
values ('georgep','Main Movies','EZ Theater Company','2010-03-22',1),
('calcwizard','Main Movies','EZ Theater Company','2010-03-22',2),
('calcwizard','Star Movies','EZ Theater Company','2010-03-25',3),
('imready','Star Movies','EZ Theater Company','2010-03-25',4),
('calcwizard','ML Movies','AI Theater Company','2010-03-20',5);

insert into moviez.CustomerViewMovie (movName, movReleaseDate, movPlayDate, thName, comName,creditCardNum)
values ('How to Train Your Dragon','2010-03-21','2010-04-02','Cinema Star','4400 Theater Company',1111111111111111),
('How to Train Your Dragon','2010-03-21','2010-03-22','Main Movies','EZ Theater Company',1111111111111111),
('How to Train Your Dragon','2010-03-21','2010-03-23','Main Movies','EZ Theater Company',1111111111111111),
('How to Train Your Dragon','2010-03-21','2010-03-25','Star Movies','EZ Theater Company',1111111111111100);