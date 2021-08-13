# Importing all the req libraries
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('../data/mpg.csv')

app = dash.Dash()

features = df.columns

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id='xaxis',
                        options=[{'label': i, 'value': i} for i in features],
                        value='displacement')
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(id='yaxis',
                        options=[{'label': i, 'value': i} for i in features],
                        value='mpg')
    ], style={'width': '48%', 'display': 'inline-block'}),
    dcc.Graph(id="feature-graphic")
], style={'padding': 10, 'border': 'thin lightgrey solid'})


@app.callback(Output('feature-graphic', 'figure'),
              [Input('xaxis', 'value'),
               Input('yaxis', 'value')])
def update_graph(xaxis_name, yaxis_name):
    return {
        'data': [go.Scatter(
            x=df[xaxis_name],
            y=df[yaxis_name],
            text=df['name'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            })], 'layout': go.Layout(
            title="Dashboard Layout",
            xaxis={'title': xaxis_name},
            yaxis={'title': yaxis_name},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest')
    }


if __name__ == '__main__':
    app.run_server()
