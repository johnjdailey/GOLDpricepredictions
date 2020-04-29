import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## PAGE NAME


            """
        ),
    ],
    md=4,
)

column2 = dbc.Col([html.Img(src='assets/lambda.png', className='img-fluid')])

layout = dbc.Row([column1, column2])