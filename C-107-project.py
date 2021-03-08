import plotly_express as px
import pandas as pd

df = pd.read_csv("C-109_project.csv")
fig = px.scatter(df, x="student_id", y="level", color="attempt")
fig.show()
