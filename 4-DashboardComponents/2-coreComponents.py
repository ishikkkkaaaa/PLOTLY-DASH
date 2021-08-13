import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(options=[
        {
            'label': 'New York City',
            'value': 'NYC'
        },
        {
            'label': 'San Fransico',
            'value': 'SF'
        }
    ],
        value='SF'  # defualt value
    ),

    html.Label('Slider'),
    dcc.Slider(min=-10, max=10, step=0.5, value=0,
               marks={i: i for i in range(-10, 10)}),
    html.P(html.Label('Some radio button')),
    dcc.RadioItems(options=[
        {
            'label': 'New York City',
            'value': 'NYC'
        },
        {
            'label': 'San Fransico',
            'value': 'SF'
        }
    ],
        value='SF')
])

if __name__ == '__main__':
    app.run_server()
