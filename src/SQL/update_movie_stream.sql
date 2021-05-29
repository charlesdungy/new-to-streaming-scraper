USE MovieStream;

DELETE FROM NETFLIX
WHERE Title='Multiple Seven Souls in the Skull Castle movies including';

UPDATE NETFLIX
SET Title='What Lies Below'
WHERE Title LIKE '%What Lies Below%';

UPDATE NETFLIX
SET Title='The Time Traveler''s Wife'
WHERE Title LIKE '%Time Traveler%';

UPDATE MOVIE_SCORE_DATA
SET Title='The Time Traveler''s Wife'
WHERE Title LIKE '%Time Traveler%';

UPDATE NETFLIX
SET Title='The Zookeeper''s Wife'
WHERE Title LIKE '%Zookeeper%';

UPDATE MOVIE_SCORE_DATA
SET Title='The Zookeeper''s Wife'
WHERE Title LIKE '%Zookeeper%';

UPDATE NETFLIX
SET Title='Things Heard & Seen'
WHERE Title='Things Heard and Seen';

UPDATE NETFLIX
SET Title='New Gods: Nezha Reborn'
WHERE Title='New Gods Nezha Reborn';

UPDATE NETFLIX
SET Title='Tersanjung: The Movie'
WHERE Title='Tersanjung the Movie';

UPDATE NETFLIX
SET Release_year=2020
WHERE Title='Concrete Cowboy';

UPDATE NETFLIX
SET Release_year=2020
WHERE Title='Coven of Sisters';

UPDATE NETFLIX
SET Release_year=2020
WHERE Title='Night in Paradise';

UPDATE NETFLIX
SET Release_year=2020
WHERE Title='Tell Me When';

UPDATE NETFLIX
SET Release_year=2020
WHERE Title='Two Distant Strangers';

UPDATE NETFLIX
SET Release_year=2020
WHERE Title='Sky High';

UPDATE NETFLIX
SET Release_year=2012
WHERE Title='Doctor Bello';

UPDATE NETFLIX
SET Release_year=2013
WHERE Title='Escape from Planet Earth';

UPDATE NETFLIX
SET Release_year=2019
WHERE Title='Into the Beat';