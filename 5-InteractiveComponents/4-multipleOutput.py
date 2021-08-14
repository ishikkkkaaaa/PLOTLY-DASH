
#######
# This uses a small wheels.csv dataset
# to demonstrate multiple outputs.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_components.Iframe import Iframe
import pandas as pd
# to work with images
import base64

app = dash.Dash()


def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    # reads the  image file using open(image_File, 'rb') and then which is encoded with b6
    return 'data:image/png;base64,{}'.format(encoded.decode())


df = pd.read_csv('../data/wheels.csv')

app.layout = html.Div([
    dcc.RadioItems(id='wheels',
                   options=[{'label': i, "value": i}
                            for i in df['wheels'].unique()],
                   value=1
                   ),

    html.Div(id='wheels-output'),
    html.Hr(),
    dcc.RadioItems(id='colors',
                   options=[{'label': i, "value": i}
                            for i in df['color'].unique()],
                   # , style={'fontFamily': 'Sans-Serif', 'fontSize': 130}
                   value='blue'
                   ),
    html.Div(id='colors-output'),
    html.Img(id='display-image', src='children', height=300)
], style={'fontFamily': 'Sans-Serif', 'fontSize': 18})


@app.callback(
    Output('wheels-output', 'children'),
    [Input('wheels', 'value')])
def callback_a(wheels_value):
    return "you chose {}".format(wheels_value)


@app.callback(
    Output('colors-output', 'children'),
    [Input('colors', 'value')])
def callback_a(colors_value):
    return "you chose {}".format(colors_value)


@app.callback(
    Output('display-image', 'src'),
    [Input('wheels', 'value'),
     Input('colors', 'value')])
def callback_image(wheel, color):
    path = '../data/images/'
    return encode_image(path+df[(df['wheels'] == wheel) &
                                (df['color'] == color)]['image'].values[0])


if __name__ == '__main__':
    app.run_server()
