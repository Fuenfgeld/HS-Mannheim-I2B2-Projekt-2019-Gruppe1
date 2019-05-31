from backend.sql import formatted_sql


class queryBar:

    def __init__(self):
        self.icd_list = []
        self.name_list = []

    def append_icd_list(self, icd_code):
        self.icd_list.append(icd_code)


    def delete_icd_list_items(self):
        self.icd_list.clear()
        # bei Löschen der Abfrage; neuer Aufruf von len_icd_aufruf nötig (wo?)

    def append_name_list(self, icd_name):
        if len(self.name_list) % 2 == 0:
            self.name_list.append(icd_name)
        elif len(self.name_list) % 2 == 1:
            self.name_list.append(" AND ")
            self.name_list.append(icd_name)

    def print_name_list(self):
        ausgabe = ''
        if self.name_list[0] is None:
            return 'Abfrageleiste'
        else:
            for i in range(0, len(self.name_list)):
                ausgabe = ausgabe + self.name_list[i]
        return ausgabe

    def delete_name_list_items(self):
        self.name_list.clear()
        # bei Löschen der Abfrage; neuer Aufruf von len_icd_aufruf nötig (wo?)

    def len_icd_aufruf(self):
        if len(self.icd_list) == 0:
            return formatted_sql.build_SQL_patient_dimension()
        elif len(self.icd_list) == 1:
            return formatted_sql.build_SQL_i2b2_observation_fact_krit1(self.icd_list[0])
        elif len(self.icd_list) == 2:
            return formatted_sql.build_SQL_i2b2_observation_fact_krit2(self.icd_list[0], self.icd_list[1])


