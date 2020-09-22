from abc import ABC, abstractmethod
from typing import List, Union

import numpy as np


class Embedding(ABC):
    """
    Embedding base class
    """

    @abstractmethod
    def create_vector(self, input) -> np.array:
        """
        :param input:
        :return: Vector.
        :rtype: numpy array.
        """
        raise NotImplementedError


class TextEmbedding(Embedding):
    """
    Text Embedding base class
    """
    def __init__(self):
        self.feature_names = []

    @abstractmethod
    def create_vector(self, input: Union[str, List[str]]) -> np.array:
        """
        With n documents, w features
        :param input: Input from tokenizer, type 'str' or 'list of str'.
        :return: Vector, shape (n, w).
        :rtype: numpy array.
        """
        raise NotImplementedError

    def get_feature_names(self) -> List:
        return self.feature_names

    @staticmethod
    def validate_input(input):
        """
        Check input that is str or list of str.
        :param input: str or list of str.
        :return: ValueError if not fit for the conditions.
        """
        if type(input) is str:
            pass
        elif type(input) is list:
            for text in input:
                if type(text) is not str:
                    raise ValueError("Type of input is not correct. "
                                     "Expected 'str' or 'list of str', but got ", type(text))
            pass
        else:
            raise ValueError("Type of input is not correct. "
                             "Expected 'str' or 'list of str', but got ", type(input))
