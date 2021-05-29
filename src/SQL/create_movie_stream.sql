CREATE DATABASE MovieStream;
USE MovieStream;

CREATE TABLE MOVIE (
    Rotten_Tomatoes_ID CHAR(9) NOT NULL,
    Title VARCHAR(255),
    Tomato_score INT,
    Release_date VARCHAR(10),
    Runtime VARCHAR(20),
    URL VARCHAR(255),
    PRIMARY KEY (Rotten_Tomatoes_ID)
);

CREATE TABLE ACTOR (
    Rotten_Tomatoes_ID CHAR(9) NOT NULL,
    Actor VARCHAR(255) NOT NULL,
    PRIMARY KEY (Rotten_Tomatoes_ID , Actor),
    FOREIGN KEY (Rotten_Tomatoes_ID)
        REFERENCES MOVIE (Rotten_Tomatoes_ID)
);

CREATE TABLE NETFLIX (
	Title VARCHAR(255) NOT NULL,
    Date_arriving DATE NOT NULL,
    Title_type VARCHAR(10),
    Release_year INT,
    Season VARCHAR(255),
    Weekly VARCHAR(3),
    PRIMARY KEY (Title, Date_arriving)
);

CREATE TABLE MOVIE_SCORE_DATA (
	Title VARCHAR(255) NOT NULL,
    Title_year CHAR(4) NOT NULL,
	Movie_score VARCHAR(3),
    Title_category VARCHAR(255),
    Runtime VARCHAR(10),
    URL VARCHAR(255),
    PRIMARY KEY (Title, Title_year)
);