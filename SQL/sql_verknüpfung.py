import SQL.sql_templates as sqlT


class sqlVerknüpfung:

    def anzahlPatZweiKriterienAND(self, name_char, name_char1):
        df1 = sqlT.anzahlPatEinKriteriumBlatti2b2(name_char)
        df2 = sqlT.anzahlPatEinKriteriumBlatti2b2(name_char1)
        AND = 0
        for n in range(0, len(df1)):
            m = df1.loc[n].values[0]
            for z in range(0, len(df2)):
                if m == df2.loc[z].values[0]:
                    AND += 1
        return AND

    def anzahlPatZweiKriterienOR(self, name_char, name_char1):
        df1 = sqlT.anzahlPatEinKriteriumBlatti2b2(name_char)
        df2 = sqlT.anzahlPatEinKriteriumBlatti2b2(name_char1)
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
