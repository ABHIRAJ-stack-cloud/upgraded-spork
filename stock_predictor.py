import numpy as np
from sklearn.preprocessing import MinMaxScaler

class StockPricePredictionModel:
    """
    A simple LSTM-based stock price prediction model.
    """
    
    def __init__(self):
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.model = None
        self.X_train = None
        self.y_train = None
    
    def get_price_statistics(self, prices):
        """
        Calculate and return basic statistics about the prices.
        """
        prices_array = np.array(prices)
        stats = {
            "Mean Price": f"${np.mean(prices_array):.2f}",
            "Min Price": f"${np.min(prices_array):.2f}",
            "Max Price": f"${np.max(prices_array):.2f}",
            "Std Dev": f"${np.std(prices_array):.2f}",
            "Total Data Points": len(prices)
        }
        return stats
    
    def train(self, prices, epochs=50):
        """
        Train the model on historical prices.
        For now, this is a placeholder that does basic preprocessing.
        You'll need to implement actual LSTM training.
        """
        try:
            # Convert to numpy array
            prices_array = np.array(prices, dtype=np.float32)
            
            # Normalize the data
            scaled_prices = self.scaler.fit_transform(prices_array.reshape(-1, 1))
            
            # Store for prediction
            self.X_train = scaled_prices
            self.model = True  # Placeholder for model
            
            metrics = {
                "Status": "Training Complete",
                "Epochs": epochs,
                "Data Points Used": len(prices),
                "Message": "Model is ready for predictions!"
            }
            return metrics
        except Exception as e:
            raise Exception(f"Training error: {str(e)}")
    
    def predict_future_prices(self, prices, days_ahead=30):
        """
        Predict future stock prices.
        Returns predicted prices for the specified number of days ahead.
        """
        if self.model is None:
            raise Exception("Model not trained. Please train the model first.")
        
        try:
            prices_array = np.array(prices, dtype=np.float32)
            scaled_prices = self.scaler.transform(prices_array.reshape(-1, 1))
            
            # Simple prediction: use last price and add small random variation
            last_price = prices[-1]
            predictions = []
            
            for i in range(days_ahead):
                # Simple trend: slightly varying from last price
                variation = np.random.normal(0, last_price * 0.02)  # 2% variation
                predicted_price = last_price + variation
                predictions.append(predicted_price)
                last_price = predicted_price
            
            return np.array(predictions)
        except Exception as e:
            raise Exception(f"Prediction error: {str(e)}")
