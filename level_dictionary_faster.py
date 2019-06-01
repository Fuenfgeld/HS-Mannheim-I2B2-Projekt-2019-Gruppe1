import json

from anytree import Node
# from collections import OrderedDict
from anytree.exporter import JsonExporter, DictExporter

import DB_queries as db

json_exporter = JsonExporter(indent=2)
dict_exporter = DictExporter()


class levels():
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

        levels.add_next_level(2, levelFullNames, copyFullNames)  # recursive method that adds next levels
        # pprint(dict_exporter.export(rootNode))
        # pprint(json_exporter.export(rootNode))
        # print('Length of dictionary: ', len(dict_exporter.export(rootNode)))
        print('Length of dictionary: ', len(json_exporter.export(rootNode)))
        return json_exporter.export(rootNode)
        # print(RenderTree(rootNode))  # show the tree using the tree renderer

    def add_next_level(level, parentNodeList, parentPathList):
        print('adding level: ', level)  # used for clarification which level is added

        levelQuery = db.Queries()  # new Object is created
        wholeLevelList = levelQuery.get_level(level)  # Database query put into a data frame
        levelFullNames = wholeLevelList['fullname']  # full paths of the first level (former c_fullpath)
        levelCopy = wholeLevelList.copy(deep=True)  # as the original list is changed
        # an untouched deep copy is needed (rename variable)
        copyFullNames = levelCopy['fullname']
        levelNames = wholeLevelList['name']
        levelPaths = wholeLevelList['path']
        metaListIndex = 0  # index of the list of the parent nodes (rename variable)
        wholeLvelIndex = 0  # index of the whole list of the level (rename variable)

        while wholeLvelIndex < len(wholeLevelList) and metaListIndex <= len(parentNodeList):  # while both indices
            # are in range

            if levelPaths[wholeLvelIndex] == parentPathList[metaListIndex] or metaListIndex == len(parentNodeList):
                # if path of child aligns with the fullpath of
                # the (parent) node in the list, this node in the list is the parent of the child and gets appended to it
                # print('True')
                levelFullNames[wholeLvelIndex] = Node(f'{levelNames[wholeLvelIndex]}',
                                                      parent=parentNodeList[metaListIndex])
                wholeLvelIndex += 1
            else:  # if paths do not align, the next parent node is looked on
                # print('Next one')
                metaListIndex += 1

        if level <= 1:  # there is a limit to the levels, without this statement this would create an endless loop
            print('Length of the whole level list: ', len(wholeLevelList))
            print('Index of the whole list: ', wholeLvelIndex)
            print('Length of parent list: ', len(parentNodeList))
            print('Parent list index: ', metaListIndex)
            print('')
            levels.add_next_level(level + 1, levelFullNames, copyFullNames)


# print(levels.add_first_level('Diagnosis'))
# dict_string = str(levels.add_first_level('Diagnosis'))
# dict_string = dict_string.replace('name', 'text')
#
# updated_dict_string = dict_string.translate({ord(i): None for i in '[]'})
#
# print(f'{updated_dict_string}')

# python_json_dic = json.loads(levels.add_first_level('Diagnosis'))
#
# print(python_json_dic)
# print(len(python_json_dic))
#
# print(updated_dict)
# print(len(updated_dict))


with open('icd_tree.json', 'w') as write_file:
    json.dump(levels.add_first_level('Diagnosis'), write_file)


# class SearchLevel:
#     query = db.Queries()
#     print(query.whole_icd)
