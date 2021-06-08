/* Updates made to the MovieStream db from the beginning, however trivial. */

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

UPDATE NETFLIX
SET Release_year=2021
WHERE Title='Slay';

UPDATE NETFLIX
SET Title='Tyler Perry''s Madea''s Big Happy Family'
WHERE Title LIKE '%Big Happy Family';

UPDATE MOVIE_SCORE_DATA
SET Title='Tyler Perry''s Madea''s Big Happy Family'
WHERE Title LIKE '%Big Happy Family';

UPDATE MOVIE_SCORE_DATA
SET Title='The Fisherman''s Diary'
WHERE Title LIKE '%Fisherman%';

UPDATE NETFLIX
SET Title='The Fisherman''s Diary'
WHERE Title LIKE '%Fisherman%';

UPDATE MOVIE_SCORE_DATA
SET Title='Dad Stop Embarrassing Me – The Afterparty'
WHERE Title='Dad Stop Embarrassing Me - The Afterparty';

UPDATE NETFLIX
SET Title='Perfume Imaginary Museum Time Wrap'
WHERE Title LIKE 'Perfume Imaginary Museum “Time Wrap”';

UPDATE NETFLIX
SET Release_year=2020
WHERE Title='Perfume Imaginary Museum Time Wrap';

UPDATE NETFLIX
SET Release_year=2019
WHERE Title='Rudra: The Rise of King Pharaoh';

UPDATE NETFLIX
SET Title='Shadow and Bone - The Afterparty'
WHERE Title='Shadow and Bone – The Netflix Afterparty';

UPDATE NETFLIX
SET Release_year=2019
WHERE Title='Shiva: Journey to Plunotaria';

UPDATE MOVIE_SCORE_DATA
SET Title='Story of Kale: When Someone''s in Love'
WHERE Title LIKE '%Story of Kale%';

UPDATE NETFLIX
SET Title='Story of Kale: When Someone''s in Love'
WHERE Title LIKE '%Story of Kale%';

UPDATE MOVIE_SCORE_DATA
SET Title_category = ltrim(Title_category);

UPDATE MOVIE_SCORE_DATA
SET Runtime = ltrim(Runtime);

