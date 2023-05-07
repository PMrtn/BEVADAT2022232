import numpy as np

class Dense:
    def __init__(self, n_output, n_input=None):
        self.layer_input = None
        self.n_input = n_input
        self.n_output = n_output
        self.trainable = True
        self.W = None
        self.bias = None
        self.initialize()

    def initialize(self):
        # Initialize the weights
        np.random.seed(42)
        self.W = np.random.normal(0.0, 1, (self.n_input, self.n_output))
        self.bias = np.random.random(size=(self.n_output))

    def forward_pass(self, X):
        self.y_pred = np.dot(X, self.W) + self.bias
        return self.y_pred
    
class ReLU():
    def forward_pass(self, X):
        return np.maximum(0, X)