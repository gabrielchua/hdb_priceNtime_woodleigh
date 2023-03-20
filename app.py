import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("output.csv")

fig = px.scatter(df,
                 x="ppsqm",
                 y="travel_time",
                 color="town",
                 hover_name="address", 
                 labels={
                     "travel_time": "Travel Time To Woodleigh (Minutes)",
                     "ppsqm": "Median Price Per Square Metre, 2022-2023 ($)",
                     "town": "Town",
                 })

st.plotly_chart(fig,
	theme=None,
	use_container_width=False)
