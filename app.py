from dash import Dash, Input, Output, State, callback, dash_table, dcc, html
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

first_page_layout = dbc.Container([
    dbc.Label('Select a Stock'),  # Update label
    dbc.Input(id='underlying-input', placeholder='Enter underlying symbol', type='text',value="RIVN"),
    dbc.Button('Load Options', id='load-options-button', n_clicks=1, color='primary'),
    dash_table.DataTable(id='tbl'),
    dbc.Alert(id='tbl_out'),
])


# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
