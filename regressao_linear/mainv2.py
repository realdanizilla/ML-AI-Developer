import numpy as np
from linear_regressionv2 import MyLinearRegression

y = np.array([10,50,100,200,70,20,19])

X = np.array([
    [30,7,1,1.5,2],
    [40,10,0,1.6,4],
    [50,20,1,1.7,5],
    [60,12,0,1.8,7],
    [25,10,1,1.65,7],
    [24,12,0,1.62,0],
    [32,22,1,1.90,0]
])

mean = np.mean(X, axis=0)
std = np.std(X, axis=0)
X_standardized = (X - mean) / std

model = MyLinearRegression()
model.fit(X_standardized,y)
a = model.predict(np.array([[35,45,0,1.78,4]]))
print(a)
print(model.intercept)
print(model.coefficients)