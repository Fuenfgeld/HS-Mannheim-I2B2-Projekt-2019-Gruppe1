from anytree import Node, RenderTree

import DB_queries as db


# something = Node('Something', parent=diagnosis)
# somethingElse = Node('Something else', parent=diagnosis)
# anythingElse = Node('anything else')
# anything = Node('anything', parent=diagnosis)


def add_first_level(metaPath):
    rootNode = Node(f'{metaPath}')
    levelQuery = db.Queries()
    levelList = levelQuery.get_level(1)
    levelCopy = levelList.copy(deep=True)
    levelFullNames = levelList['fullname']
    copyFullNames = levelCopy['fullname']
    # print(levelList)
    levelNames = levelList['name']

    for i in range(len(levelList)):
        if str(levelList['path'][i]) == '\\Diagnoses\\':
            levelFullNames[i] = Node(f'{levelNames[i]}', parent=rootNode)
            # print(levelFullNames[i])
            # print(copyFullNames[i])
            add_next_level(copyFullNames[i], levelFullNames[i], 2)

    print(RenderTree(rootNode))


def add_next_level(metaPath, metaNode, level):
    print('adding level: ', level)
    levelQuery = db.Queries()
    levelList = levelQuery.get_level(level)
    levelCopy = levelList.copy(deep=True)
    levelFullNames = levelList['fullname']
    copyFullNames = levelCopy['fullname']
    levelNames = levelList['name']

    if level <= 2:
        for i in range(len(levelList)):
            if str(levelList['path'][i]) == f'{metaPath}':
                levelFullNames[i] = Node(f'{levelNames[i]}', parent=metaNode)
                # print(levelFullNames[i])
                # print(copyFullNames[i])
                add_next_level(copyFullNames[i], levelFullNames[i], level + 1)


add_first_level('Diagnosis')

# class SearchLevel:
#     query = db.Queries()
#     print(query.whole_icd)
