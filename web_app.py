import streamlit as st
import numpy as np
import pandas as pd
from stock_predictor import StockPricePredictionModel
import matplotlib.pyplot as plt

st.title("📈 Stock Price Prediction AI")

st.markdown("""
*Powered by LSTM Neural Networks*

**Instructions:**
- Upload a CSV (with a `Close` or `Price` column), or
- Enter 5 years of historical prices (comma-separated or one per line)
- Click **Train Model**
- Adjust days and click **Predict** to see the future!
""")

# Data input section
st.header("1. Provide Historical Data")
prices = []

input_method = st.radio("How would you like to provide data?", ["Upload CSV", "Manual Entry"], horizontal=True)

if input_method == "Upload CSV":
    uploaded_file = st.file_uploader("Upload your historical stock prices CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        candidates = [col for col in df.columns if "price" in col.lower() or "close" in col.lower()]
        col = st.selectbox("Select the price/close column", candidates if candidates else df.columns)
        prices = df[col].dropna().tolist()
        st.write(f"Loaded {len(prices)} data points.")
else:
    manual_input = st.text_area("Paste comma-separated or newline historical prices", "", height=150)
    if manual_input.strip():
        try:
            # Split by commas and/or newlines
            raw = manual_input.replace("\n", ",").split(",")
            prices = [float(x) for x in raw if x.strip()]
            st.write(f"Loaded {len(prices)} data points.")
        except Exception:
            st.warning("Ensure all entries are valid numbers (comma/newline separated).")

# Only proceed if there are enough data points
if prices and len(prices) >= 100:
    st.header("2. Data Statistics")
    model = StockPricePredictionModel()
    stats = model.get_price_statistics(prices)
    st.write(stats)
    fig, ax = plt.subplots()
    ax.plot(prices, label="Historical Prices")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    ax.legend()
    st.pyplot(fig)

    st.header("3. Train the AI Model")
    epochs = st.slider("Training Epochs", 10, 200, 50)
    if st.button("Train Model"):
        with st.spinner("Training..."):
            try:
                metrics = model.train(prices, epochs=epochs)
                st.success("Training complete!")
                st.write(metrics)
            except Exception as e:
                st.error(f"Training failed: {e}")
        st.session_state["model"] = model
        st.session_state["prices"] = prices
    else:
        if "model" in st.session_state and "prices" in st.session_state:
            model = st.session_state["model"]
            prices = st.session_state["prices"]

    st.header("4. Predict Future Prices")
    days_ahead = st.slider("Days to Predict Ahead", 1, 365, 30)
    if st.button("Predict Future Prices"):
        if "model" in st.session_state and "prices" in st.session_state:
            model = st.session_state["model"]
            prices = st.session_state["prices"]
            future = model.predict_future_prices(prices, days_ahead=days_ahead)
            st.line_chart(pd.Series(list(prices) + list(future), name="Forecast"))
            pred_df = pd.DataFrame({
                "Day Ahead": np.arange(1, days_ahead+1),
                "Predicted Price": future
            })
            st.write(pred_df)
        else:
            st.warning("You must train the model first before prediction.")
else:
    st.info("Add at least 100 data points to continue.")

st.markdown("---\n*This AI model is for educational/research use only.*")
