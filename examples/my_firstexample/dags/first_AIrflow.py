from airflow.models import DAG
from  airflow.providers.sqlite.operators.sqlite import SqliteOperator
from datetime import datetime

default_args={
'start_date':datetime(2021,1,1)
}

with DAG('user_processing',schedule_interval='@daily',
         start_date=datetime(2021,1,1),catchup=False) as dag:

  creating_table= SqliteOperator(task_id='creating_table',
                                 sqlite_conn_id='db_sqlite',
                                 sql='''
                                 CREATE TABLE users
                                 (user_id INTEGER PRIMARY_KEY AUTOINCREMENT,
                                 firstname TEXT NOT NULL,
                                 lastname TEXT NOT NULL,
                                 country TEXT NOT NULL,
                                 username TEXT NOT NULL,
                                 password TEXT NOT NULL,
                                 email TEXT NOT NULL PRIMARY KEY);
                                 '''
                                 )