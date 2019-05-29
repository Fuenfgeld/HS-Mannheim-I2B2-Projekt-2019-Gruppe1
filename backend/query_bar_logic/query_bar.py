from backend.sql import formatted_sql


class queryBar:

    def __init__(self):
        self.icd_list = []
        self.name_list = []

    def append_icd_list(self, icd_code):
        self.icd_list.append(icd_code)
        return self.icd_list

    def len_icd_aufruf(self):
        if len(self.icd_list) == 0:
            return formatted_sql.build_SQL_patient_dimension()
        elif len(self.icd_list) == 1:
            return formatted_sql.build_SQL_i2b2_observation_fact_krit1(self.icd_list[0])
        elif len(self.icd_list) == 2:
            return formatted_sql.build_SQL_i2b2_observation_fact_krit2(self.icd_list[0], self.icd_list[1])

    def append_name_list(self, icd_name):
        if len(self.name_list) % 2 == 0:
            self.name_list.append(icd_name)
            return self.name_list
        elif len(self.name_list) % 2 == 1:
            self.name_list.append(" AND ")
            self.name_list.append(icd_name)
            return self.name_list
