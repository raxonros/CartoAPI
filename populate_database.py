import pgdb as pg

username = 'carto'
password = 'carto'
database = 'carto'

conn =  pg.Connection( host="postgres", port= 5432, user=username, password=password, database=database )

conn.autocommit = True
cursor = conn.cursor()

sql_create_table= '''CREATE TABLE paystats(id int NOT NULL,\
    amount FLOAT,\
    p_month DATE, \
    p_age varchar(30),\
    p_gender varchar(30),\
    postal_code_id int,\
    PRIMARY KEY (id));'''



cursor.execute(sql_create_table)

sql_import_csv = '''COPY paystats(amount,\
    p_month,p_age,p_gender,postal_code_id,id)\
    FROM '/data_csv/paystats.csv'\
    DELIMITER ','\
    CSV HEADER;'''

cursor.execute(sql_import_csv)


conn.commit()
conn.close()