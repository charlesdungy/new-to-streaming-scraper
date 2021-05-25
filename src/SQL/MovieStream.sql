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


    