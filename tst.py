# Library Import
import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Size": [500, 700, 900, 1100, 1300],
    "Rent": [8000, 12000, 16000, 20000, 24000]
}

# DataFrame
df = pd.DataFrame(data)

# Dataset Print
print(df)

# Feature (Input)
X = df[["Size"]]

# Target (Output)
y = df["Rent"]

# Model Create
model = LinearRegression()

# Train Model
model.fit(X, y)

# Prediction
prediction = model.predict([[1000]])

# Output
print("Predicted Rent =", prediction[0])

# Slope
print("Slope =", model.coef_[0])

# Intercept
print("Intercept =", model.intercept_)