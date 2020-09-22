from abc import ABC, abstractmethod

import numpy as np


class DistanceFunction(ABC):
    """
    Distance Function base class.
    """
    def __call__(self, x, y):
        return self.calculate_dist(x, y)

    @abstractmethod
    def calculate_dist(self, x: np.array, y: np.array) -> np.array:
        """
        Calculate distances with the specific distance functions.
        :param x: array-like, shape (n_samples_1, n_features)
        :param y: array-like, shape (n_samples_2, n_features)
        :return: distances of x and y, shape (n_sample_1, n_sample_2)
        :rtype: np.array
        """
        raise NotImplementedError
