model.save('my_model.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save model into .tflite file
with open('cnn.tflite', 'wb') as f:
    f.write(tflite_model)
