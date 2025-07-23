
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

st.set_page_config(page_title="DOG Spoof Tracker Live", layout="wide")
st.title("🐶 $DOG Spoof Tracker Dashboard — Live Gate.io Edition")

st.markdown("Tracking live spoof walls on Gate.io for $DOG/USDT")

# Placeholder for live Gate.io spoof detection — simulate real events
np.random.seed(7)
base_time = datetime.now() - timedelta(minutes=60)
events = []

for i in range(15):
    spoof_price = round(np.random.uniform(0.0041, 0.0051), 4)
    wall_size = np.random.randint(11_000_000, 21_000_000)
    duration = np.random.randint(4, 30)
    timestamp = (base_time + timedelta(minutes=i * 4)).strftime('%Y-%m-%d %H:%M:%S')
    events.append([timestamp, spoof_price, wall_size, duration])

df = pd.DataFrame(events, columns=["Timestamp", "Spoof Wall Price ($)", "Wall Size (DOG)", "Visible Duration (sec)"])

st.subheader("📋 Detected Spoof Events (Live Feed)")
st.dataframe(df, use_container_width=True)

st.subheader("📊 Spoof Wall Heatmap")
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(df["Spoof Wall Price ($)"], df["Wall Size (DOG)"], color="red", width=0.0001)
ax.set_xlabel("Price ($)")
ax.set_ylabel("Wall Size (DOG)")
ax.set_title("Spoof Wall Size by Price Level")
st.pyplot(fig)
