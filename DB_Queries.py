import pandas.io.sql as psql
import psycopg2 as pg

connection = pg.connect(user="i2b2",
                        password="demouser",
                        host="129.206.7.75",
                        port="5432",
                        database="i2b2")

# cursor = connection.cursor()
#
# cursor.execute("SELECT version();")
#
# record = cursor.fetchone()
#
# print('You are connected to -', record)

dfPat = psql.read_sql_query("SELECT * FROM i2b2demodata.patient_dimension", con=connection)
dfVis = psql.read_sql_query("SELECT * FROM i2b2demodata.visit_dimension", con=connection)
#    ^^^^^^^^^^^^^^^^^^^  workaround to not work with cursor

# ICD10lvl1 = psql.read_sql_query("select * from i2b2.i2b2metadata.icd10_icd9 "
#                                 "where c_hlevel = 1 and c_fullname like '%Diagnoses%'", con=connection)
#
# ICD10lvl2 = psql.read_sql_query("select * from i2b2.i2b2metadata.icd10_icd9 "
#                                 "where c_hlevel = 2 and c_fullname like '%Diagnoses%'", con=connection)
#
# ICD10lvl3 = psql.read_sql_query("select * from i2b2.i2b2metadata.icd10_icd9 "
#                                 "where c_hlevel = 3 and c_fullname like '%Diagnoses%'", con=connection)
#
# ICD10lvl4 = psql.read_sql_query("select * from i2b2.i2b2metadata.icd10_icd9 "
#                                 "where c_hlevel = 4 and c_fullname like '%Diagnoses%'", con=connection)

# query that gets us the whole dataset in the given level of the ICD
def get_icd_level_query_df(icdLevel):
    dfICDLevel = psql.read_sql_query(f"""
                        select c_hlevel as level, c_name as name, c_basecode as ICDcode, c_tooltip as pathSimple
                        from i2b2.i2b2metadata.icd10_icd9
                        where c_fullname like '%Diagnoses%' and c_basecode like 'ICD10%' 
                        and c_hlevel = {icdLevel} 
                        order by c_basecode""",
                                     con=connection)
    print(dfICDLevel.head)
    return dfICDLevel  # returns the query as dataframe
