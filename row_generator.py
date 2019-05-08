import dash_html_components as html

import DB_Test as db


# print(db.df.keys())
# print(db.df.keys()[1])

# listOfKeys = list(db.df)

# print(list(db.df))


def add_distinct_values(df):
    uniqueItems = df.unique()
    listUnique = []
    for i in range(len(uniqueItems)):
        listUnique.append(html.Div('' + str(uniqueItems[i]) + ''))
    print(listUnique)
    return listUnique


def add_list_items(df):
    listOfKeys = list(df)
    listOfDivElements = []
    for i in range(len(listOfKeys)):
        if len(df[listOfKeys[i]].unique()) > 1:
            listOfDivElements.append(html.Div([
                html.Span('' + listOfKeys[i] + '', className='caret'),
                html.Ul(add_distinct_values(df[listOfKeys[i]]), className='nested'),
            ],
            ),
            )
        else:
            listOfDivElements.append(html.Div(['' + listOfKeys[i] + '',
                                               ], className='empty')
                                     )
    return listOfDivElements


def add_one_item(df):
    return html.Div('' + list(df)[0] + '')
