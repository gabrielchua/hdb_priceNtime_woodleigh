import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("output.csv")

st.set_page_config(layout="wide")

fig = px.scatter(df,
                 x="ppsqm",
                 y="travel_time",
                 color="town",
                 hover_name="address", 
                 labels={
                     "travel_time": "Travel Time To Woodleigh (Minutes)",
                     "ppsqm": "Median Price Per Square Metre, 2022-2023 ($)",
                     "town": "Town",
                 },
                 width = 1200,
                 height = 800
                 )

st.plotly_chart(fig,
	theme=None,
	use_container_width=False,
	width=1200,
	height=800)