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
[^2]: PS + PL, programmable logic.

#### Table 2: Execution Time on CPU, 4T GPU, FPGA (Full CNN) on MNIST Datasets

| Dataset                | CPU (ms) | GPU (ms)     | FPGA (ms)  |
|------------            |------------|------------|------------|
| Handwritten digits     |1931.23     |727.25      | 3.84       |
| Fashion                |1940.01     |653.84      | 2.59       |
| Kuzushiji              |1898.00     |710.30      | 2.61       |


#### Regression model
- t = A L<sup>n</sup> (ms).
- Speed up = t<sub>CPU</sub>/t<sub>FPGA</sub> =109.33 L<sup>0.464</sup> (times).
[^1]: PS, processing system.
[^2]: PS + PL, programmable logic.

## Dataset

[1] "MNIST Handwritten Digits Dataset". Available: https://www.kaggle.com/datasets/hojjatk/mnist-dataset.

[2] "Fashion MNIST Dataset". Available: https://www.kaggle.com/datasets/zalando-research/fashionmnist.

[3] "Kuzushiji MNIST Dataset". Available: https://www.kaggle.com/datasets/anokas/kuzushiji.
