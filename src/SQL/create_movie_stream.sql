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
    Critic_score VARCHAR(3) NOT NULL,
    Audience_score VARCHAR(3) NOT NULL,
    Title_category VARCHAR(255),
    Rating VARCHAR(10),
    Runtime VARCHAR(10),
    URL VARCHAR(255),
    Poster_URL VARCHAR(255),
    PRIMARY KEY (Title, Title_year, Critic_score, Audience_score)
);

CREATE TABLE MOVIE_POSTER_DATA (
    Poster_URL VARCHAR(255) NOT NULL,
    Poster_file_path VARCHAR(255) NOT NULL,
    PRIMARY KEY (Poster_URL, Poster_file_path)
);
