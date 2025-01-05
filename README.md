## Host PC CNN Training 
### 1. Train CNN Model
- Define and train a CNN model.
- Save as keras file.

### 2. Download and Prepare Dataset
- Download the MNIST dataset from Kaggle.
- Load and preprocess the dataset.
- Save the dataset as a pickle file.

### 3. Convert to TensorFlow Lite
- Convert the trained CNN model to TensorFlow Lite (tflite) format.

## Files
- `pickle_conv.py` – Pickle convertor.
- `tflite_conv.py` – Keras to tflite convertor.


### Table 1: Execution Time on FPGA and CPU for 2D Convolution with Various Kernels

| **Kernel**         | **Sobel time (ms)**                     | **Laplacian time (ms)**                 | **Prewitt time (ms)**                  |
|--------------------|-----------------------------------------|-----------------------------------------|----------------------------------------|
|                    | **PS + PL** | **PS**                     | **PS + PL** | **PS**                     | **PS + PL** | **PS**                     |
| **Image size**      |             |                             |             |                             |             |                             |
|--------------------|-------------|-----------------------------|-------------|-----------------------------|-------------|-----------------------------|
| 32 × 32            | 1.249       | 541                         | 1.324       | 525                         | 1.324       | 545                         |
| 64 × 64            | 2.291       | 2312                        | 2.668       | 2266                        | 2.319       | 2189                        |
| 128 × 128          | 6.686       | 9206                        | 7.507       | 9449                        | 7.020       | 9381                        |
| 512 × 512          | 93.908      | 156785                      | 93.687      | 158426                      | 95.277      | 155178                      |


## Dataset
The following datasets were used in this project:

[1] "MNIST Handwritten Digits Dataset". Available: https://www.kaggle.com/datasets/hojjatk/mnist-dataset.

[2] "Fashion MNIST Dataset". Available: https://www.kaggle.com/datasets/zalando-research/fashionmnist.

[3] "Kuzushiji MNIST Dataset". Available: https://www.kaggle.com/datasets/anokas/kuzushiji.
