# Allows the caprison of 2 variables for a set of data points

import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',
    marker=dict(
        size=12,
        color='rgb(51,204,153)',
        symbol='pentagon',
        line={'width': 2}
    ))]
layout = go.Layout(
    title='Random Data Scatterplot',  # Graph title
    xaxis=dict(title='Some random x-values'),  # x-axis label
    yaxis=dict(title='Some random y-values'),  # y-axis label
    hovermode='closest'  # handles multiple points landing on the same vertical
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter3.html')
