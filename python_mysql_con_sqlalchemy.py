import pandas as pd
import sqlalchemy

name = input('Enter user name: ')
password = input('Enter password: ')
database_name = input('Enter DB name: ')
engine=sqlalchemy.create_engine('mysql+pymysql://'+name+':'+password+'@localhost:3306/'+database_name)
try:
    df= pd.read_sql('show tables',engine)
    print(df)
except sqlalchemy.exc.OperationalError:
    #this error will raise when we give database name which doesnt exists
    print('connection not established please check given connection details')       
    

   
