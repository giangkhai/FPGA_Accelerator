# CNN Training 
## Dataset
We use the MNIST dataset available at the following link:
[MNIST Handwritten](https://www.kaggle.com/datasets/hojjatk/mnist-dataset)
[MNIST Fashion](https://www.kaggle.com/datasets/zalando-research/fashionmnist)
[MNIST Kuzushiji](https://paperswithcode.com/dataset/kuzushiji-mnist)
## Project Workflow
### 1. Train CNN Model
- Define and train a Convolutional Neural Network (CNN) model.
- Save as keras file.

### 2. Download and Prepare Dataset
- Download the MNIST dataset from Kaggle.
- Load and preprocess the dataset.
- Save the dataset as a pickle file.

### 4. Convert to TensorFlow Lite
- Convert the trained CNN model to TensorFlow Lite (tflite) format.

## Files
- `mnist_data.pkl` – Pickle file containing the MNIST dataset.
- `model.tflite` – Trained CNN model in TensorFlow Lite format.

## Conclusion
This project provides a step-by-step guide to training a CNN on the MNIST dataset, converting the dataset to pickle format, and exporting the trained model to TensorFlow Lite. This is useful for deploying models to edge devices or mobile platforms.

