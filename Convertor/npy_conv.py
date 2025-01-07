import tensorflow as tf
import numpy as np

# Load the TFLite model
with open('model.tflite', 'rb') as f:
    tflite_model = f.read()

# Initialize and allocate the TFLite interpreter
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

# Print input and output details
print("Input Details:", interpreter.get_input_details())
print("Output Details:", interpreter.get_output_details())

# Function to extract and save kernel weights
def save_weights(interpreter, tensor_index, save_path):
    weights = np.array(interpreter.tensor(tensor_index)())  # Get weights
    np.save(save_path, weights)  # Save as numpy file
    print(f"Saved weights (index {tensor_index}, shape {weights.shape}) to {save_path}")

# Example usage
# save_weights(interpreter, tensor_index=0, save_path="weights.npy")
