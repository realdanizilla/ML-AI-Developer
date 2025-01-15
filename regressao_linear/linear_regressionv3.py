import numpy as np
from abc import ABC, abstractmethod

class BaseLinearModel(ABC):
    @abstractmethod
    def fit(self, X,y): # exige a implementação de um método fit para todas as classes que herdarem a BaseLinearModel
        pass

class ExactLinearRegression(BaseLinearModel):
    def __init__(self):
        self.intercept = None
        self.coefficients = None
    
    def fit(self, X, y):
        Xb = np.c_[np.ones((X.shape[0],1)),X]
        self.theta = np.linalg.inv(Xb.T.dot(Xb)).dot(Xb.T).dot(y)    
        self.intercept = self.theta[0]
        self.coefficients = self.theta[1:]

class GradientDescentBatchRegression(BaseLinearModel):
    def __init__(self,learning_rate=0.01, n_iterations=1000):
        self.intercept = None
        self.coefficients = None
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
    
    def fit(self, X,y):
        Xb = np.c_[np.ones((X.shape[0],1)),X]
        m,n = Xb.shape
        self.theta = np.zeros(n)
        for _ in range(self.n_iterations):
            gradients = (2/m) * Xb.T.dot(Xb.dot(self.theta)- y) # conforme passo intermediário da derivação de (Xb-y)^T (Xb-y)
            self.theta -= self.learning_rate * gradients #subtrai pq queremos o ponto de mínimo, nao de máximo
        self.intercept = self.theta[0]
        self.coefficients = self.theta[1:]

class MyLinearRegression:
    def __init__(self,method='gradient_descent', **kwargs):
        if method == 'exact':
            self.model = ExactLinearRegression()
        elif method == 'gradient_descent':
            self.model = GradientDescentBatchRegression()
        else:
            raise ValueError("Invalid method. Choose 'exact' or 'gradient_descent'")

    def fit(self,X,y):
        self.model.fit(X,y)
        self.intercept = self.model.intercept
        self.coefficients = self.model.coefficients

    def predict(self,X):
        Xb = np.c_[np.ones((X.shape[0],1)),X]
        return Xb.dot(np.r_[self.intercept,self.coefficients])