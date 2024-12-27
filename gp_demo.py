# Required libraries
# !pip install gpy
import numpy as np
import GPy

# 1. Generate training data
# Randomly generate 10 samples of 3D input data
X = np.random.rand(10, 3)  # 10 samples, each with 3 features

# Generate 16D output data based on a random relationship
# Example function: quadratic sum of input features with random coefficients
coefficients = np.random.rand(3, 16)  # Random coefficients for 3 -> 16 mapping
Y = X @ coefficients + np.random.normal(0, 0.1, (10, 16))  # Add small noise

# 2. Create and configure the GPR model
# RBF kernel for input_dim=3 (3D input space)
kernel = GPy.kern.RBF(input_dim=3, variance=1.0, lengthscale=1.0)

# Use Gaussian Process Regression for multivariate output
# Each dimension of the output is treated as a separate regression problem
m = GPy.models.GPRegression(X, Y, kernel)

# 3. Optimize the model
# Optimize hyperparameters to improve the fit
m.optimize_restarts(num_restarts=5)

# 4. Generate new test data for prediction
# 5 new samples of 3D input data
pred_array = np.random.rand(5, 3)

# Predict the corresponding 16D outputs
predictions, uncertainties = m.predict(pred_array)

# 5. Evaluate the results
# Generate true outputs based on the same relationship
true_array = pred_array @ coefficients

# Calculate the error
error = np.abs(predictions - true_array)

# 6. Print results
print("Predictions (5x16):\n", predictions)
print("\nTrue Values (5x16):\n", true_array)
print("\nError (5x16):\n", error)
