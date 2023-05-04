# Portfolio Management System

This my repository for the work for my Senior year Capstone Project (Stock news collection using Web Scraping and Stock price prediction) using Machine Learning Models.

## Overview
The goal is to build a machine learning model which is capable to take historical stock news using API or web scraping, and perform sentiment analysis on the headline of the news to predict the future outcome of the news in the stock market. Also, see a relation of other assests affecting the stock market.

## Summary of Workdone

### Data

#### Web scraping to collect data:
For collecting the historical stock news I chose FinViz website. This website is a stock screener which has all stock information, market prices along with news related to each particular stock. Also it has updated information on the performance of each sector, industry and any major stock index. Below is a quick look how the stock news are arranged for each ticker, for example: 'AMZN'
   * ![pics](https://github.com/lasta11/DATA-CAPSTONE-PROJECT/blob/main/Example%20Images/Finviz%20News.png)

Using python to parse this website and get date, ticker, and the headline of the news over a period of time. I used libraries like BeautifulSoup, requests, json to parse the website, extract the news the HTML, which looks like this: 
  * ![pics](https://github.com/lasta11/DATA-CAPSTONE-PROJECT/blob/main/Example%20Images/HTML%20Scraping.png)
  
  As we can see that each news are stored into a table with id='news-table' bounded by <tr>tags for the time data and <a></a> tags for the news headline tags, also we can see use similar method to get the news URL if we want for further use.  

  
* Preprocessing/ Clean up:
  
  For the preprocessing part, I iterate through all tr tags from the previous step and get the text for date, time, ticker and headline. I further format it into a list of lists for each news headline in proper format of [['ticker1','YYYY-MM-DD', 'HH:MMPM', 'News Headline1'], ['ticker1','YYYY-MM-DD', 'HH:MMPM', 'News Headline2']]


### Problem Formulation:

* Sentiment Analysis
  
  First step, to the project after the stock news collection was to perform sentiment analysis on the news data collected and assign a compuund score -1 being the highest negative and 1 being the highest positive and 0 being neutral. For example for 'AMZN' the compound sentiment was:
  
  * ![pics](https://github.com/lasta11/DATA-CAPSTONE-PROJECT/blob/main/Example%20Images/CompoundStock%20Sentiment.png)
  
  

*Prediction using Machine Learning

### Training
Model 1:

Model 2:


### Performance Comparison
Metrics Evaluation:


### Challenges 

### Future Work


## How to reproduce results


### Overview of files in repository


### Software Setup
* Packages used in notebook: 


### References:
*


