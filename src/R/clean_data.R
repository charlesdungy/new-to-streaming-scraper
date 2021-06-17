library(lubridate)
library(tidyverse)

current_month <- as.character(month(today(), label = TRUE, abbr = FALSE))
current_month_lower <- str_to_lower(current_month)
current_year <- as.character(year(now()))

# Import data ------------------------------------------------------------------
file_name <- str_c("../../data/raw/whatsonnetflix_", current_month_lower, ".csv")
df <- read_csv(file_name, col_names = FALSE)
netflix_df <- df

# Drop X1, rename X2 to Title, create Temp_Date in order to extract date -------
netflix_df <- netflix_df %>%
  select(-(X1)) %>%
  rename(Title = X2) %>%
  mutate(Temp_Date = case_when(
    str_detect(Title, "Coming to Netflix") ~ Title))

# 
netflix_df <- netflix_df %>% 
  fill(Temp_Date) %>%
  mutate(Weekly = case_when(
    str_detect(Temp_Date, "Weekly") ~ "Yes", TRUE ~ "No")) %>%
  mutate(Date_Arriving = str_match(Temp_Date, paste(current_month, "\\d+"))) %>%
  mutate(Date_Arriving = case_when(
    !str_detect(Date_Arriving, current_year) ~ 
      str_c(Date_Arriving, sep = " ", current_year), TRUE ~ Date_Arriving)) %>%
  mutate(Date_Arriving = mdy(Date_Arriving))

# 
netflix_df <- netflix_df %>% 
  mutate(Type = case_when(
    str_detect(Title, "Season|Series|Collection|Part") ~ "TV", TRUE ~ "Movie"))

# 
netflix_df <- netflix_df %>% 
  mutate(Season_Year = str_extract(Title, "\\((.*)\\)")) %>%
  mutate(Season_Year = str_replace_all(Season_Year, "[//(//)]", "")) %>%
  mutate(Title = str_replace(Title, "\\s\\((.*)\\)", "")) %>%
  filter(!str_detect(Title, "Coming to Netflix"))

# 
netflix_df <- netflix_df %>% 
  mutate(Season = case_when(
    str_detect(Season_Year, "Season|Series|Collection|Part") ~ Season_Year,
    TRUE ~ "")) %>%
  mutate(Year = case_when(
    !str_detect(Season_Year, "Season|Series|Collection|Part") ~ Season_Year,
    TRUE ~ "0"))

# 
netflix_df <- netflix_df %>% 
  slice(2:n()) %>%
  select(-c(Temp_Date, Season_Year)) %>%
  mutate(Year = str_replace_all(Year, "[^0-9]", ""))

# 
netflix_df <- netflix_df %>% 
  relocate(Date_Arriving, .after = Title) %>%
  relocate(Year, .after = Type) %>%
  relocate(Weekly, .after = Season) %>%
  arrange(Type, Date_Arriving, Title, Year)

#
file_ext <- ".csv"
file_name <- str_c("netflix", sep = "_", current_month_lower)
file_name <- str_c(file_name, sep = "", file_ext)
file_path <- str_c("../../data/processed/", sep = "", file_name)

# 
write_csv(
  netflix_df, 
  file = file_path)