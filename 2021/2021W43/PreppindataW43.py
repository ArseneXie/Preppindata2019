import pandas as pd
import datetime

xlsx = pd.ExcelFile(r"C:\Data\PreppinData\2021W43 Input.xlsx")

xlsx.sheet_names

unit_a = pd.read_excel(xlsx, 'Business Unit A ')
unit_a = unit_a.merge(pd.read_excel(xlsx, 'Risk Level'), left_on='Rating', right_on='Risk level')
unit_a['Date lodged'] = unit_a.apply(lambda x: f"{x['Date']}/{x['Month ']}/{x['Year']}", axis=1)
unit_a = unit_a[['Date lodged', 'Status', 'Risk rating']].rename(columns={'Risk rating':'Rating'})
unit_b = pd.read_excel(xlsx, 'Business Unit B ', skiprows=5)[['Date lodged', 'Status', 'Rating']]

rating = pd.concat([unit_a, unit_b])

unit_a['Month']

unit_a.columns

lookup.columns

parse_dates=['Date lodged'],
                       date_parser=lambda x: pd.to_datetime(x, format='%d/%m/%Y')
['Business Unit A ', 'Business Unit B ', 'Risk Level']

process = pd.read_csv("C:\\Data\\PreppinData\\Bike Painting Process - Painting Process.csv")
process['Datetime'] = process.apply(lambda x: pd.to_datetime(f"{x['Date']} {x['Time']}"), axis=1)
process = process.groupby(['Batch No.']).apply(pd.DataFrame.sort_values, 'Datetime', ascending=True).reset_index(drop=True)
 
for attr in ['Bike Type', 'Batch Status', 'Name of Process Stage']:
    process[attr] = process.apply(lambda x: x['Data Value'] if x['Data Parameter']==attr else None, axis=1)
    process[attr] = process.groupby(['Batch No.'])[attr].ffill() 
    
process = process[(process['Data Type']=='Process Data') & (process['Data Parameter']!='Name of Process Stage')]
for vtype in ['Actual', 'Target']:
    process[vtype] = process.apply(lambda x: float(x['Data Value']) if re.match(f'^({vtype})',x['Data Parameter']) else None, axis=1)
process['Data Parameter'] = process['Data Parameter'].apply(lambda x: re.sub('^(\w+\s)','',x))
process = process[['Batch No.', 'Bike Type', 'Batch Status', 'Name of Process Stage',
                   'Data Parameter', 'Actual', 'Target', 'Datetime']]
   

