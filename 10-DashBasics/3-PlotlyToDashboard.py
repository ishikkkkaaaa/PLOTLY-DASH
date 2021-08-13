import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

# creating DATA
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)
app.layout = html.Div([
    dcc.Graph(
        id='scatter1',
        figure={
            'data': [
                go.Scatter(
                    x=random_x,
                    y=random_y,
                    mode='markers',
                    marker={
                        'size': 12,
                        'color': 'rgb(200,204,53)',
                        'symbol': 'pentagon',
                        'line': {'width': 2}
                    }
                )
            ],
            'layout': go.Layout(
                title='Firs Scatterplot',
                xaxis={'title': 'Some random x-values'},
                yaxis={'title': 'Some random y-values'},
                # hovermode='closest'
            )
        }
    ),
    dcc.Graph(
        id='scatter2',
        figure={
            'data': [
                go.Scatter(
                    x=random_x,
                    y=random_y,
                    mode='markers',
                    marker={
                        'size': 12,
                        'color': 'rgb(51,204,153)',
                        'symbol': 'pentagon',
                        'line': {'width': 2}
                    }
                )
            ],
            'layout': go.Layout(
                title='Second Data Scatterplot',
                xaxis={'title': 'Some random x-values'},
                yaxis={'title': 'Some random y-values'},
                # hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()
