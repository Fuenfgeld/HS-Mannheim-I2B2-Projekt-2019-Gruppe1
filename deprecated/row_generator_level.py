# # import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input
#
# from deprecated import db_queries as db
#
# # import plotly.graph_objs as go
#
# icdSecondLevelQuery = db.get_icd_level_query_df(2)
# secondLevelNames = icdSecondLevelQuery['name']
# secondLevelICD = icdSecondLevelQuery['icdcode']
# secondLevelIDList = []
#
# icdThirdLevelQuery = db.get_icd_level_query_df(3)
# thirdLevelNames = icdThirdLevelQuery['name']
# thirdLevelICD = icdThirdLevelQuery['icdcode']
# thirdLevelIDList = []
#
# icdFourthLevelQuery = db.get_icd_level_query_df(4)
# fourthLevelNames = icdThirdLevelQuery['name']
# fourthLevelICD = icdThirdLevelQuery['icdcode']
#
# inputList = []
#
# def add_levels_icd():
#     add_groundlevel()
#
#
# def add_groundlevel():
#     groundLeveldf = db.get_icd_level_query_df(1)
#     listGroundLevelDiv = []
#     icdClasses = groundLeveldf['name']
#     icdCodes = groundLeveldf['icdcode']
#     # print(groundLeveldf['name'])
#     print(inputList)
#
#
#
#
#     for i in range(len(icdClasses)):
#         listGroundLevelDiv.append(html.Div([
#
#             html.Span(f'{icdClasses[i]}', className='caret'),
#             html.Ul(add_second_level(icdCodes[i]), className='nested')],
#         ))
#     # print(icdCodes)
#     # print(listGroundLevelDiv)
#     return listGroundLevelDiv
#
#
# # adds the second level to the structure
# def add_second_level(icdMetaCode):
#     listSecondLevelDiv = []
#
#     global secondLevelIDList
#     global inputList
#
#     for i in range(70):
#
#         if str(secondLevelICD[i]).startswith(icdMetaCode[0:7]) or \
#                 secondLevelICD[i][10] in icdMetaCode[10] and secondLevelICD[i][10] != secondLevelICD[i][6]:
#             # print(secondLevelICD[i])
#             # print(icdMetaCode)
#             listSecondLevelDiv.append(html.Div([
#                 html.Span(f'{secondLevelNames[i]}', id=f'{secondLevelICD[i]} {secondLevelNames[i][0]}',
#                           className='caret'),
#                 # html.Ul(add_third_level(secondLevelICD[i]), className='nested')],
#             ]))
#             secondLevelIDList.append(Input(f'{secondLevelICD[i]} {secondLevelNames[i][0]}', 'id'))
#             inputList.append(f'{secondLevelICD[i]} {secondLevelNames[i][0]}')
#             # print(f'{secondLevelICD[i]} {secondLevelNames[i][0]}')
#             # print(secondLevelICD[i][10])
#
#
#     return listSecondLevelDiv
#
#
# ###
# def add_third_level(icdMetaCode):
#     listThirdLevelDiv = []
#
#     global thirdLevelIDList
#     for i in range(len(thirdLevelICD)):
#
#         if str(thirdLevelICD[i]).startswith(icdMetaCode[0:8]):
#             # print(thirdLevelICD[i])
#             # print(icdMetaCode)
#             listThirdLevelDiv.append(html.Div([
#                 html.Span(f'{thirdLevelNames[i]} ({thirdLevelICD[i][6:10]})', className='caret',
#                           id=f'{thirdLevelICD[i]}'),
#                 # html.Ul(add_fourth_level(icdMetaCode), className='nested')],
#             ]))
#     return listThirdLevelDiv
#
#
# def add_fourth_level(icdMetaCode):
#     listFourthLevelDiv = []
#
#     for i in range(len(fourthLevelICD)):
#
#         if str(fourthLevelICD[i]).startswith(icdMetaCode[0:8]):
#             # print(thirdLevelICD[i])
#             # print(icdMetaCode)
#             listFourthLevelDiv.append(html.Div([
#                 html.Span(f'{fourthLevelNames[i]} ({fourthLevelICD[i][7:10]})', className='caret'),
#                 html.Ul('hehe boah', className='nested')],
#             ))
#
#     return listFourthLevelDiv
#
#
# # ANYTREE PYTHON
#
# # you'll get this, the matter of efficiency, make use of the access to the data frames
# # on each separate level, you know what to do
#
#
# # method that returns a list of the ICD Codes that start with the given ICD code in the parameter
# def get_icd_codes(icdCode, dataSet):
#     icdCodeList = []
#
#     for i in range(len(dataSet)):
#         # print(dataSet)
#         if str(dataSet[i]).startswith(icdCode):
#             icdCodeList.append(dataSet[i])
#
#     # print (icdCodeList)
#     return icdCodeList
#
#
#
#
# add_groundlevel()