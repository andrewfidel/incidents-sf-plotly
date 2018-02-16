import plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd

df = pd.read_csv(r'reducedDays.csv')
x = [x for x in df['day']]
y = [y for y in df['value']]


# trace1 = go.Bar(
#     x=x,
#     y=y
# )

trace1 = go.Bar(
    x=[x for x in df['day']],
    y=[y for y in df['value']],
    text=[y for y in df['value']],
    textposition='auto',
    marker=dict(
        color='rgb(174,37,22)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.0,
        )
    ),
    opacity=0.5
)

layout = go.Layout(
    title='San Francisco Police Incidents',
    yaxis = dict(
        title='values'
    ),
    xaxis = dict(
        title='day of week'
    )
)

fig = go.Figure(data=[trace1], layout=layout)
py.offline.plot(fig, filename='incidents-sf.html', auto_open=False)