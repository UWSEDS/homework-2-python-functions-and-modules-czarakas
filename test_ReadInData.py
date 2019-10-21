### HW2
### Claire Zarakas

import ReadInData
thisurl = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
columnNames_true = ['Date','Fremont Bridge East Sidewalk','Fremont Bridge West Sidewalk']
df = ReadInData.create_dataframe(url=thisurl)

def test_one_shot():
    assert(ReadInData.test_create_dataframe(df,columnNames_true))

## Same column names in different order
def test_columnNames_diffOrder():
    columnNames = ['Fremont Bridge East Sidewalk', 'Date', 'Fremont Bridge West Sidewalk']
    assert(ReadInData.test_create_dataframe(df,columnNames))

## Same column names but missing one
def test_columnNames_missingOne():
    columnNames = ['Date', 'Fremont Bridge East Sidewalk']
    assert(not ReadInData.test_create_dataframe(df,columnNames))

## Same column names but added one
def test_columnNames_addedOne():
    columnNames = ['Date', 'Fremont Bridge East Sidewalk', 'Fremont Bridge West Sidewalk', 'Extra Entry']
    assert(not ReadInData.test_create_dataframe(df,columnNames))

## Missing one column names, one extra column name
def test_columnNames_missingOne_addedOne():
    columnNames = ['Date', 'Fremont Bridge East Sidewalk', 'Extra Entry']
    assert(not ReadInData.test_create_dataframe(df,columnNames))

## Only 5 rows
def test_enoughRows():
    df_alt = df.iloc[0:5]
    assert(not ReadInData.test_create_dataframe(df_alt,columnNames_true))

## First column has one row with an inconsistent type
def test_consistentType_firstColumn():
    df_alt = df
    df_alt['Date'][5]=7
    assert(not ReadInData.test_create_dataframe(df_alt,columnNames_true))

## Last column has one row with an inconsistent type
def test_consistentType_lastColumn():
    df_alt = df
    df_alt['Fremont Bridge West Sidewalk'][5]='No Data'
    assert(not ReadInData.test_create_dataframe(df_alt,columnNames_true))