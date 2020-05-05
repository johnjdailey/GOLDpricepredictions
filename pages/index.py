import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Value Proposition

            This app can benefit users by predicting GOLD stock prices.

            """
        ),
        dcc.Link(dbc.Button('GOLD Predictions', color='primary'), href='/predictions')
    ],
    md=4,
)

#gapminder = px.data.gapminder()
#fig = px.line(gapminder.query("year==2007"), x="Date", y="Price", title = "GOLD Prices 1985 - 2020")

column2 = dbc.Col(
    [
        #dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])