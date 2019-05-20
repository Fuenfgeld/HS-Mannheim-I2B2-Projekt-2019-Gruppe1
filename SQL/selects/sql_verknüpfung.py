import SQL.selects.sql_templates as sqlT
import pandas as pd


class sqlVerknüpfung:

    def anzahlPatZweiKriterienAND(self, name_char, name_char1):
        df1 = sqlT.pat_df_ein_kriterium_blatt_i2b2(name_char)
        df2 = sqlT.pat_df_ein_kriterium_blatt_i2b2(name_char1)
        df1 = pd.merge(df1, df2, on=['patient_num'], how='inner')
        return df1

    def anzahlPatZweiKriterienOR(self, name_char, name_char1):
        df1 = sqlT.pat_df_ein_kriterium_blatt_i2b2(name_char)
        df2 = sqlT.pat_df_ein_kriterium_blatt_i2b2(name_char1)
        df1 = pd.merge(df1, df2, on=['patient_num'], how='outer')
        return df1
