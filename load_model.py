from keras.models import load_model
from keras.layers import DepthwiseConv2D

# Define custom DepthwiseConv2D if necessary
def custom_depthwise_conv2d(*args, **kwargs):
    kwargs.pop('groups', None)  # Remove 'groups' if it's not recognized
    return DepthwiseConv2D(*args, **kwargs)

# Load the model
def load_trained_model():
    model_path = '/Users/miguelangel/Downloads/conv_MLP_84.h5'
    model_cnn = load_model(model_path, custom_objects={'DepthwiseConv2D': custom_depthwise_conv2d}, compile=False)
    
    # Compile the model with appropriate loss and optimizer
    model_cnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model_cnn
