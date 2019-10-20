# HW2
Claire Zarakas

Due Week of October 21, 2019

This project directory contains 2 files, as described below:

### ReadInData.py

This python module contains the following 2 functions:

1. create_dataframe: creates a dataframe from a URL that points to a CSV file.

1. test_create_dataframe: takes a pandas DataFrame and list of column names as input, and returns True if the following conditions hold:

  - The DataFrame contains only the columns that you specified as the second argument.
  - The values in each column have the same python type
  - There are at least 10 rows in the DataFrame.

### Check_ReadInData.ipynb
This notebook checks whether the functions in the ReadInData module work as expected, using the remont_Bridge_Hourly_Bicycle_Counts_by_Month_October_2012_to_present dataset downloaded from https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD

ReadInData.py requires pandas.

