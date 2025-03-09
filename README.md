# Intellihack_Sidemen_4

# Stock Price Prediction Challenge

## Exploratory Data Analysis

- **Line Plot**: Compared Close and Adjusted Close prices.  
- **Moving Average**: Analyzed 5-day, 20-day, and 50-day moving averages to observe short-term and long-term trends.  
- **Correlation Matrix**: Identified strong correlations between Close, High, Low, and Open prices.  
- **Volume Analysis**: Determined that Volume had low correlation with Close price and was excluded from the model.  

---

## 🧠 Model Architecture
The final model is an LSTM-based neural network:

| Layer | Units | Activation | Output Shape |
|-------|-------|------------|--------------|
| LSTM (return seq) | 128 | Tanh | (None, 60, 128) |
| LSTM | 64 | Tanh | (None, 64) |
| Dense | 25 | ReLU | (None, 25) |
| Dense | 1 | Linear | (None, 1) |

- **Optimizer**: Adam (learning rate = 0.001)  
- **Loss Function**: Mean Squared Error (MSE)  
- **Sequence Length**: 60 days  

---

## 📈 Training and Evaluation
### ✅ Training
- Trained on **95%** of the dataset.  
- **Batch Size**: 8  
- **Epochs**: 10 (can be increased for better performance)  

### ✅ Evaluation
- **Root Mean Squared Error (RMSE):**  
```bash
RMSE: {rmse:.4f}
## Directional Accuracy
Measures how often the model correctly predicts the direction of price movement.

---

## 📅 Prediction for Next 5 Days
| Day | Predicted Close Price (USD) |
|------|-----------------------------|
| Day 1 | `{future_predictions[0][0]}` |
| Day 2 | `{future_predictions[1][0]}` |
| Day 3 | `{future_predictions[2][0]}` |
| Day 4 | `{future_predictions[3][0]}` |
| Day 5 | `{future_predictions[4][0]}` |

---

## ⚠️ Limitations
- Model struggles with extreme market volatility.  
- Insufficient data volume for robust generalization.  
- No external market data (e.g., interest rates, news events) included in the model.  

---

## 💡 Proposed Improvements
- Include more external market indicators (e.g., interest rates, GDP data).  
- Teat with training epochs and sequence length for improved accuracy. 
- Generate Dataset

---

## 📜 Reproduction Guide
### ✅ Preprocessing
1. Load the CSV file.  
2. Fill missing values using a **5-day rolling mean**.  
3. Scale data using **MinMaxScaler**.  

### ✅ Training
1. Create training sequences (60-day window).  
2. Train LSTM model with **128 and 64 units**.  
3. Evaluate using **RMSE** and **directional accuracy**.  

### ✅ Prediction
1. Use the final sequence to predict next 5 days.  
2. Inverse transform the results using the scaler.  
3. Save predictions to **future_predictions.csv**.  

---

## 📄 Results
| Metric | Value |
|--------|-------|
| RMSE | `{rmse:.4f}` |
| Directional Accuracy | `{directional_accuracy}%` |

---



---

## ✅ License
This project is licensed under the **Apache License** – see the LICENSE file for details.

---
