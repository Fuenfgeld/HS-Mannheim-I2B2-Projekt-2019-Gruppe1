from backend.sql_logic import sql_builder


class queryBar:

    def __init__(self):
        self.icd_list = []
        self.name_list = []

    def get_icd_code_from_name(self, name):
        return sql_builder.build_SQL_i2b2_metadata_i2b2_code(name)

    def append_icd_list(self, code):
        self.icd_list.append(code)

    def delete_icd_list_items(self):
        self.icd_list.clear()

    def append_name_list(self, name):
        if len(self.name_list) % 2 == 0:
            self.name_list.append(name)
        elif len(self.name_list) % 2 == 1:
            self.name_list.append(" AND ")
            self.name_list.append(name)

    def delete_name_list_items(self):
        self.name_list.clear()

    def get_all_patients_within_icd_list(self):
        if len(self.icd_list) == 0:
            return sql_builder.build_SQL_i2b2_patient_dimension_patient_num()
        elif len(self.icd_list) == 1:
            return sql_builder.build_SQL_i2b2_observation_fact_1_criterium(self.icd_list[0])
        elif len(self.icd_list) == 2:
            return sql_builder.build_SQL_i2b2_observation_fact_2_criteria(self.icd_list[0],
                                                                          self.icd_list[1], self.name_list[1])
        elif len(self.icd_list) == 3:
            return sql_builder.build_SQL_i2b2_observation_fact_3_criteria(self.icd_list[0], self.icd_list[1],
                                                                          self.icd_list[2], self.name_list[1],
                                                                          self.name_list[3])
