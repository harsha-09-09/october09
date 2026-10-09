from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load California Housing dataset
data = fetch_california_housing()

X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "california1.joblib")

print("Model trained successfully!")
print("Model saved as california1.joblib")