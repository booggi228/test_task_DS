import numpy as np
from abc import ABC, abstractmethod

class DigitClassificationInterface(ABC):
    """
    Interface for digit classification models.
    """

    @abstractmethod
    def predict(self, image):
        """
        Predict the digit in the given image.

        Args:
            image (numpy.ndarray): Input image according to the model requirements.

        Returns:
            int: The predicted digit.
        """
        pass

class ConvolutionalNeuralNetwork(DigitClassificationInterface):
    """
    Convolutional Neural Network model for digit classification.
    """

    def predict(self, image):
        # Ensure the input shape is 28x28x1
        if image.shape != (28, 28, 1):
            raise ValueError("Invalid input shape for CNN. Expected (28, 28, 1).")
        raise NotImplementedError("CNN prediction not implemented.")

class RandomForestClassifier(DigitClassificationInterface):
    """
    Random Forest model for digit classification.
    """

    def predict(self, image):
        # Ensure the input is a 1D array of length 784
        if image.ndim != 1 or len(image) != 784:
            raise ValueError("Invalid input shape for Random Forest. Expected 1D array of length 784.")
        raise NotImplementedError("Random Forest prediction not implemented.")

class RandomModel(DigitClassificationInterface):
    """
    Random model for digit classification (for simplicity).
    """

    def predict(self, image):
        # Center crop the image to 10x10
        center_crop = image[9:-9, 9:-9]  # This will give a 10x10 center crop
        if center_crop.shape != (10, 10):
            raise ValueError("Invalid input shape for Random Model. Expected (10, 10) after center crop.")
        # Return a random digit
        return np.random.randint(0, 10)

class DigitClassifier:
    """
    Digit classifier that can use different models for prediction.
    """

    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.model = self._create_model()

    def _create_model(self):
        if self.algorithm == "cnn":
            return ConvolutionalNeuralNetwork()
        elif self.algorithm == "rf":
            return RandomForestClassifier()
        elif self.algorithm == "rand":
            return RandomModel()
        else:
            raise ValueError("Invalid algorithm specified.")

    def predict(self, image):
        """
        Predict the digit in the given image using the selected algorithm.

        Args:
            image (numpy.ndarray): A 28x28x1 image.

        Returns:
            int: The predicted digit.
        """
        return self.model.predict(image)