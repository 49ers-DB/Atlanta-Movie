-- Explore Theater

DROP PROCEDURE IF EXISTS user_filter_th;
DELIMITER $$
CREATE PROCEDURE `user_filter_th`(IN i_thName VARCHAR(50), IN i_comName VARCHAR(50), IN i_city VARCHAR(50), IN i_state VARCHAR(3))
BEGIN
    DROP TABLE IF EXISTS UserFilterTh;
    CREATE TABLE UserFilterTh
    SELECT thName, thStreet, thCity, thState, thZipcode, comName
    FROM Theater
    WHERE (thName = i_thName OR i_thName = "ALL") AND
        (comName = i_comName OR i_comName = "ALL") AND
        (thCity = i_city OR i_city = "ALL") AND
        (thState = i_state OR i_state = "ALL") AND;
    END$$
    DELIMITER ;

DROP PROCEDURE IF EXISTS user_visit_th;
DELIMITER $$
CREATE PROCEDURE `user_visit_th`(IN i_thName VARCHAR(50), IN i_comName VARCHAR(50),IN i_visitDate DATE, IN i_username VARCHAR(50))
BEGIN
    INSERT INTO UserVisitTheater (thName, comName, visitDate, username)
        VALUES (i_thName, i_comName, i_visitDate, i_username);
END$$
DELIMITER ;

-- Explore Movie

select MoviePlay.movName as 'Movie', MoviePlay.thName as 'Theater', Theater.thStreet as 'Street', Theater.thCity as 'City', Theater.thState as 'State', Theater.thZipcode as 'Zip Code', MoviePlay.comName as 'Company', MoviePlay.movPlayDate as 'Play Date' from MoviePlay inner join Theater on Theater.thName,Theater.comName = MoviePlay.thName,MoviePLay.comName;

DROP PROCEDURE IF EXISTS customer_filter_mov;
DELIMITER $$
CREATE PROCEDURE `customer_filter_mov`(IN i_movName VARCHAR(50), IN i_comName VARCHAR(50), IN i_city VARCHAR(50), IN i_state VARCHAR(3), IN i_movPlayDate DATE)
BEGIN
    DROP TABLE IF EXISTS CustomerFilterMov;
    CREATE TABLE CustomerFilterMov
    SELECT MoviePlay.movName, MoviePlay.comName, Theater.thCity, Theater.thState, MoviePlay.movPlayDate
    FROM MoviePlay INNER JOIN Theater ON Theater.thName, Theater.comName = MoviePlay.thName, MoviePLay.comName
    WHERE (movName = i_movName OR i_movName = "ALL") AND
        (comName = i_comName OR i_comName = "ALL") AND
        (thCity = i_city OR i_city = "ALL") AND
        (thState = i_state OR i_state = "ALL") AND
        (movPlayDate = i_movPlayDate OR i_movPlayDate = "ALL");
END$$
DELIMITER ;

DROP PROCEDURE IF EXISTS customer_view_mov;
DELIMITER $$
CREATE PROCEDURE `customer_view_mov`(IN i_movName VARCHAR(50), IN i_thName VARCHAR(50), IN i_comName VARCHAR(50), IN i_creditCardNum CHAR(16), IN i_viewDate DATE)
    INSERT INTO CustomerViewMovie (creditCardNum, thName, comName, movName, movReleaseDate, movPlayDate)
        VALUES (i_creditCardNum, i_thName, i_comName, i_movName, i_movReleaseDate, i_movPlayDate);
END$$
DELIMITER ;

-- Create Theater

insert into Theater (thName, comName, capacity, thStreet, thCity, thState, thZipcode, manUsername)
values (i_thName, i_comName, i_capacity, i_thStreet, i_thCity, i_thState, i_thZipcode, i_manUsername);

-- Create Movie

insert into Movie (movName, movReleaseDate, duration)
values (i_movName, i_movReleaseDate, i_duration);

-- Schedule Movie

select movName as 'Name', movReleaseDate as 'Release Date' from Movie;
insert into MoviePlay (thName, comName, movName, movReleaseDate, movPlayDate)
    values (i_thName, i_comName, i_movName, i_movReleaseDate, i_movPlayDate)
    where Manager.comName = i_comName and Manager. --im confused

-- Company Detail

select
