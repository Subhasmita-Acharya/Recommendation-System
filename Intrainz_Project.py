import pandas as pd

data = pd.read_excel("OnlineRetail.xlsx")
df = data[:]
df_cq = df[['StockCode','InvoiceDate','Country','Quantity']]
data.groupby(['StockCode', 'Country'])['Quantity'].mean().sort_values(ascending=False) 
data.groupby(['StockCode', 'Country'])['Quantity'].count().sort_values(ascending=False)

def global_s():
    Global_stock = pd.DataFrame(df_cq.groupby('StockCode')['Quantity'].mean().sort_values(ascending=False))
    return Global_stock.head()

def country():
    Countrys = pd.DataFrame(df_cq.groupby(['Country', 'StockCode'])['Quantity'].mean())
    Countrys_stock = Countrys['Quantity'].groupby('Country', group_keys=False)
    res = Countrys_stock.apply(lambda x: x.sort_values(ascending=False).head())
    return res

def month():
    dts = pd.to_datetime(df_cq['InvoiceDate'])
    dts = dts.dt.normalize()
    dts_m = df[['StockCode','Quantity']].copy()
    dts_m['Month'] = dts.dt.month
    Months = pd.DataFrame(dts_m.groupby(['Month', 'StockCode'])['Quantity'].mean())
    Months_stock = Months['Quantity'].groupby('Month', group_keys=False)
    res_m = Months_stock.apply(lambda x: x.sort_values(ascending=False).head())
    return res_m

print('\nStockCode of Top 5 Globally recommended products with their average sale value are:\n',global_s())
print('\nStockCode of Top 5 Country-wise recommended products with their average sale value are:\n',country())
print('\nStockCode of Top 5 Month-wise recommended products with their average sale value are:\n',month())

'''
Output:
StockCode of Top 5 Globally recommended products with their average sale value are:
              Quantity
StockCode            
47556B     957.750000
84826      359.078947
16014      246.814815
79063D     211.538462
79062D     202.400000

StockCode of Top 5 Country-wise recommended products with their average sale value are:
 Country      StockCode
Australia    15036        600.0
             21899        576.0
             21900        576.0
             21902        576.0
             21984        432.0
                          ...
Unspecified  84077         48.0
             47021G        48.0
             22439         40.0
             23119         36.0
             22952         36.0
Name: Quantity, Length: 190, dtype: float64

StockCode of Top 5 Month-wise recommended products with their average sale value are:
 Month  StockCode
1      37413        5568.000000
       79063D       2560.000000
       47556B       1300.000000
       17021         303.000000
       17003         244.692308
2      22053         996.500000
       16014         750.500000
       18007         609.750000
       79062D        486.000000
       44235         432.000000
3      16014         530.000000
       21897         342.000000
       17003         226.400000
       22440         161.222222
       84568         153.812500
4      47556B       1300.000000
       84077         235.883721
       17038         200.000000
       75131         196.500000
       22543         176.333333
5      16014         346.375000
       22702         320.666667
       22608         288.000000
       22609         288.000000
       22243         175.857143
6      16216         287.666667
       16045         150.000000
       17003         149.450000
       15034         147.363636
       84568         120.700000
7      22339         288.000000
       84568         264.157895
       17084R        216.000000
       23001         200.000000
       21181         192.000000
8      16014         295.000000
       22337         288.000000
       62018         250.600000
       23431         200.000000
       16259         162.000000
9      84212         302.400000
       16014         212.200000
       16218         120.000000
       17003         113.631579
       35598B        106.000000
10     84212         178.000000
       22102         156.400000
       84077         138.644068
       22710         135.714286
       62018         135.666667
11     84826        2510.200000
       16014         360.600000
       21586         144.000000
       16045         111.111111
       17084R        108.000000
12     17096         577.000000
       17084R        432.000000
       22693         169.058824
       22856         153.000000
       23446         144.000000
Name: Quantity, dtype: float64

'''