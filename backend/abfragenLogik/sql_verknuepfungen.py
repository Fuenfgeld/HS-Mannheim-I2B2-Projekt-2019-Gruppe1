from backend.abfragenLogik import sql_templates


class SQLVerknuepfung:

    sqlTemplates = sql_templates.SQLTemplates()

    def anzahlPatZweiKriterienAND(self, name_char1, name_char2):
        df1 = self.sqlTemplates.c_basecode_from_i2b2_ein_kriterium_blatt(name_char1)
        df2 = self.sqlTemplates.c_basecode_from_i2b2_ein_kriterium_blatt(name_char2)
        AND = 0
        for n in range(0, len(df1)):
            m = df1.loc[n].values[0]
            for z in range(0, len(df2)):
                if m == df2.loc[z].values[0]:
                    AND += 1
        return AND

    def anzahlPatZweiKriterienOR(self, name_char1, name_char2):
        df1 = self.sqlTemplates.c_basecode_from_i2b2_ein_kriterium_blatt(name_char1)
        df2 = self.sqlTemplates.c_basecode_from_i2b2_ein_kriterium_blatt(name_char2)
        OR = 0
        AND = 0
        for n in range(0, len(df1)):
            m = df1.loc[n].values[0]
            for z in range(0, len(df2)):
                if m != df2.loc[z].values[0]:
                    OR += 1
                elif m == df2.loc[z].values[0]:
                    AND += 1
        return OR + AND