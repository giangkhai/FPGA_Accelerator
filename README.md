## Host PC CNN Training 
### 1. CNN Model 
- Define and train a CNN model.
  
| Layer (type)                       | Output  Shape     | Param #     |
|------------                        |-----------------  |------------ |
| conv2d_1 (Conv2D)                  |(None, 24, 24, 16) |416          | 
| max_pooling2d_1 (MaxPooling2D)     |(None, 6, 6, 16)   |0            | 
| flatten_1 (Flatten)                |(None, 576)        |0            |
| dropout_1 (Dropout)                |(None, 576)        |0            |
| dense_1 (Dense)                    |(None, 10)         |5770        |

- Save as keras file.

### 2. Download and Prepare Dataset
- Download the MNIST dataset from Kaggle.
- Load and preprocess the dataset.
- Save the dataset as a pickle file.

### 3. Convert to TensorFlow Lite
- Convert the trained CNN model to TensorFlow Lite (tflite) format.
- Convert tflite file to weight with npy format if FPGA doesn't have TensorFlow Lite (optinal).

## Files
- `pickle_conv.py` – Pickle convertor.
- `tflite_conv.py` – Keras to tflite convertor.
- `npy_conv.py` – tflite to npy convertor.

## Deployment on FPGA 
### 1. CNN Overlays
- Source files and project configurations for creating CNN overlays on the FPGA are available in the Vitis folder.

### 2. Running CNN on FPGA
- Jupyter Notebook scripts for running the trained CNN model on the FPGA are available in the Jupyter folder.
- The overlays in the folder were created using the 2021.2 HLS tool and are running on PYNQ version 2.7.

## Results
#### Table 1: Execution Time on FPGA and CPU for 2D Convolution on Gray images

| Image Size - L | FPGA [^1] (ms) | CPU [^2] (ms)     |
|------------|-----------------|------------|
| 32 × 32    |1.3              |537         | 
| 64 × 64    |2.43             |2255.67     | 
| 128 × 128  |7.07             |9345.33     | 
| 512 × 512  |94.29            |156796.3    |

#### Regression model
- t = A L<sup>n</sup> (ms).
- Speed up = t<sub>CPU</sub>/t<sub>FPGA</sub> =109.33 L<sup>0.464</sup> (times).
[^1]: PS, processing system.
[^2]: PS + PL, programmable logic PYNQ-Z2.

#### Table 2: Execution Time on CPU, T4 GPU, FPGA (Full CNN) on MNIST Datasets (10,000 samples)

| Dataset                | CPU (ms) | T4 GPU (ms)     | FPGA (ms)  |
|------------            |------------|------------|------------|
| Handwritten digits     |1931.23     |727.25      | 3.84       |
| Fashion                |1940.01     |653.84      | 2.59       |
| Kuzushiji              |1898.00     |710.30      | 2.61       |


## Dataset

[1] "MNIST Handwritten Digits Dataset". Available: https://www.kaggle.com/datasets/hojjatk/mnist-dataset.

[2] "Fashion MNIST Dataset". Available: https://www.kaggle.com/datasets/zalando-research/fashionmnist.

[3] "Kuzushiji MNIST Dataset". Available: https://www.kaggle.com/datasets/anokas/kuzushiji.

## Contributors
- Project by: Khai Giang-Mien and Nguyen Phan-Nguyen-Khoi
