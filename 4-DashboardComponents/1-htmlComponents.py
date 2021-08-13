import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

app = dash.Dash()
# if we have multiple components,then we need a list, else we can just directly write it!
app.layout = html.Div([
    'This is the Outermost div!',
    html.Div('This is an inner div!',
             style={'color': 'red', 'border': '3px red solid'}),
    html.Div('This is another inner div',
             style={'color': 'blue', 'border': '3px blue solid'})
],
    style={'color': 'green', 'border': '3px green solid'})

if __name__ == "__main__":
    app.run_server()
