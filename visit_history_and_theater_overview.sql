-- view history
select movName as "Movie", thName as "Theater", comName as "Company", creditCardNum as "Credit Card", movPlayDate as "View Date" from CustomerViewMovie;

--visit history
select thName, thStreet, thCity, thState, thZipcode, comName, visitDate from UserVisitTheater natural join Theater where (username = i_username) and (i_minVisitDate IS null or visitDate >= i_minVisitDate) and (i_maxVisitDate is null or visitDate <= i_maxVisitDate);

--theater overview
select distinct Movie.movName as "Movie", Movie.duration as "Duration", Movie.movReleaseDate as "Release_Date", MoviePlay.movPlayDate as "Play_Date"
from Movie FULL JOIN MoviePlay on MoviePlay.movName=Movie.movName and MoviePlay.movReleaseDate=Movie.movReleaseDate
where (i_minReleaseDate IS null or Movie.movReleaseDate >= i_minReleaseDate)
and (i_maxReleaseDate is null or Movie.movReleaseDate <= i_maxReleaseDate)
and (i_maxPlayDate is null or MoviePlay.movPlayDate <= i_maxPlayDate)
and (i_minPlayDate IS null or MoviePlay.movPlayDate >= i_minPlayDate)
and (i_maxDuration is null or Movie.Duration <= i_maxDuration)
and (i_minDuration IS null or Movie.Duration >= i_minDuration)
and (i_Movie IS null or Movie.movName = i_Movie);
--how to include the correct theater based on the manager that's logged in?
--how to handle the include not played movie button
