from backend.abfragenLogik import sql_templates
import pandas as pd

class SQLVerknuepfung:

    sqlTemplates = sql_templates.SQLTemplates()

    def anzahlPatZweiKriterienAND(self, name_char1, name_char2):
        df1 = self.sqlTemplates.pat_df_ein_kriterium_blatt_i2b2(name_char1)
        df2 = self.sqlTemplates.pat_df_ein_kriterium_blatt_i2b2(name_char2)
        df1 = pd.merge(df1, df2, on=['patient_num'], how='inner')
        return df1

    def anzahlPatZweiKriterienOR(self, name_char1, name_char2):
        df1 = self.sqlTemplates.pat_df_ein_kriterium_blatt_i2b2(name_char1)
        df2 = self.sqlTemplates.pat_df_ein_kriterium_blatt_i2b2(name_char2)
        df1 = pd.merge(df1, df2, on=['patient_num'], how='outer')
        return df1