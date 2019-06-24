from backend.data_frame_logic import data_frame_current_patients
from backend.data_frame_logic import data_frame_logic_new


class queryBarLogicNew:

    def __init__(self):
        self.name_list = []
        self.con_list = ['AND', 'AND']
        self.df_list = []
        self.current_over_all_df = data_frame_logic_new.generate_df_default()

    def append_selection(self, name):
        self.append_name_list(name)
        self.append_df_list(name)
        self.update_current_over_all_df()

    def delete_all(self):
        self.delete_name_list_items()
        self.delete_df_list()
        self.con_list[0] = 'AND'
        self.con_list[1] = 'AND'
        self.update_current_over_all_df()

    def get_actual_over_all_df(self):
        return self.current_over_all_df

    def update_current_over_all_df(self):
        if len(self.name_list) == 0:
            self.current_over_all_df = data_frame_logic_new.generate_df_default()
        if len(self.name_list) == 1:
            self.current_over_all_df = self.df_list[0]
        if len(self.name_list) == 2:
            self.current_over_all_df = data_frame_logic_new.generate_df_two_criteria(self.con_list, self.df_list)
        if len(self.name_list) == 3:
            self.current_over_all_df = data_frame_logic_new.generate_df_three_criteria(self.con_list, self.df_list)

    # private methods:

    def append_name_list(self, name):
        self.name_list.append(name)

    def delete_name_list_items(self):
        self.name_list.clear()

    def append_df_list(self, name):
        self.df_list.append(data_frame_current_patients.build_df_pat_num_all(name))

    def delete_df_list(self):
        self.df_list.clear()






