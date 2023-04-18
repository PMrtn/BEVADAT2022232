import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.L = lr
        self.epochs = epochs
        self.m = 0
        self.c = 0



    def fit(self, X: np.array, y: np.array):
        n = float(len(X))

        losses = []
        for i in range(self.epochs): 
            y_pred = self.m*X + self.c  # The current predicted value of Y

            residuals = y_pred - y
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(X * residuals)  # Derivative wrt m
            D_c = (-2/n) * sum(residuals)  # Derivative wrt c
            self.m = self.m + self.L * D_m  # Update m
            self.c = self.c + self.L * D_c  # Update c
            if i % 100 == 0:
                print(np.mean(y-y_pred))
        return losses



    def predict(self, X):
        self.pred = []
        for x in X:
            y_pred = self.m*x + self.c
            self.pred.append(y_pred)

        y_pred = self.m*X + self.c

        return y_pred