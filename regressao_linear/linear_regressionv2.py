import numpy as np

class MyLinearRegression():
    def __init__(self,learning_rate=0.01, n_iterations=1000):
        self.intercept = None
        self.coefficients = None
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        #self.theta = None

    def fit(self, X,y):
        Xb = np.c_[np.ones((X.shape[0],1)),X]
        # self.theta = np.linalg.inv(Xb.T.dot(Xb)).dot(Xb.T).dot(y) # para poucos dados essa linha funciona, porém para muitos dados não
        m,n = Xb.shape
        self.theta = np.zeros(n)
        for _ in range(self.n_iterations):
            gradients = (2/m) * Xb.T.dot(Xb.dot(self.theta)- y) # conforme passo intermediário da derivação de (Xb-y)^T (Xb-y)
            self.theta -= self.learning_rate * gradients #subtrai pq queremos o ponto de mínimo, nao de máximo
        self.intercept = self.theta[0]
        self.coefficients = self.theta[1:]

    def predict(self,X):
        Xb = np.c_[np.ones((X.shape[0],1)),X]
        return Xb.dot(np.r_[self.intercept,self.coefficients])