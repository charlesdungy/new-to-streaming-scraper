library(DT)
library(highcharter)
library(htmlwidgets)
library(lubridate)
library(tidyverse)

# Perform connection to MovieStream db -----------------------------------------
source("connect_to_db.R")

# Initialize function to query db ----------------------------------------------
source("query_db.R")

# SQL statement used to query db -----------------------------------------------
sql_stmt <- "SELECT N.Title, 
                    N.Date_Arriving, 
                    N.Release_year, 
                    M.Critic_score,
                    M.Audience_score, 
                    M.Title_Category,
                    M.Rating,
                    M.Runtime,
                    N.Title_type,
                    M.URL,
                    P.Poster_file_path
             FROM   NETFLIX N
                    LEFT JOIN MOVIE_SCORE_DATA M 
                    ON M.Title=N.Title 
                    AND M.Title_year=N.Release_year
                    LEFT JOIN MOVIE_POSTER_DATA P
                    ON P.Poster_URL=M.Poster_URL"

# Resulting dataframe from query execution -------------------------------------
monthly_df <- as.data.frame(
  execute_query(movie_stream_db, sql_stmt)
)

# Movies only, omit critic/audience scores that are NR, parse as number, sort -- 
monthly_df_filtered <- monthly_df %>%
  filter(Title_type == "Movie") %>%
  filter(Critic_score != "NR") %>%
  filter(Audience_score != "NR") %>%
  mutate(Critic_score = parse_number(Critic_score, na = c("", "NR"))) %>%
  mutate(Audience_score = parse_number(Audience_score, na = c("", "NR"))) %>%
  mutate(Date_Arriving = as.Date(Date_Arriving, format = '%Y-%m-%d')) %>%
  mutate(Date_Arriving = format(Date_Arriving, "%m/%d/%Y")) %>%
  arrange(desc(Critic_score))

# Attributes used for plot ----------------------------------------------------
current_month <- as.character(month(today(), label = TRUE, abbr = FALSE))
current_year <- as.character(year(now()))
chart_title <- str_c(current_month, " ", current_year)
chart_subtitle <- "New Titles Streaming to Netflix: Critic Score vs. Audience Score"

# Begin creating plot ----------------------------------------------------------
hchart <- hchart(
  monthly_df_filtered,
  type = "point",
  hcaes(x = Audience_score,
        y = Critic_score,
        group = Rating),
  color = c('#011f4b', 
            '#03396c', 
            '#005b96', 
            '#6497b1', 
            '#b3cde0')
) 

# Edit y-axis, x-axis, tooltip -------------------------------------------------  
hchart <- hchart %>%
  hc_yAxis(
    opposite = FALSE, 
    labels = list(format = "{value}%"),
    min = 0,
    tickInterval = 20,
    max = 100,
    title = "Critic Score") %>% 
  hc_xAxis(
    opposite = FALSE, 
    labels = list(format = "{value}%"),
    tickLength = 0,
    tickInterval = 10,
    title = "Audience Score") %>% 
  hc_tooltip(
    pointFormat = '<b>{point.Title}</b>, 
                   {point.Release_year},
                   {point.Rating}
                   <br> ----- <br> 
                   Critic Score: {point.y: .0f}% <br>
                   Audience Score: {point.x: .0f}% <br>
                   Runtime: {point.Runtime} <br>
                   Genre: {point.Title_Category}'
    )

# Edit title, subtitle, legend, caption, theme ---------------------------------
hchart <- hchart %>% 
  hc_title(
    text = chart_title,
    margin = 20,
    align = "left",
    style = list(useHTML = TRUE)) %>%
  hc_subtitle(
    text = chart_subtitle,
    align = "left",
    style = list(color = "#2b908f", fontWeight = "bold")
  ) %>%
  hc_legend(
    align = "right",
    verticalAlign = "bottom",
    layout = "horizontal"
  ) %>%
  hc_caption(
    align = "right",
    margin = 10,
    text = "Movie titles without either an audience score or critic score have 
    been omitted.<br>Source: Netflix; Rotten Tomatoes; What's on Netflix"
  ) %>%
  hc_add_theme(hc_theme_hcrt())

# Begin DataTable --------------------------------------------------------------

# Variables for image links ----------------------------------------------------
poster_width <-  ' alt="" width="200"'
poster_height <- 'height="300"'
end_html <- ">"
img_src <- '<img src="https://raw.githubusercontent.com/charlesdungy/new-to-streaming-scraper/main/'

#
monthly_df_filtered <- monthly_df_filtered %>%
  mutate(Poster_file_path = str_sub(Poster_file_path, 7)) %>%
  mutate(Poster_img_path = str_c(img_src, '', Poster_file_path, 
                                 '"', poster_width, ' ', 
                                 poster_height, '', end_html))

#
monthly_df_filtered_2 <- monthly_df_filtered %>%
  select('Title', 
         'Date_Arriving', 
         'Release_year', 
         'Critic_score',
         'Audience_score', 
         'Title_Category', 
         'Rating', 
         'Runtime',
         'Poster_img_path')

#
monthly_df_filtered_2 <- monthly_df_filtered_2 %>%
  mutate(Critic_score = str_c(Critic_score, "", "%")) %>%
  mutate(Audience_score = str_c(Audience_score, "", "%")) 

#
monthly_df_filtered_2 <- monthly_df_filtered_2[c('Poster_img_path',
                                                 'Title',
                                                 'Release_year',
                                                 'Critic_score',
                                                 'Audience_score',
                                                 'Rating',
                                                 'Runtime',
                                                 'Title_Category',
                                                 'Date_Arriving')]

#
column_names <- c(
  'Poster',
  'Title',
  'Year',
  'Critic Score',
  'Audience Score',
  'Rating',
  'Runtime',
  'Genre',
  'Date Arriving'
)

#
dt <- datatable(
  escape = FALSE,
  monthly_df_filtered_2,
  options = list(pageLength = 150,
                 columnDefs = list(list(className = 'dt-center',
                                        targets = 0:8))),
  class = 'cell-border stripe',
  rownames = FALSE,
  colnames = column_names,
  caption = htmltools::tags$caption(
    style = 'caption-side: top; text-align: left; padding-top: 10px',
    str_c(chart_subtitle, " for ", chart_title)
  )
)

#
dt <- dt %>%
  formatStyle(
    names(monthly_df_filtered_2), 
    fontFamily = 'Arial', 
    align = 'center')