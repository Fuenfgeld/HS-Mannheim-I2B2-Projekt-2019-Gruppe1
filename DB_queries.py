print('importing')
import pandas.io.sql as psql
import psycopg2 as pg


class Queries:
    print('connecting')
    connection = pg.connect(user="i2b2",
                            password="demouser",
                            host="129.206.7.75",
                            port="5432",
                            database="i2b2")

    print('almost done')

    def get_level(self, level):
        whole_icd = psql.read_sql_query(
            "select c_name as name, c_path as path, c_basecode as icdcode, c_hlevel as level, c_fullname as fullname "
            f"from i2b2metadata.icd10_icd9 where c_hlevel = {level} and c_basecode like 'ICD%' "
            f"order by c_hlevel, c_fullname ",
            con=Queries.connection)  # query into a data frame that contains name. icd code, level, path and fullpath
        # (extended path) of a certain level of the icd catalogue
        return whole_icd

    print('done')
