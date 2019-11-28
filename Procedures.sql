use moviez;
DROP PROCEDURE IF EXISTS user_login;
DELIMITER $$
CREATE PROCEDURE `user_login`(IN i_username VARCHAR(50), IN i_password VARCHAR(50))
BEGIN
    DROP TABLE IF EXISTS UserLogin;
    CREATE TABLE UserLogin
        SELECT User1.username, User1.status, count(Customer.username) as "isCustomer", count(Manager.username) as "isManager", count(Admin.username) as "isAdmin" FROM
        (SELECT User.username, User.status FROM User
        where User.username = i_username and password = MD5(i_password)) as User1
        left outer join Customer on
        Customer.username = User1.username
        left outer join Manager on
        Manager.username=User1.username
        left outer join Admin on
        Admin.username=User1.username;
    SELECT * from UserLogin;
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS user_register;
DELIMITER $$
CREATE PROCEDURE `user_register`(IN i_username VARCHAR(50), IN i_password VARCHAR(50), IN i_firstname VARCHAR(50), IN i_lastname VARCHAR(50))
BEGIN
    INSERT INTO user (username, password, firstname, lastname) VALUES (i_username, MD5(i_password), i_firstname, i_lastname);
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS customer_only_register;
DELIMITER $$
CREATE PROCEDURE `customer_only_register`(IN i_username VARCHAR(50), IN i_password VARCHAR(50), IN i_firstname VARCHAR(50), IN i_lastname VARCHAR(50))
BEGIN
    INSERT INTO user (username, password, firstname, lastname) VALUES (i_username, MD5(i_password), i_firstname, i_lastname);
    INSERT INTO customer (username) VALUES (i_username);
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS customer_add_creditcard;
DELIMITER $$
CREATE PROCEDURE `customer_add_creditcard`(IN i_username VARCHAR(50), IN i_creditCardNum CHAR(16))
BEGIN
    DECLARE ccCount INT;

    SELECT ccCount = count(i_creditCardNum) FROM CustomerCreditCard WHERE username=i_username;
    IF (ccCount < 6) THEN
        INSERT INTO CustomerCreditCard (username, creditCardNum) VALUES (i_username, i_creditCardNum);
    END IF;

END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS manager_only_register;
DELIMITER $$
CREATE PROCEDURE `manager_only_register`(IN i_username VARCHAR(50), IN i_password VARCHAR(50), IN i_firstname VARCHAR(50), IN i_lastname VARCHAR(50), IN i_comName VARCHAR(50), IN i_empStreet VARCHAR(50), IN i_empCity VARCHAR(50), IN i_empState CHAR(2), IN i_empZipcode CHAR(5))
BEGIN
    INSERT INTO user (username, password, firstname, lastname) VALUES (i_username, MD5(i_password), i_firstname, i_lastname);
    INSERT INTO employee (username) VALUES (i_username);
    INSERT INTO manager (username, manStreet, manCity, manState, manZipcode, comName) VALUES (i_username, i_empStreet, i_empCity, i_empState, i_empZipcode, i_comName);
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS manager_customer_register;
DELIMITER $$
CREATE PROCEDURE `manager_customer_register`(IN i_username VARCHAR(50), IN i_password VARCHAR(50), IN i_firstname VARCHAR(50), IN i_lastname VARCHAR(50), IN i_comName VARCHAR(50), IN i_empStreet VARCHAR(50), IN i_empCity VARCHAR(50), IN i_empState CHAR(2), IN i_empZipcode CHAR(5))
BEGIN
    INSERT INTO user (username, password, firstname, lastname) VALUES (i_username, MD5(i_password), i_firstname, i_lastname);
    INSERT INTO employee (username) VALUES (i_username);
    INSERT INTO manager (username, manStreet, manCity, manState, manZipcode, comName) VALUES (i_username, i_empStreet, i_empCity, i_empState, i_empZipcode, i_comName);
    INSERT INTO customer (username) VALUES (i_username);
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS manager_customer_add_creditcard;
DELIMITER $$
CREATE PROCEDURE `manager_customer_add_creditcard`(IN i_username VARCHAR(50), IN i_creditCardNum CHAR(16))
BEGIN
    DECLARE ccCount INT;

    SELECT ccCount = count(i_creditCardNum) FROM CustomerCreditCard WHERE username=i_username;
    IF (ccCount < 6) THEN
        INSERT INTO CustomerCreditCard (username, creditCardNum) VALUES (i_username, i_creditCardNum);
    END IF;
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS admin_approve_user;
DELIMITER $$
CREATE PROCEDURE `admin_approve_user`(IN i_username VARCHAR(50))
BEGIN

    UPDATE user SET status = 'Approved' where username = i_username;
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS admin_decline_user;
DELIMITER $$
CREATE PROCEDURE `admin_decline_user`(IN i_username VARCHAR(50))
BEGIN
    UPDATE user SET status = 'Declined' where username = i_username
    and status = 'Pending';
END$$
DELIMITER ;

DROP PROCEDURE IF EXISTS admin_filter_user;
DELIMITER $$
CREATE PROCEDURE `admin_filter_user`(IN i_username VARCHAR(50), IN i_status ENUM('ALL','Pending', 'Approved', 'Declined'), IN i_sortBy ENUM('username','creditCardCount','userType','status',''), IN i_sortDirection VARCHAR(4))
BEGIN
    DROP TABLE IF EXISTS AdFilterUser;
    CREATE TABLE AdFilterUser
        select * from
             (select user.username, count(CustomerCreditCard.creditCardNum) as "creditCardCount", user.status
             from user
             inner join CustomerCreditCard on user.username = CustomerCreditCard.username group by User.username
             union
             select user.username, 0 as "creditCardCount", user.status
             from user where user.username not in (select username from  CustomerCreditCard)) as Table1
             natural join
             (select user.username, "CustomerAdmin" as "userType"
             from user
             where user.username in
             (select admin.username
             from admin
             inner join customer
             where admin.username=customer.username)
             union
             select user.username, "Admin" as "userType"
             from user
             where user.username in
             (select admin.username from admin)
             and user.username not in
             (select admin.username
             from admin
             inner join customer
             where admin.username = customer.username)
             union
             select user.username, "CustomerManager" as "userType"
             from user
             where user.username in
             (select manager.username
             from manager
             inner join customer
             where manager.username=customer.username)
             union
             select user.username, "Customer" as "userType"
             from user
             where user.username in
             (select customer.username from customer)
             and user.username not in
             (select manager.username
             from manager
             inner join customer
             where manager.username = customer.username)
             and user.username not in (select admin.username
             from admin
             inner join customer
             where admin.username = customer.username)
             union
             select user.username, "Manager" as "userType"
             from user
             where user.username in
             (select manager.username from manager)
             and user.username not in
             (select manager.username
             from manager
             inner join customer
             where manager.username = customer.username)
             union
             select user.username, "User" as "userType"
             from user
             where user.username in
             (select user.username from user)
             and user.username not in
             (select manager.username
             from manager
             inner join customer
             where manager.username = customer.username)
             and user.username not in (select customer.username from customer)
             and user.username not in (select admin.username from admin)
             and user.username not in (select manager.username from manager)) as Table2
             where (Table1.status = i_status or i_status = "ALL") AND
             (Table1.username = i_username or i_username is NULL or i_username = "")
             ORDER BY
                  CASE WHEN i_sortDirection = 'desc' or i_sortDirection = "" THEN 1
                  ELSE
                       CASE WHEN i_sortBy = "" THEN Table1.username
                            WHEN i_sortBy = 'username' THEN Table1.username
                            WHEN i_sortBy = 'creditCardCount' THEN Table1.creditCardCount
                            WHEN i_sortBy = 'userType' THEN Table2.userType
                            WHEN i_sortBy = 'status' THEN Table1.status
                       END
                  END ASC,
                  CASE WHEN i_sortDirection = 'asc' THEN 1
                  ELSE
                       CASE WHEN i_sortBy = "" THEN Table1.username
                            WHEN i_sortBy = 'username' THEN Table1.username
                            WHEN i_sortBy = 'creditCardCount' THEN Table1.creditCardCount
                            WHEN i_sortBy = 'userType' THEN Table2.userType
                            WHEN i_sortBy = 'status' THEN Table1.status
                       END
                  END DESC;
    SELECT * FROM AdFilterUser;
END$$
DELIMITER ;

DROP PROCEDURE IF EXISTS admin_filter_company;
DELIMITER $$
CREATE PROCEDURE `admin_filter_company`(IN i_comName VARCHAR(50), IN i_minCity INT, IN i_maxCity INT, IN i_minTheater INT, IN i_maxTheater INT, in i_minEmployee INT, IN i_maxEmployee INT, IN i_sortBy VARCHAR(50), IN i_sortDirection VARCHAR(10))
BEGIN
    DROP TABLE IF EXISTS AdFilterCom;
    CREATE TABLE AdFilterCom
    select manager.comName as "comName", count(distinct theater.thCity) as "numCityCover",
            count(distinct theater.thName) as "numTheater", count(distinct Manager.username) as "numEmployee"
            from theater join Manager on theater.comName = Manager.comName group by theater.comName
            having
            (i_comName = "ALL" or i_comName = "" or manager.comName = i_comName)
            and (count(distinct theater.thCity) >= i_minCity or i_minCity is NULL)
            and (count(distinct theater.thCity) <= i_maxCity or i_maxCity is NULL)
            and (count(distinct theater.thName) >= i_minTheater or i_minTheater is NULL)
            and (count(distinct theater.thName) <= i_maxTheater or i_maxTheater is NULL)
            and (count(distinct Manager.username) >= i_minEmployee or i_minEmployee is NULL)
            and (count(distinct Manager.username) <= i_maxEmployee or i_maxEmployee is NULL)
            ORDER BY
                  CASE WHEN i_sortDirection = 'DESC' or i_sortDirection = '' THEN 1
                  ELSE
                       CASE WHEN i_sortBy = '' THEN manager.comName
                            WHEN i_sortBy = 'comName' THEN manager.comName
                            WHEN i_sortBy = 'numCityCover' THEN count(distinct theater.thCity)
                            WHEN i_sortBy = 'numTheater' THEN count(distinct theater.thName)
                            WHEN i_sortBy = 'numEmployee' THEN count(distinct Manager.username)
                       END
                  END ASC,
                  CASE WHEN i_sortDirection = 'ASC' THEN 1
                  ELSE
                       CASE WHEN i_sortBy = '' THEN manager.comName
                            WHEN i_sortBy = 'comName' THEN manager.comName
                            WHEN i_sortBy = 'numCityCover' THEN count(distinct theater.thCity)
                            WHEN i_sortBy = 'numTheater' THEN count(distinct theater.thName)
                            WHEN i_sortBy = 'numEmployee' THEN count(distinct Manager.username)
                       END
                  END DESC;
    SELECT * FROM AdFilterCom;
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS admin_create_theater;
DELIMITER $$
CREATE PROCEDURE `admin_create_theater`(IN i_thName VARCHAR(50), IN i_comName VARCHAR(50), IN i_thStreet VARCHAR(50), IN i_thCity VARCHAR(50), IN i_thState CHAR(2), IN i_thZipcode CHAR(5), IN i_capacity INT, IN i_managerUsername VARCHAR(50))
BEGIN
    DECLARE manComName VARCHAR(50);

    SELECT Manager.comName INTO manComName FROM Manager WHERE username=i_managerUsername;
	Select i_managerUsername;
	SELECT manComName;
	select manComName like i_comName;
    IF (manComName like i_comName) THEN
        INSERT INTO Theater (thName, comName, thStreet, thCity, thState, thZipcode, capacity, manUsername)
        VALUES (i_thName, i_comName, i_thStreet, i_thCity, i_thState, i_thZipcode, i_capacity, i_managerUsername);
    END IF;

END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS admin_view_comDetail_emp;
DELIMITER $$
CREATE PROCEDURE `admin_view_comDetail_emp`(IN i_comName VARCHAR(50))
BEGIN
    DROP TABLE IF EXISTS AdComDetailEmp;
    CREATE TABLE AdComDetailEmp
    select user.firstname as "empFirstname", user.lastname as "empLastname"
            from user
            join manager on user.username=manager.username
            and manager.comName in
            (select company.comName from company where company.comName = i_comName);
    SELECT * From AdComDetailEmp;
END$$
DELIMITER ;

DROP PROCEDURE IF EXISTS admin_view_comDetail_th;
DELIMITER $$
CREATE PROCEDURE `admin_view_comDetail_th`(IN i_comName VARCHAR(50))
BEGIN
    DROP TABLE IF EXISTS AdComDetailTh;
    CREATE TABLE AdComDetailTh
    select theater.thName, theater.manUsername as "thManagerUsername", theater.thCity, theater.thState, theater.capacity  as "thCapacity"
            from theater where theater.comName=i_comName;
    SELECT * from AdComDetailTh;
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS admin_create_mov;
DELIMITER $$
CREATE PROCEDURE `admin_create_mov`(IN i_movName VARCHAR(50), IN i_movDuration INT, IN i_movReleaseDate DATE)
BEGIN
    INSERT INTO Movie (movName, movReleaseDate, duration)
    VALUES ( i_movName, i_movReleaseDate, i_movDuration);
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS manager_filter_th;
DELIMITER $$
CREATE PROCEDURE `manager_filter_th`(IN i_manUsername VARCHAR(50), IN i_movName VARCHAR(50), IN i_minMovDuration INT, IN i_maxMovDuration INT, IN i_minMovReleaseDate DATE, IN i_maxMovReleaseDate DATE, IN i_minMovPlayDate DATE, IN i_maxMovPlayDate DATE, IN i_includeNotPlayed BOOLEAN)
BEGIN
    DROP TABLE IF EXISTS ManFilterTh;
    CREATE TABLE ManFilterTh
    select distinct MoviePlay.movName as "movName", MoviePlay.movReleaseDate as "movReleaseDate",
    MoviePlay.movPlayDate as "movPlayDate", Movie.duration as "movDuration"
            from MoviePlay join Movie on MoviePlay.movName = Movie.movName where MoviePlay.thName in
            (select thName from Theater where Theater.manUsername = i_manUsername)
            and (i_minMovReleaseDate is NULL or Movie.movReleaseDate >= i_minMovReleaseDate)
            and (i_maxMovReleaseDate is NULL or Movie.movReleaseDate <= i_maxMovReleaseDate)
            and (i_maxMovPlayDate is NULL or MoviePlay.movPlayDate <= i_maxMovPlayDate)
            and (i_minMovPlayDate is NULL or MoviePlay.movPlayDate >= i_minMovPlayDate)
            and (i_maxMovDuration is NULL or Movie.duration <= i_maxMovDuration)
            and (i_minMovDuration is NULL or Movie.duration >= i_minMovDuration)
            and (i_movName ="" or Movie.movName like i_movName)
            and (i_includeNotPlayed is NULL or i_includeNotPlayed=False or MoviePlay.movPlayDate != NULL)
            Union
            select Movie.movName as "movName", Movie.movReleaseDate as "movReleaseDate",
            cast(NULL as date) as "movPlayDate", Movie.duration as "movDuration" from Movie
            where Movie.movName not in
            (select MoviePlay.movName from MoviePlay where MoviePlay.thName in
                (select thName from Theater where Theater.manUsername = @i_manUsername))
            and (i_minMovReleaseDate is NULL or Movie.movReleaseDate >= i_minMovReleaseDate)
            and (i_maxMovReleaseDate is NULL or Movie.movReleaseDate <= i_maxMovReleaseDate)
            and (i_minMovDuration is NULL or Movie.duration >= i_minMovDuration)
            and (i_maxMovDuration is NULL or Movie.duration <= i_maxMovDuration)
            and (i_movName ="" or Movie.movName like i_movName);
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS manager_schedule_mov;
DELIMITER $$
CREATE PROCEDURE `manager_schedule_mov`(IN i_manUsername VARCHAR(50), IN i_movName VARCHAR(50), IN i_movReleaseDate DATE, IN i_movPlayDate DATE)
BEGIN
    DROP TABLE IF EXISTS tempMoviePlay;
    CREATE Table tempMoviePlay
        SELECT movName, movReleaseDate, thName, comName, i_movPlayDate as movPlayDate FROM Theater
        join Movie
        where Movie.movName=i_movName
        and Movie.movReleaseDate=i_movReleaseDate
        and Theater.manUsername = i_manUsername;
    Select * FROM tempMoviePlay;
    IF (i_movPlayDate >= i_movReleaseDate) THEN
        INSERT INTO MoviePlay Select * FROM tempMoviePlay;
    END IF;

END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS customer_filter_mov;
DELIMITER $$
CREATE PROCEDURE `customer_filter_mov`(IN i_movName VARCHAR(50), IN i_comName VARCHAR(50), IN i_city VARCHAR(50), IN i_state VARCHAR(3), IN i_minMovPlayDate DATE, IN i_maxMovPlayDate DATE)
BEGIN
    DROP TABLE IF EXISTS CosFilterMovie;
    CREATE TABLE CosFilterMovie
    SELECT MoviePlay.movName, MoviePlay.comName,Theater.thName, Theater.thStreet, Theater.thCity, Theater.thState, Theater.thZipcode, MoviePlay.movPlayDate, MoviePlay.movReleaseDate
            FROM MoviePlay INNER JOIN Theater ON Theater.thName = MoviePlay.thName AND Theater.comName = MoviePlay.comName
            where MoviePlay.movReleaseDate<=MoviePlay.movPlayDate AND
			(MoviePlay.movName = i_movName OR i_movName = "ALL" or i_movName = "") AND
            (MoviePlay.comName = i_comName OR i_comName = "ALL" or i_comName = "") AND
            (Theater.thCity = i_city OR i_city = "") AND
            (Theater.thState = i_state OR i_state = "ALL" OR i_state = "") AND
            (MoviePlay.movPlayDate >= i_minMovPlayDate OR i_minMovPlayDate is NULL) AND
            (MoviePlay.movPlayDate <= i_maxMovPlayDate OR i_maxMovPlayDate is NULL);
    SELECT * From CosFilterMovie;
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS customer_view_mov;
DELIMITER $$
CREATE PROCEDURE `customer_view_mov`(IN i_creditCardNum CHAR(16), IN i_movName VARCHAR(50), IN i_movReleaseDate DATE, IN i_thName VARCHAR(50), IN i_comName VARCHAR(50), IN i_movPlayDate DATE)
BEGIN
    DROP TABLE IF EXISTS tempCustomerViewMovie;
    CREATE TABLE tempCustomerViewMovie
       SELECT CustomerCreditCard.creditcardNum, MoviePlay.movReleaseDate, MoviePlay.movName, MoviePlay.movPlayDate,  MoviePlay.thName, MoviePlay.comName
        FROM MoviePlay
        JOIN CustomerCreditCard
        WHERE CustomerCreditCard.creditcardNum = i_creditCardNum
        AND MoviePlay.movName = i_movName
        AND MoviePlay.movReleaseDate = i_movReleaseDate
        AND MoviePlay.thName = i_thName
        AND MoviePlay.comName = i_comName
        AND MoviePlay.movPlayDate = i_movPlayDate;
    SELECT * FROM tempCustomerViewMovie;
    INSERT INTO CustomerViewMovie SELECT * FROM tempCustomerViewMovie;
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS customer_view_history;
DELIMITER $$
CREATE PROCEDURE `customer_view_history`(IN i_cusUsername VARCHAR(50))
BEGIN
    DROP TABLE IF EXISTS CosViewHistory;
    CREATE TABLE CosViewHistory
    SELECT movName, thName, comName, creditCardNum, movPlayDate
    FROM CustomerViewMovie
    WHERE CustomerViewMovie.creditCardNum IN (SELECT creditCardNum FROM CustomerCreditCard WHERE CustomerCreditCard.username = i_cusUsername);
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS user_filter_th;
DELIMITER $$
CREATE PROCEDURE `user_filter_th`(IN i_thName VARCHAR(50), IN i_comName VARCHAR(50), IN i_city VARCHAR(50), IN i_state VARCHAR(3))
BEGIN
    DROP TABLE IF EXISTS UserFilterTh;
    CREATE TABLE UserFilterTh
    SELECT thName, thStreet, thCity, thState, thZipcode, comName
    FROM Theater
    WHERE
        (thName = i_thName OR i_thName = "ALL" OR i_thName = "") AND
        (comName = i_comName OR i_comName = "ALL" OR i_comName = "") AND
        (thCity = i_city OR i_city = "") AND
        (thState = i_state OR i_state = "" OR i_state = "ALL");
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS user_visit_th;
DELIMITER $$
CREATE PROCEDURE `user_visit_th`(IN i_thName VARCHAR(50), IN i_comName VARCHAR(50), IN i_visitDate DATE, IN i_username VARCHAR(50))
BEGIN
    INSERT INTO UserVisitTheater (thName, comName, visitDate, username)
    VALUES (i_thName, i_comName, i_visitDate, i_username);
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS user_filter_visitHistory;
DELIMITER $$
CREATE PROCEDURE `user_filter_visitHistory`(IN i_username VARCHAR(50), IN i_minVisitDate DATE, IN i_maxVisitDate DATE)
BEGIN
    DROP TABLE IF EXISTS UserVisitHistory;
    CREATE TABLE UserVisitHistory
    SELECT thName, thStreet, thCity, thState, thZipcode, comName, visitDate
    FROM UserVisitTheater
        NATURAL JOIN
        Theater
    WHERE
        (username = i_username) AND
        (i_minVisitDate IS NULL OR visitDate >= i_minVisitDate) AND
        (i_maxVisitDate IS NULL OR visitDate <= i_maxVisitDate);
END$$
DELIMITER ;
