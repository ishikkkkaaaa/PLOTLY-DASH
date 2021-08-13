#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
# Launch the application:
app = dash.Dash()

# Create a DataFrame from the .csv file:
df = pd.read_csv("../Data/OldFaithful.csv")
# print(df)

# Create a Dash layout that contains a Graph component:
app.layout = html.Div(
    [dcc.Graph(id="old_faithful",
               figure={
                   'data': [go.Scatter(
                       x=df['X'],
                       y=df['Y'],
                       mode='markers',
                       marker={
                           'size': 12,
                           'color': 'rgb(200,204,53)',
                           # 'symbol': 'pentagon',
                           'line': {'width': 2}
                       }
                   )],
                   "layout": go.Layout(
                       title="Old Faithful Erruptions",
                       xaxis={'title': "Duration"},
                       yaxis={'title': "Interval"}
                   )
               })]
)

# Add the server clause:
if __name__ == "__main__":
    app.run_server()
