# ------------------------------------------
# MariaDB & Python 연동
# ------------------------------------------
# 모듈 로딩
# import mariadb as mdb
import sys
import psycopg2
import pandas as pd
from datetime import datetime

# PostgreSQL 접속값
conn_params={'host':'localhost',
             'dbname':'steelcut',
            'port':5432,
            'user':'postgres',
            'password':'root'
            }
# ----------------------------------------------------------------------------------------- 
# connection = psycopg2.connect("host=192.168.0.1 dbname=postgres user=postgres password=1234 port=5432")
# 또는
# connection = psycopg2.connect(host="172.20.69.166", dbname="postgres", user="postgres", password="root", port=5432)
connection = psycopg2.connect(**conn_params)
cur = connection.cursor()

# 기존 csv파일 불러와서 DB에 추가
# df=pd.read_csv('./data/선반.csv')
# df=df.drop_duplicates(subset='날짜')
steelfiles={'busheling':'./data/Busheling_price.csv','heavy_scrap':'./data/HeavyScrap_price.csv','light_scrap':'./data/LightScrap_price.csv','turning_scrap':'./data/TurningScrap_price.csv'}
print(steelfiles)
for filename, path in steelfiles.items():
    df=pd.read_csv(path)
    df=df.drop_duplicates(subset='날짜')
    print(len(df.columns))
    for i in range(0,len(df)):
        if len(df.columns)==7:
            try:
                cur.execute(f"INSERT INTO {filename} VALUES ('{df.iloc[i,0]}', {df.iloc[i,1]}, {df.iloc[i,2]}, {df.iloc[i,3]},\
                            {df.iloc[i,4]}, {df.iloc[i,5]}, {df.iloc[i,6]});")
                connection.commit()
                print(df.iloc[i,0])
            except:
                continue


        elif len(df.columns)==13:
            try:
                cur.execute(f"INSERT INTO {filename} VALUES ('{df.iloc[i,0]}', {df.iloc[i,1]}, {df.iloc[i,2]}, {df.iloc[i,3]}, {df.iloc[i,4]}, {df.iloc[i,5]}, {df.iloc[i,6]},\
                        {df.iloc[i,7]}, {df.iloc[i,8]}, {df.iloc[i,9]}, {df.iloc[i,10]}, {df.iloc[i,11]}, {df.iloc[i,12]});"
                        )
                connection.commit()
                print(df.iloc[i,0])
            except:
                continue
