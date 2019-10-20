import pandas as pd

### Creates a dataframe from a URL that points to a CSV file
def create_dataframe(url):
    df = pd.read_csv(url)
    return df


#### Takes as input:
####      df = a pandas DataFrame 
####      columnNames = a list of column names
#### The function returns True if the following conditions hold:
####      - The DataFrame contains only the columns that you specified as the second argument.
####      - The values in each column have the same python type
####      - There are at least 10 rows in the DataFrame.
def test_create_dataframe(df,columnNames):
    # Check if the DataFrame contains only the columns that you specified as the second argument
    columnNames_actual = df.columns.tolist()
    correctColumns = (set(columnNames_actual)==set(columnNames))
    
    # Check if there are at least 10 rows in the DataFrame.
    minRows = 10
    count_row,count_col = df.shape
    enoughRows = count_row>=minRows
    
    # Check if the values in each column have the same python type
    consistentDataTypes=True
    for column in df:
        consistentDataTypes_thisColumn = True
        column_values = df[column].tolist()
        column_types = [type(item) for item in column_values]
        numTypes = len(set(column_types))
        if numTypes > 1:
            consistentDataTypes_thisColumn = False
        consistentDataTypes = (consistentDataTypes and consistentDataTypes_thisColumn)
    
    # Return as True if all conditions are met
    return (correctColumns and enoughRows and consistentDataTypes)