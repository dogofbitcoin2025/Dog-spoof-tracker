
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="DOG Spoof Tracker", layout="wide")
st.title("🐶 $DOG Spoof Tracker Dashboard")
st.markdown("Live detection of spoofing activity on Gate.io for $DOG/USDT")

# Simulated spoof events
np.random.seed(42)
num_events = 10
base_time = datetime.now() - timedelta(hours=1)
events = []

for i in range(num_events):
    event_time = base_time + timedelta(minutes=i * 6)
    spoof_price = round(np.random.uniform(0.0041, 0.0052), 4)
    wall_size = np.random.randint(10_000_000, 20_000_000)
    duration = np.random.randint(6, 28)
    events.append([event_time.strftime('%Y-%m-%d %H:%M:%S'), spoof_price, wall_size, duration])

df = pd.DataFrame(events, columns=["Timestamp", "Spoof Wall Price ($)", "Wall Size (DOG)", "Visible Duration (sec)"])

st.subheader("📋 Detected Spoof Events")
st.dataframe(df, use_container_width=True)

st.subheader("📊 Spoof Wall Heatmap")
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(df["Spoof Wall Price ($)"], df["Wall Size (DOG)"], color="orange", width=0.0001)
ax.set_xlabel("Price ($)")
ax.set_ylabel("Wall Size (DOG)")
ax.set_title("Spoof Wall Size by Price")
st.pyplot(fig)
