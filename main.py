# dash library
import dash
# import dash_core_components as dcc
import dash_html_components as html
# from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
# import plotly.graph_objs as go

__navbar = dbc.NavbarSimple(
    children=[],
    brand="Engineering Budget Monitoring System",
    brand_href="#",
    sticky="top",
    # color="primary",
    # dark=True
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MATERIA])

app.layout = html.Div([__navbar])

if __name__ == "__main__":
    app.run_server()
    # app.run_server(debug=True)
