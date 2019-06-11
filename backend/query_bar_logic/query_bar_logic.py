from backend.sql_logic import sql_builder


class queryBar:

    def __init__(self):
        self.icd_list_decimal = []
        self.icd_list_sex_cd = []
        self.icd_list_language_cd = []
        self.icd_list_age_in_years_num = []
        self.icd_list_race_cd = []
        self.name_list = []

    def get_icd_code_from_name(self, name):
        return sql_builder.build_SQL_i2b2_metadata_i2b2_code(name)

    def append_icd_list_decimal(self, code):
        self.icd_list_decimal.append(code)

    def delete_icd_list_decimal_items(self):
        self.icd_list_decimal.clear()

    def append_icd_list_sex_cd(self, code):
        self.icd_list_sex_cd.append(code)

    def delete_icd_list_sex_cd_items(self):
        self.icd_list_sex_cd.clear()

    def append_icd_list_race_cd(self, code):
        self.icd_list_race_cd.append(code)

    def delete_icd_list_race_cd_items(self):
        self.icd_list_race_cd.clear()

    def append_icd_list_language_cd(self, code):
        self.icd_list_language_cd.append(code)

    def delete_icd_list_language_cd_items(self):
        self.icd_list_language_cd.clear()

    def append_icd_list_age_in_years_num(self, code):
        self.icd_list_age_in_years_num.append(code)

    def delete_icd_list_age_in_years_num_items(self):
        self.icd_list_age_in_years_num.clear()

    def append_name_list(self, name):
        if len(self.name_list) % 2 == 0:
            self.name_list.append(name)
        elif len(self.name_list) % 2 == 1:
            self.name_list.append(" OR ")
            self.name_list.append(name)

    def print_name_list(self):
        result = ''
        for i in range(0, len(self.name_list)):
            result = result + self.name_list[i]
        return result

    def delete_name_list_items(self):
        self.name_list.clear()

    def get_all_patients_within_icd_list_decimal(self):
        if len(self.icd_list_decimal) == 0:
            return sql_builder.build_SQL_i2b2_patient_dimension_patient_num()
        elif len(self.icd_list_decimal) == 1:
            return sql_builder.build_SQL_i2b2_observation_fact_1_criterium(self.icd_list_decimal[0])
        elif len(self.icd_list_decimal) == 2:
            return sql_builder.build_SQL_i2b2_observation_fact_2_criteria(self.icd_list_decimal[0],
                                                                          self.icd_list_decimal[1], self.name_list[1])

    def get_all_patients_within_icd_list_sex_cd(self):
        if len(self.icd_list_sex_cd) == 0:
            return sql_builder.build_SQL_i2b2_patient_dimension_patient_num()
        elif len(self.icd_list_sex_cd) == 1:
            return sql_builder.build_SQL_i2b2_observation_fact_1_criterium(self.icd_list_sex_cd[0])
        elif len(self.icd_list_sex_cd) == 2:
            return sql_builder.build_SQL_i2b2_observation_fact_2_criteria(self.icd_list_sex_cd[0],
                                                                          self.icd_list_sex_cd[1], self.name_list[1])

    def get_all_patients_within_icd_list_language_cd(self):
        if len(self.icd_list_language_cd) == 0:
            return sql_builder.build_SQL_i2b2_patient_dimension_patient_num()
        elif len(self.icd_list_language_cd) == 1:
            return sql_builder.build_SQL_i2b2_observation_fact_1_criterium(self.icd_list_language_cd[0])
        elif len(self.icd_list_language_cd) == 2:
            return sql_builder.build_SQL_i2b2_observation_fact_2_criteria(self.icd_list_language_cd[0],
                                                                          self.icd_list_language_cd[1],
                                                                          self.name_list[1])

    def get_all_patients_within_icd_list_age_in_years_num(self):
        if len(self.icd_list_age_in_years_num) == 0:
            return sql_builder.build_SQL_i2b2_patient_dimension_patient_num()
        elif len(self.icd_list_age_in_years_num) == 1:
            return sql_builder.build_SQL_i2b2_observation_fact_1_criterium(self.icd_list_age_in_years_num[0])
        elif len(self.icd_list_age_in_years_num) == 2:
            return sql_builder.build_SQL_i2b2_observation_fact_2_criteria(self.icd_list_age_in_years_num[0],
                                                                          self.icd_list_age_in_years_num[1],
                                                                          self.name_list[1])

    def get_all_patients_within_icd_list_race_cd(self):
        if len(self.icd_list_race_cd) == 0:
            return sql_builder.build_SQL_i2b2_patient_dimension_patient_num()
        elif len(self.icd_list_race_cd) == 1:
            return sql_builder.build_SQL_i2b2_observation_fact_1_criterium(self.icd_list_race_cd[0])
        elif len(self.icd_list_race_cd) == 2:
            return sql_builder.build_SQL_i2b2_observation_fact_2_criteria(self.icd_list_race_cd[0],
                                                                          self.icd_list_race_cd[1], self.name_list[1])
