from anytree import Node, RenderTree

import DB_queries as db


def add_first_level(metaPath):
    rootNode = Node(f'{metaPath}')
    levelQuery = db.Queries()  # Object of Queries
    wholeLevelList = levelQuery.get_level(1)  # Database query put into a data frame
    levelCopy = wholeLevelList.copy(deep=True)  # as the original list is changed
    # an untouched deep copy is needed (rename variable)
    levelFullNames = wholeLevelList['fullname']  # full paths of the first level (former c_fullpath)
    copyFullNames = levelCopy['fullname']  # same reason as above
    # print(wholeLevelList)
    levelNames = wholeLevelList['name']  # 'plain' names that are used as the content of the nodes
    # (e.g. Certain infectious and parasitic diseases (a00-b99))

    for i in range(len(wholeLevelList)):  # loop over every row of the first level
        if str(wholeLevelList['path'][i]) == '\\Diagnoses\\':  # if the path starts with \Diagnoses\
            levelFullNames[i] = Node(f'{levelNames[i]}', parent=rootNode)  # create a new node with name as content,
            # rootNode as parent and fullname (extended path e.g. \Diagnoses\(A00-B99) Cert~ugmm\ ) as name that can be
            # referenced

    add_next_level(2, levelFullNames, copyFullNames)  # recursive method that adds next levels
    print(RenderTree(rootNode))  # show the tree using the tree renderer


def add_next_level(level, metaNodeList, metaPathList):
    print('adding level: ', level)  # used for clarification which level is added

    levelQuery = db.Queries()  # new Object is created
    wholeLevelList = levelQuery.get_level(level)  # Database query put into a data frame
    levelCopy = wholeLevelList.copy(deep=True)  # as the original list is changed
    # an untouched deep copy is needed (rename variable)
    levelFullNames = wholeLevelList['fullname']  # full paths of the first level (former c_fullpath)
    copyFullNames = levelCopy['fullname']
    levelNames = wholeLevelList['name']
    levelPaths = wholeLevelList['path']
    metaListIndex = 0  # index of the list of the parent nodes (rename variable)
    wholeLvelIndex = 0  # index of the whole list of the level (rename variable)

    # print('Full name: ', levelFullNames[0])
    # print('Path: ', levelPaths[0])
    # print('meta path: ', metaPathList[0])
    # print('Name: ', levelNames[0])
    # print('Parent: ', metaNodeList[0])

    while wholeLvelIndex <= len(wholeLevelList) and metaListIndex < len(metaNodeList):  # while both indices
        # are in range

        if levelPaths[wholeLvelIndex] == metaPathList[metaListIndex]:  # if path of child aligns with the fullpath of
            # the (parent) node in the list, this node in the list is the parent of the child and gets appended to it
            # print('True')
            levelFullNames[wholeLvelIndex] = Node(f'{levelNames[wholeLvelIndex]}', parent=metaNodeList[metaListIndex])
            wholeLvelIndex += 1
        else:  # if paths do not align, the next parent node is looked on
            # print('Next one')
            metaListIndex += 1

    if level <= 4:  # there is a limit to the levels, without this statement this would create an endless loop
        add_next_level(level + 1, levelFullNames, copyFullNames)


add_first_level('Diagnosis')

# class SearchLevel:
#     query = db.Queries()
#     print(query.whole_icd)
