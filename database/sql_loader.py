import sqlalchemy as sal

def load_data(df):
    engine = sal.create_engine(
        "mssql+pyodbc://@LocalSQL"
    )
    conn = engine.connect()
    print("Connected successfully")
    
    #load the data into sql server using append option
    df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')