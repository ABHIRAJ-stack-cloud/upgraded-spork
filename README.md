# 📈 Stock Price Prediction AI

A beginner-friendly **Streamlit web application** that uses AI to predict future stock prices based on historical data. Built with Python, this project is perfect for learning about machine learning, data visualization, and web apps!

---

## 🎯 Features

- **Upload CSV or Manual Entry**: Provide stock price data in two ways
  - Upload a CSV file with historical prices
  - Manually enter comma-separated or line-separated prices
- **Data Statistics**: View mean, min, max, and standard deviation of prices
- **Train AI Model**: Train a machine learning model on your historical data
- **Predict Future Prices**: Generate predictions for the next 1-365 days
- **Interactive Charts**: Beautiful visualizations of historical and predicted prices

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository** (or download and extract):
```bash
git clone https://github.com/ABHIRAJ-stack-cloud/upgraded-spork.git
cd upgraded-spork
```

2. **Install required packages**:
```bash
pip install streamlit pandas numpy matplotlib scikit-learn
```

3. **Run the app**:
```bash
streamlit run web_app.py
```

Or if that doesn't work, try:
```bash
python -m streamlit run web_app.py
```

4. **Open in browser**:
The app will automatically open at `http://localhost:8501`

---

## 📖 How to Use

### Step 1: Provide Historical Data
Choose how you want to input data:
- **Upload CSV**: Select a file with a `Price` or `Close` column
- **Manual Entry**: Paste prices (comma-separated or one per line)

**Minimum requirement**: At least 100 data points

### Step 2: View Data Statistics
Once you upload data, you'll see:
- Mean, min, and max prices
- Standard deviation
- A chart showing historical prices

### Step 3: Train the Model
- Adjust the **Training Epochs** slider (10-200)
- Click **"Train Model"** button
- Wait for training to complete ✅

### Step 4: Predict Future Prices
- Set **"Days to Predict Ahead"** (1-365 days)
- Click **"Predict Future Prices"** button
- View the predictions in a chart and table format

---

## 📁 Project Structure

```
upgraded-spork/
├── web_app.py              # Main Streamlit application
├── stock_predictor.py      # AI model and prediction logic
└── README.md               # This file
```

---

## 💡 Sample Data

To test the app quickly, use these 100 sample prices:

```
100, 102, 101, 103, 105, 104, 106, 108, 107, 109, 111, 110, 112, 114, 113, 115, 117, 116, 118, 120, 119, 121, 123, 122, 124, 126, 125, 127, 129, 128, 130, 132, 131, 133, 135, 134, 136, 138, 137, 139, 141, 140, 142, 144, 143, 145, 147, 146, 148, 150, 149, 151, 153, 152, 154, 156, 155, 157, 159, 158, 160, 162, 161, 163, 165, 164, 166, 168, 167, 169, 171, 170, 172, 174, 173, 175, 177, 176, 178, 180, 179, 181, 183, 182, 184, 186, 185, 187, 189, 188, 190, 192, 191, 193, 195, 194, 196, 198, 197, 199
```

---

## ⚠️ Disclaimer

This AI model is for **educational and research purposes only**. 

**Important Notes:**
- Stock price predictions are not guaranteed to be accurate
- Do NOT rely on this model for real investment decisions
- Always consult with financial advisors before making investment choices
- Past performance does not guarantee future results

---

## 🛠️ Technologies Used

- **Streamlit**: Web app framework
- **Python**: Programming language
- **Pandas**: Data manipulation
- **NumPy**: Numerical computations
- **Matplotlib**: Data visualization
- **Scikit-learn**: Machine learning utilities

---

## 📝 Files Explanation

### `web_app.py`
The main Streamlit application that provides the user interface for:
- Data input (CSV or manual)
- Model training controls
- Prediction interface
- Results visualization

### `stock_predictor.py`
Contains the `StockPricePredictionModel` class with methods for:
- `get_price_statistics()`: Calculate stats from historical prices
- `train()`: Train the model on historical data
- `predict_future_prices()`: Generate future price predictions

---

## 🤝 Contributing

Feel free to:
- Fork this repository
- Enhance the AI model with real LSTM neural networks
- Add more features (e.g., multiple stock comparison, technical indicators)
- Fix bugs or improve documentation

---

## 📧 Support

If you have questions or issues:
1. Check the code comments
2. Review the disclaimer section
3. Open an issue on GitHub

---

## 📄 License

This project is open source and available for educational purposes.

---

**Happy predicting! 🚀📈**
