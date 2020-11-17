import pandas as pnd
import plotly.express as px
import plotly.graph_objects as gp 
import csv
import plotly.figure_factory as pf

df = pnd.read_csv("103data.csv")
fig = px.scatter(df, x="date", y = "cases", color = "country")
fig.show()
