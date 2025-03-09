# Intellihack_Sidemen_4

# Stock Price Prediction Challenge


## Reports
- [Report available at Intellihack_Sidemen_4_report_part1.pdf](./Intellihack_Sidemen_4_report_part1.pdf)  
- [Report available at Intellihack_Sidemen_4_report_part2.pdf](./Intellihack_Sidemen_4_report_part2.pdf)  

## Exploratory Data Analysis

- **Line Plot**: Compared Close and Adjusted Close prices.  
- **Moving Average**: Analyzed 5-day, 20-day, and 50-day moving averages to observe short-term and long-term trends.  
- **Correlation Matrix**: Identified strong correlations between Close, High, Low, and Open prices.  
- **Volume Analysis**: Determined that Volume had low correlation with Close price and was excluded from the model.  

---

## Model Architecture
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

## Training and Evaluation
### Training
- **Batch Size**: 8  
- **Epochs**: 10 (can be increased for better performance)  

### Evaluation
```bash
RMSE: 3.65
MSE: 2.65
```

## Directional Accuracy
Measures how often the model correctly predicts the direction of price movement.

```bash

## Prediction for Next 5 Days
| Day | Predicted Close Price (USD) |
|------|-----------------------------|
| Day 1 | [200.5243 ] |
| Day 2 | [201.29904] |
| Day 3 | [201.97197] |
| Day 4 | [202.63661] |
| Day 5 | [203.34831] |


```

## Limitations
- Model struggles with extreme market volatility.  
- Insufficient data volume for robust generalization.  
- No external market data (e.g., interest rates, news events) included in the model.  



## Proposed Improvements
- Include more external market indicators (e.g., interest rates, GDP data).  
- Teat with training epochs and sequence length for improved accuracy. 
- Generate Dataset



## Reproduction Guide
### Preprocessing
1. Load the CSV file.  
2. Fill missing values using a **5-day rolling mean**.  
3. Scale data using **MinMaxScaler**.  

### Training
1. Create training sequences (60-day window).  
2. Train LSTM model with **128 and 64 units**.  
3. Evaluate using **RMSE** and **directional accuracy**.  

### Prediction
1. Use the final sequence to predict next 5 days.  
2. Inverse transform the results using the scaler.  
3. Save predictions to **future_predictions.csv**.  

```bash

## Results
| Metric | Value |
|--------|-------|
| RMSE   | 3.65  |
| MSE    | 2.65  |
| Directional Accuracy | 49.55% |

```
## License
This project is licensed under the **Apache License** – see the LICENSE file for details.


