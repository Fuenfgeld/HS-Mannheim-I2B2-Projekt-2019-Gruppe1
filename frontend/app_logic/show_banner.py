import dash
import dash_core_components as dcc
import dash_html_components as html

class ShowBanner():
    app = dash.Dash(__name__)

    layoutBanner = app.layout
    layoutBanner = html.Div([
            html.H5("greenCET"),
            html.Img(src="/assets/LOGO.png")
    ], className="bannerDiv")
