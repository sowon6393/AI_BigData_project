# ------------------------------------------
# PostgreSQL & Python 연동
# ------------------------------------------
# 모듈 로딩
import sys
import psycopg2 as pg2
import pandas as pd
from datetime import datetime

# PostgreSQL 접속값
# conn_params={'host':'211.199.70.9',
#             'port':315,
#             'user':'kynu',
#             'password':'kynuPW12!@'
#             }

conn_params={'host':'localhost',
             'dbname':'steelcut',
            'port':5432,
            'user':'postgres',
            'password':'root'
            }
conn = pg2.connect(**conn_params)
cur = conn.cursor()

sql_busheling='''CREATE TABLE IF NOT EXISTS public.busheling
(
    date date NOT NULL,
    "BA_K" integer,
    "BA_K_ud" integer,
    "BA_Y" integer,
    "BA_Y_ud" integer,
    "BA_M" integer,
    "BA_M_ud" integer,
    CONSTRAINT steeldata_pkey PRIMARY KEY (date)
)
;'''
sql_heavy_scrap='''CREATE TABLE IF NOT EXISTS public.heavy_scrap
(
    date date NOT NULL,
    "HSA_K" integer,
    "HSA_K_ud" integer,
    "HSA_Y" integer,
    "HSA_Y_ud" integer,
    "HSA_M" integer,
    "HSA_M_ud" integer,
    CONSTRAINT heavy_scrap_pkey PRIMARY KEY (date)
);'''

sql_light_scrap='''CREATE TABLE IF NOT EXISTS public.light_scrap
(
    date date NOT NULL,
    "LSA_K" integer,
    "LSA_K_ud" integer,
    "LSA_Y" integer,
    "LSA_Y_ud" integer,
    "LSA_M" integer,
    "LSA_M_ud" integer,
    CONSTRAINT light_scrap_pkey PRIMARY KEY (date)
)
;'''

sql_turning_scrap='''CREATE TABLE IF NOT EXISTS public.turning_scrap\
(
    date date NOT NULL,
    "TSA_K" integer,
    "TSA_K_ud" integer,
    "TSA_Y" integer,
    "TSA_Y_ud" integer,
    "TSA_M" integer,
    "TSA_M_ud" integer,
    "TSC_K" integer,
    "TSC_K_ud" integer,
    "TSC_Y" integer,
    "TSC_Y_ud" integer,
    "TSC_M" integer,
    "TSC_M_ud" integer,
    PRIMARY KEY (date)
);'''

cur.execute(sql_busheling)
cur.execute(sql_heavy_scrap)
cur.execute(sql_light_scrap)
cur.execute(sql_turning_scrap)
conn.commit()