import numpy as np
import matplotlib.pyplot as plt

class TinyNN:
    def __init__(self, input_dim, hidden_dim, output_dim, lr=0.1):
        self.W1 = np.random.randn(input_dim, hidden_dim)
        self.b1 = np.zeros((1, hidden_dim))

        self.W2 = np.random.randn(hidden_dim, output_dim)
        self.b2 = np.zeros((1, output_dim))

        self.lr = lr

    def forward(self, X):
        self.z1 = X @ self.W1 + self.b1
        self.a1 = np.maximum(0, self.z1) #ReLU

        self.z2 = self.a1 @ self.W2 + self.b2
        self.a2 = 1 / (1 + np.exp(-self.z2)) #Sigmoid

        return self.a2

    def backward(self, X, y):
        m = y.shape[0]

        #dLoss/dOutput
        dz2 = (self.a2 - y) #derivative of BCE with sigmoid

        dW2 = self.a1.T @ dz2 / m
        db2 = np.sum(dz2, axis=0, keepdims = True) / m
        
        #Backprop through ReLU
        da1 = dz2 @ self.W2.T
        dz1 = da1 * (self.z1 > 0)

        dW1 = X.T @ dz1 / m
        db1 = np.sum(dz1, axis=0, keepdims = True) / m

        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1
        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2

    def train(self, X, y, epochs=5000):
        losses = []

        for i in range(epochs):
            out = self.forward(X)
            loss = -np.mean(y * np.log(out+1e-9) +
                            (1-y) * np.log(1 - out + 1e-9))
            losses.append(loss)

            self.backward(X, y)

        return losses
if __name__ == "__main__":
    X = np.array([[0,0],[0,1],[1,0],[1,1]])
    y = np.array([[0],[1],[1],[0]])

    model = TinyNN(2, 4, 1, lr=0.1)
    losses = model.train(X, y)

    plt.plot(losses)
    plt.title("Loss Curve")
    plt.savefig("loss_curve.png")
    plt.show()

    print(model.forward(X))
    