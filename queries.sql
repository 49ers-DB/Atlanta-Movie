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

-- Schedule Movie: I literally don't know how to do this

select movName, movReleaseDate from Movie

insert into MoviePlay (thName, comName, movName, movReleaseDate, movPlayDate)
    values (i_thName, i_comName, i_movName, i_movReleaseDate, i_movPlayDate)

-- Company Detail

    -- Admin view company detail (Employee)
select firstname, lastname from user inner join manager on user.username = manager.username where i_comName = manager.comName

    -- Admin view company detail (Theater)
select thName, manUsername, thCity, thState, capacity from theater where i_comName = theater.comName

-- Manager Filter Theater (Manager Theater Overview) : Literally don't think this is right but I tried

DROP PROCEDURE IF EXISTS manager_filter_th;
DELIMITER $$
CREATE PROCEDURE `manager_filter_th`(IN i_manUsername VARCHAR(50), IN i_movName VARCHAR(50), IN i_minMovDuration INT, IN i_maxMovDuration INT, IN i_minMovReleaseDate DATE, IN i_maxMovReleaseDate DATE, IN i_minMovPlayDate DATE, IN i_maxMovPlayDate DATE, IN i_includeNotPlayed BOOLEAN)
BEGIN
    DROP TABLE IF EXISTS ManagerFilterTh;
    CREATE TABLE ManagerFilterTh
    SELECT movie.movName, movie.duration, movie.movReleaseDate, MoviePlay.movPlayDate
    FROM Movie inner join MoviePlay on movie.MovName = MoviePlay.MovName AND movie.movReleaseDate = MoviePlay.movReleaseDate
    WHERE (movie.movName = i_movName) AND -- trying to figure out how to use $$ to make it to where someone can put in part of a movie name and get results of maybe a keyword or something??
        (movie.duration >= i_minMovDuration OR movie.duration <= i_maxMovDuration OR i_minMovDuration = "ALL" OR i_maxMovDuration = "ALL") AND
        (movie.movReleaseDate >= i_minMovReleaseDate OR movie.movReleaseDate <= i_maxMovReleaseDate OR i_minMovReleaseDate = "ALL" OR i_maxMovDuration = "ALL") AND
        (MoviePlay.movPlayDate >= i_minMovPlayDate OR MoviePlay.movPlayDate <= i_maxMovPlayDate OR i_minMovPlayDate = "ALL" OR i_maxMovPlayDate = "ALL") AND
        (MoviePlay.movPlayDate >= i_includeNotPlayed);
    END$$
    DELIMITER ;




