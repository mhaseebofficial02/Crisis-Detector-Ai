import streamlit as st
import pandas as pd
from crisis_dataset import crisis_data

st.set_page_config(page_title="CrisisDetect AI", layout="wide")
st.title("🌍 CrisisDetect AI — Real-Time Event Feed")

df = pd.DataFrame(crisis_data)

with st.sidebar:
st.header("🔍 Filter by Type")
selected_type = st.selectbox("Crisis Type", options=["All"] + sorted(df["type"].unique()))
if selected_type != "All":
df = df[df["type"] == selected_type]

st.metric("Total Events", len(df))
st.dataframe(df, use_container_width=True)
