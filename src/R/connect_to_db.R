library(DBI)
library(RMySQL)

# Establish connection to MovieStream db ---------------------------------------
movie_stream_db <- tryCatch({
  dbConnect(
    drv = dbDriver("MySQL"),
    default.file = "../Python/config/config.cnf", 
    group = "MovieStream",
    user = NULL, 
    password = NULL
  )},
  error = function(c) "error"
)

# Set encoding -----------------------------------------------------------------
dbSendQuery(movie_stream_db, "SET NAMES utf8mb4;")
dbSendQuery(movie_stream_db, "SET CHARACTER SET utf8mb4;")
dbSendQuery(movie_stream_db, "SET character_set_connection=utf8mb4;")