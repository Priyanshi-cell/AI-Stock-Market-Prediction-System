import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="EDA",
    layout="wide"
)

st.title(
    "📊 Exploratory Data Analysis"
)

stock = st.sidebar.selectbox(
    "Select Stock",
    [
        "AAPL",
        "MSFT",
        "GOOGL",
        "NVDA",
        "TSLA"
    ]
)

df = pd.read_csv(
    f"data/processed/{stock}_features.csv"
)

st.subheader(
    "Closing Price Distribution"
)

fig1 = px.histogram(
    df,
    x="Close",
    nbins=50
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.subheader(
    "Volume Distribution"
)

fig2 = px.histogram(
    df,
    x="Volume",
    nbins=50
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.subheader(
    "Correlation Matrix"
)

corr = df[
    [
        "Close",
        "MA10",
        "MA50",
        "RSI",
        "MACD",
        "Volume"
    ]
].corr()

fig3 = px.imshow(
    corr,
    text_auto=True,
    title="Feature Correlation"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)