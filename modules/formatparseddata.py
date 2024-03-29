# -*- coding: utf-8 -*-
"""formatParsedData.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1re-dh3zI9x5LOvF0fRjezKZMhOBSlVFf
"""

def parse_dates(parsed_news):
    years = {"23": "2023", "22": "2022", "21": "2021", "20": "2020"}
    months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    
    for x in range(len(parsed_news)):
        splitted = parsed_news[x][1].split("-")
        parsed_news[x][1] = years[splitted[-1]] + "-" + months[splitted[0]] + "-" + splitted[1]
    
    return parsed_news