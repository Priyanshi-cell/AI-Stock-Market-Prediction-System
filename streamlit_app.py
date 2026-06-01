import streamlit as st
import pandas as pd
import plotly.express as px

from src.predict import predict_next_price
from src.recommendation import generate_recommendation
from src.forecast import forecast_next_7_days

st.set_page_config(
    page_title="AI Stock Predictor",
    page_icon="📈",
    layout="wide"
)

st.title(
    "📈 AI Powered Stock Market Prediction System"
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

predicted_price = predict_next_price(df)

current_price = df.iloc[-1]["Close"]

recommendation = generate_recommendation(
    predicted_price,
    current_price
)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Current Price",
        f"${current_price:.2f}"
    )

with col2:

    st.metric(
        "Predicted Price",
        f"${predicted_price:.2f}"
    )

with col3:

    st.metric(
        "Recommendation",
        recommendation
    )

price_change = (
    (predicted_price - current_price)
    / current_price
) * 100

if recommendation == "BUY":

    st.success(
        f"🤖 AI Insight: Expected upside of {price_change:.2f}% based on model prediction."
    )

elif recommendation == "SELL":

    st.error(
        f"🤖 AI Insight: Expected downside of {abs(price_change):.2f}% based on model prediction."
    )

else:

    st.info(
        f"🤖 AI Insight: Predicted movement is only {abs(price_change):.2f}% suggesting a neutral outlook."
    )

st.divider()

st.subheader(
    "📅 7-Day Forecast"
)

forecast_df = forecast_next_7_days(df)

st.dataframe(
    forecast_df,
    use_container_width=True
)

forecast_chart = px.line(
    forecast_df,
    x="Day",
    y="Predicted Price",
    markers=True
)

st.plotly_chart(
    forecast_chart,
    use_container_width=True
)

st.divider()

st.subheader(
    "Model Performance"
)

results = pd.read_csv(
    "data/results.csv"
)

st.dataframe(
    results,
    use_container_width=True
)

st.subheader(
    "Model Comparison Charts"
)

fig_r2 = px.bar(
    results,
    x="Model",
    y="R2",
    title="R² Score Comparison"
)

st.plotly_chart(
    fig_r2,
    use_container_width=True
)

fig_rmse = px.bar(
    results,
    x="Model",
    y="RMSE",
    title="RMSE Comparison"
)

st.plotly_chart(
    fig_rmse,
    use_container_width=True
)

best_model = (
    results.sort_values(
        by="R2",
        ascending=False
    )
    .iloc[0]["Model"]
)

st.success(
    f"🏆 Best Model: {best_model}"
)