from audioop import avg
import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv("data.csv")
avg=df["Avg Rating"].to_list()

fig=ff.create_distplot([avg],["Mobile Rating"],show_hist=False)
fig.show()