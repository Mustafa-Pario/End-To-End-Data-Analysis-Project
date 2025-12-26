import pandas as pd

def transform_data():
    #read data from the file and handle null values
    df = pd.read_csv('orders.csv', na_values=['Not Available', 'unknown'])
    
    #rename columns names ..make them lower case and replace space with underscore
    df.columns=df.columns.str.lower()
    df.columns=df.columns.str.replace(' ','_')
    
    #derive new columns discount , sale price and profit
    df['discount']=df['list_price']*df['discount_percent']*.01
    df['sale_price']= df['list_price']-df['discount']
    df['profit']=df['sale_price']-df['cost_price']
    
    #convert order date from object data type to datetime
    df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")
    
    #drop cost price list price and discount percent columns
    df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)
    
    return df