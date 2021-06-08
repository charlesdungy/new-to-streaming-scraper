# Query DB ---------------------------------------------------------------------
execute_query <- function(db, sql_stmt) {
  query <- dbGetQuery(
    conn = db, 
    statement = sql_stmt
  )
  return(query)
}