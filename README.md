# New to Streaming Scraper

This is a web scraping project built with Python, R, and SQL. 

The scraped data are movie and TV show information. The goal of the project is to show new to streaming titles that arrive on Netflix monthly with additional details, such as critic and audience ratings.

~~Current stage: Preparing how to present data with R Markdown.~~
> ~~Testing at: https://no-longer-hosted.com~~

~~Future stage: Complete documentation, comments.~~

Note: Though GitHub may be hosting this project's demo, this project will see no future updates.

## Description

Data are retrieved from two different data sources: [What's on Netflix](https://www.whats-on-netflix.com) (WON) and [Rotten Tomatoes](https://www.rottentomatoes.com) (RT). RT data are cleaned and transformed with Python, while WON data are cleaned and transformed with R.

All data are piped into a MySQL database, then retrieved for presentation in R.

Here is a high-level look at the pipeline:<br>

![Pipeline](https://github.com/charlesdungy/new-to-streaming-scraper/blob/main/data/images/new-to-streaming-pipeline.png?raw=true)

###### *Data Source 1 is WON data. Data Source 2 is RT data.*

## Main Packages/Tools

### Python

* [NumPy](https://numpy.org)
* [pandas](https://pandas.pydata.org)
* [Scrapy](https://scrapy.org)

### R

* [Highcharter](https://jkunst.com/highcharter/)
* [htmlwidgets](http://www.htmlwidgets.org/index.html)
* [R Markdown](https://rmarkdown.rstudio.com)
* [Tidyverse](https://www.tidyverse.org)

### SQL

* [MySQL](https://www.mysql.com)

## Current Directory Tree

![tree](https://github.com/charlesdungy/new-to-streaming-scraper/blob/main/data/images/tree.png?raw=true)

## License

MIT