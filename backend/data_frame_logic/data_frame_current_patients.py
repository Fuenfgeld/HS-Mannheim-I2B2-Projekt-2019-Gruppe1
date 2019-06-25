from config import database
import pandas as pd


def build_df_c_fullname(c_name):
    dffirst = pd.read_sql(f'select icd.c_fullname from i2b2metadata.icd10_icd9 as icd '
                          f'where icd.c_name = \'{c_name}\'', con=database.engine)
    return dffirst

def build_df_c_basecode(c_fullname):
    dfnext = pd.read_sql(f'select distinct icd10_icd9.c_basecode from i2b2metadata.icd10_icd9 as icd10_icd9 '
                         f'join i2b2demodata.observation_fact as obfa on obfa.concept_cd = icd10_icd9.c_basecode '
                         f'join i2b2demodata.patient_dimension as pd on pd.patient_num=obfa.patient_num '
                         f'where icd10_icd9.c_fullname like \'{c_fullname}%%\'', con=database.engine)
    return dfnext

def replace_slash(str):
    str = str.replace('\\', '_')
    return str

def format_str_last(abc):
    fs = f' or obfa.concept_cd = \'{abc}\''
    return fs

def format_str_first(abc):
    fs = f'\'{abc}\''
    return fs

def build_df_pat_num(a):
    b = f'select distinct obfa.patient_num from i2b2demodata.observation_fact as obfa where obfa.concept_cd = {a}'
    return b


def build_df_pat_num_all(name):
    a = ""
    c_fullname = (build_df_c_fullname(name)).loc[0].values[0]
    c_fullname_re_sl = replace_slash(c_fullname)
    build_icd_code = build_df_c_basecode(c_fullname_re_sl)
    if build_icd_code.empty :
        d = {'patient_num': []}
        df_tmp = pd.DataFrame(data=d)
        return df_tmp
    for i in range(0, len(build_icd_code)):
        if len(build_icd_code) == 1 or i == 1:
            a = a.__add__(format_str_first(build_icd_code.loc[i].values[0]))
        elif len(build_icd_code) > 1 and i > 1:
            a = a.__add__(format_str_last(build_icd_code.loc[i].values[0]))
        #print(a)
    df_tmp = pd.read_sql(build_df_pat_num(a), con=database.engine)
    return df_tmp


