# import dash_core_components as dcc
import dash_html_components as html

import DB_Queries as db  # import from the file with the database query


# import plotly.graph_objs as go

def add_levels_icd():
    add_groundlevel()
    add_sublevels()


def add_groundlevel():
    groundLeveldf = db.get_icd_level_query_df(1)
    listGroundLevelDiv = []
    icdClasses = groundLeveldf['name']
    # print(groundLeveldf['name'])

    for i in range(len(icdClasses)):
        listGroundLevelDiv.append(html.Div(f'{icdClasses[i]}', className='caret'))

    print(listGroundLevelDiv)
    return listGroundLevelDiv


# def add_sublevels():
#     adsfa

add_groundlevel()
