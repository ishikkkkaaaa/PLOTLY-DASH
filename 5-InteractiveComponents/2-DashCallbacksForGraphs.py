#Importing all the req libraries
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# https://dash.plot.ly/dash-core-components/dropdown

#read data from csv
df = pd.read_csv('../data/gapminderDataFiveYear.csv')

#creating application
app = dash.Dash()

#creating year options for dropdown
year_options = []
for year in df['year'].unique():
    year_options.append({'label': str(year), 'value': year})

#app layout is just graph and dropdown
app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='year-picker',
                 options=year_options,
                 value=df['year'].min()
                 )
]
)

# connects the input from the dropdown to output of the graph


@app.callback(Output('graph', 'figure'),
              [Input('year-picker', 'value')])

# this creates figure for the dropdown of the actual figure!
def update_figure(selected_year):
    # data only for selected year from dropdown
    filtered_df = df[df['year'] == selected_year]

    traces = []
    #this is the main thing which is updating the figure
    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent']
                                      == continent_name]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            text=df_by_continent['country'],
            mode='markers',
            opacity=0.7,
            marker={'size': 15},
            name=continent_name
        ))
    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
            yaxis={'title': 'Life Expectancy'},
            hovermode='closest'
        )
    }
    # legend={'x': 0, 'y': 1})}


if __name__ == '__main__':
    app.run_server()
