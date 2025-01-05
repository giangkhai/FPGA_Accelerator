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

| Image Size - L | FPGA (ms) | CPU (ms)   |
|------------|-----------------|------------|
| 32 × 32    | 1.3          | 537      | 
| 64 × 64    | 2.43         | 2255.67      | 
| 128 × 128  | 7.07          | 9345.33      | 
| 512 × 512  | 94.29    | 156796.3   |
#### For sequential computation 
$\tau$<sub>CPU</sub> ∼ (L+1 - S)<sup>2</sup> = O(L<sup>2</sup>)
#### For FPGA computation
$\tau$<sub>FPGA</sub> ∼ O(L<sup>$\beta$</sup>)
#### Regression model
$\tau$ = $\alpha \cdot$ $L$<sup>$\beta$</sup>
## Dataset
The following datasets were used in this project:

[1] "MNIST Handwritten Digits Dataset". Available: https://www.kaggle.com/datasets/hojjatk/mnist-dataset.

[2] "Fashion MNIST Dataset". Available: https://www.kaggle.com/datasets/zalando-research/fashionmnist.

[3] "Kuzushiji MNIST Dataset". Available: https://www.kaggle.com/datasets/anokas/kuzushiji.
