import pickle
from tensorflow.keras.datasets import fashion_mnist

# Load Fashion-MNIST dataset
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# Save the dataset into a .pkl file
with open("fashion_mnist.pkl", "wb") as f:
    pickle.dump(((x_train, y_train), (x_test, y_test)), f)

print("fashion_mnist.pkl has been created!")
