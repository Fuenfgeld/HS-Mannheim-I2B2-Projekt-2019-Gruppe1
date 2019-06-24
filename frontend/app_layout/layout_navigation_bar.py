import dash_core_components as dcc
import dash_html_components as html
import visdcc


class layoutNavigationBar:

    layout_search_bar = html.Div([
        dcc.Input(id='input-box', placeholder='Suche/Eingabe', type='text', className='DivEingabe'),
        html.Button(id='add-button', children='Add', n_clicks=0, className='DivAddButton'),
        html.Button('Clear', id='clear'),
        visdcc.Run_js(id='javascript', run="""
            var target = document.getElementById('input-box')
            document.getElementById('add-button').addEventListener('click', function(evt) {
                setProps({
                    'event': {'x':target.className,
                              'y':evt.y }
                })
                //alert($(event.target).prop('class'))
                //target.className=target.value
            });        
                """),

    ], className="DivEingabeUndAdden")

    layout_navigation = html.Div([
        html.Div(id='clicked-button', children='del:0 add:0 co1:0 co2:0 last:nan', style={'display': 'none'}),
        html.Div(
            [html.Div(className='container'),
             html.Div(id='jstree-tree'),
             html.Div(id='jstree-result', hidden=True)]
        )

    ], className="DivBaum")