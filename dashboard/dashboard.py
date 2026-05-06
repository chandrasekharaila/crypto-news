import sys
from pathlib import Path

import pandas as pd
import streamlit as st

from streamlit_autorefresh import st_autorefresh


# -----------------------------------
# FIX PYTHON IMPORT PATH
# -----------------------------------

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)


# -----------------------------------
# IMPORT PIPELINE
# -----------------------------------

from app.pipelines.news_pipeline import run_news_pipeline


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Crypto Event Intelligence",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -----------------------------------
# AUTO REFRESH
# -----------------------------------

st_autorefresh(
    interval=60000,
    key="crypto_refresh"
)


# -----------------------------------
# CACHE DATA
# -----------------------------------

@st.cache_data(ttl=300)
def load_news():
    return run_news_pipeline()


# -----------------------------------
# LOAD DATA
# -----------------------------------

data = load_news()

df = pd.DataFrame(data)


# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}

.main {
    background-color: #0f1117;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #151823;
    border-right: 1px solid #2a2f45;
}

div[data-testid="stMetric"] {
    background-color: #1c1f2b;
    border: 1px solid #2d3345;
    padding: 15px;
    border-radius: 15px;
}

.block-container {
    padding-top: 2rem;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #1a1d29;
    border-radius: 18px;
    border: 1px solid #2a2f45;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("⚡ Filters")


# Event Type Filter
event_types = ["All"]

if "event_type" in df.columns:

    unique_events = (
        df["event_type"]
        .dropna()
        .unique()
        .tolist()
    )

    event_types += sorted(unique_events)


selected_event = st.sidebar.selectbox(
    "Event Type",
    event_types
)


# Importance Slider
min_importance = st.sidebar.slider(
    "Minimum Importance",
    1,
    10,
    1
)


# Search
search = st.sidebar.text_input(
    "Search Events"
)


# -----------------------------------
# FILTERING
# -----------------------------------

if selected_event != "All":

    df = df[
        df["event_type"] == selected_event
    ]


df = df[
    df["importance"] >= min_importance
]


if search:

    df = df[
        df["title"]
        .str.contains(search, case=False)
    ]


# -----------------------------------
# CATEGORIES
# -----------------------------------

high_df = df[
    df["importance"] >= 7
]

medium_df = df[
    (df["importance"] >= 4) &
    (df["importance"] <= 6)
]

low_df = df[
    df["importance"] <= 3
]


# -----------------------------------
# HEADER
# -----------------------------------

st.markdown("""
# 🔥 Crypto Event Intelligence

Institutional-grade crypto market monitoring dashboard.
""")


# -----------------------------------
# METRICS
# -----------------------------------

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    st.metric(
        "Total Events",
        len(df)
    )

with metric2:
    st.metric(
        "High Signal",
        len(high_df)
    )

with metric3:
    st.metric(
        "Medium Signal",
        len(medium_df)
    )

with metric4:
    st.metric(
        "Low Signal",
        len(low_df)
    )


st.markdown("---")


# -----------------------------------
# MAIN LAYOUT
# -----------------------------------

col1, col2, col3 = st.columns(3)


# -----------------------------------
# HIGH SIGNAL
# -----------------------------------

with col1:

    st.subheader("🚨 High Signal")

    for _, row in high_df.iterrows():

        with st.container(border=True):

            st.markdown(
                f"### {row['title']}"
            )

            st.caption(
                f"{row['source']} • Importance {row['importance']}"
            )

            st.markdown(
                f"**Event Type:** `{row['event_type']}`"
            )

            st.link_button(
                "Open Article",
                row["url"],
                use_container_width=True
            )

            st.markdown("<br>", unsafe_allow_html=True)


# -----------------------------------
# MEDIUM SIGNAL
# -----------------------------------

with col2:

    st.subheader("⚠️ Medium Signal")

    for _, row in medium_df.iterrows():

        with st.container(border=True):

            st.markdown(
                f"### {row['title']}"
            )

            st.caption(
                f"{row['source']} • Importance {row['importance']}"
            )

            st.markdown(
                f"**Event Type:** `{row['event_type']}`"
            )

            st.link_button(
                "Open Article",
                row["url"],
                use_container_width=True
            )

            st.markdown("<br>", unsafe_allow_html=True)


# -----------------------------------
# LOW SIGNAL
# -----------------------------------

with col3:

    st.subheader("ℹ️ Low Signal")

    for _, row in low_df.iterrows():

        with st.container(border=True):

            st.markdown(
                f"### {row['title']}"
            )

            st.caption(
                f"{row['source']} • Importance {row['importance']}"
            )

            st.markdown(
                f"**Event Type:** `{row['event_type']}`"
            )

            st.link_button(
                "Open Article",
                row["url"],
                use_container_width=True
            )

            st.markdown("<br>", unsafe_allow_html=True)