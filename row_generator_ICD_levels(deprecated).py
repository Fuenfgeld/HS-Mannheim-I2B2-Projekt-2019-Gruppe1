# import dash_core_components as dcc
import dash_html_components as html

import DB_Queries as db  # import from the file with the database query

# import plotly.graph_objs as go

icdSecondLevelQuery = db.get_icd_level_query_df(2)
icdThirdLevelQuery = db.get_icd_level_query_df(3)


def add_levels_icd():
    add_groundlevel()


def add_groundlevel():
    groundLeveldf = db.get_icd_level_query_df(1)
    listGroundLevelDiv = []
    icdClasses = groundLeveldf['name']
    icdCodes = groundLeveldf['icdcode']
    # print(groundLeveldf['name'])

    for i in range(len(icdClasses)):
        listGroundLevelDiv.append(html.Div([
            html.Span(f'{icdClasses[i]}', className='caret'),
            html.Ul(add_second_level(icdCodes[i], 2), className='nested')],
        ))
    # print(icdCodes)
    # print(listGroundLevelDiv)
    return listGroundLevelDiv


# ANYTREE PYTHON

def add_second_level(metaICDCode, level):
    icdCodeString = metaICDCode
    nextLevelList = []
    print(metaICDCode)

    icdNextLevelCodes = icdSecondLevelQuery['icdcode']
    icdCodes = get_icd_names(metaICDCode, icdSecondLevelQuery)

    # print(icdCodes)
    for i in range(len(icdCodes)):
        nextLevelList.append(html.Div([
            html.Span(f'{icdCodes[i]}', className='caret'),
            # html.Ul(add_third_level(icdNextLevelCodes[i]), className='nested'),
        ],
        ),
        )

    # print(nextLevelList)
    # print(icdNextLevelCodes)
    return nextLevelList


# def add_third_level(icdCodeLetter):
#
#     icdCodeLetter = icdCodeLetter[6:8]
#     icdCodeString = 'ICD10:'+icdCodeLetter
#
#     thirdLevelList=[]
#     icdCodes = icdThirdLevelQuery['icdcode']
#     icdCodes = get_icd_codes(icdCodeString, icdCodes)
#     icdNames = icdThirdLevelQuery['name']
#
#     for i in range(len(icdNames)):
#         thirdLevelList.append(html.Div([
#             html.Span(f'{icdNames[i]}', className='caret'),
#             html.Ul('hehe boah', className='nested'),
#         ],
#         ),
#         )
#     print(icdThirdLevelQuery['name'])
# print(icdCodes)
# return thirdLevelList

def get_icd_codes(icdCode, dataSet):
    icdCodeList = []

    for i in range(len(dataSet)):
        # print(dataSet)
        if str(dataSet[i]).startswith(icdCode):
            icdCodeList.append(dataSet[i])

    # print (icdCodeList)
    return icdCodeList


def get_icd_names(icdCode, dataSet):
    icdNameList = []
    dataSetCodes = dataSet['icdcode']

    for i in range(len(dataSet)):
        # print(dataSet)
        if str(dataSetCodes[i]).startswith(icdCode):
            icdNameList.append(dataSet[i])

    print(dataSetCodes)
    print(icdNameList)
    return icdNameList


add_groundlevel()
