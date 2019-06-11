# In[]:
# Import required libraries
import dash
import dash_html_components as html
from dash.dependencies import Input, Output


# Define the app
app = dash.Dash('')
server = app.server
app.config.suppress_callback_exceptions = False
app.scripts.config.serve_locally = True


class DashCallbackVariables:
    """Class to store information useful to callbacks"""

    def __init__(self):
        self.n_clicks = {1: 0, 2: 0}

    def update_n_clicks(self, nclicks, bt_num):
        self.n_clicks[bt_num] = nclicks


callbacks_vars = DashCallbackVariables()

root_layout = html.Div(
    id='main_page',
    children=[
        html.Div(
                id='btn_name',
                children="No button was clicked"
        ),
        html.Div(
            [
                html.Button(
                    'Button1',
                    id='btn_1',
                    type='submit',
                    n_clicks=0
                )
            ]
        )
    ], className="ButtDiv"
)

app.layout = root_layout